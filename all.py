import base64
import gradio as gr
import requests
import json
from PIL import Image
import numpy as np
from io import BytesIO
import time
import os

# Safehttpx 검증 비활성화
os.environ["SAFEHTTPX_TRUSTED_HOSTS"] = "localhost,127.0.0.1"
os.environ["SAFEHTTPX_DISABLE"] = "1"

PORT = 7778  # Gradio 서버 포트 번호
COMFYUI_PORT = 8688
COMFYUI_API_URL = f"http://localhost:{COMFYUI_PORT}/api/prompt"

# JSON 경로 설정
WORKFLOW_API_PATH_IMAGE = "./workflow_api_1.json"  # 영정사진
WORKFLOW_API_PATH_ENHANCE = "./workflow_api_dream.json"  # 인생더하기
WORKFLOW_API_PATH_VIDEO = "./workflow_api_video_11.json"  # 메모리얼 비디오

# 노드 ID 설정
NODE_IMAGE_INPUT = "68"  
NODE_IMAGE_OUTPUT = "69"  
NODE_ENHANCE_INPUTS = ["28", "29", "30"]  
NODE_ENHANCE_OUTPUT = "31"  
NODE_VIDEO_INPUT = "38"  
NODE_VIDEO_OUTPUT = "31"

# Helper function to convert image to base64
def convert_image_to_base64(image):
    """Convert an ndarray or PIL image to base64."""
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Modify workflow JSON for image processing
def modify_image_workflow_json(image, workflow_path, input_node_id):
    try:
        with open(workflow_path, "r") as file:
            workflow_data = json.load(file)

        # 이미지를 base64로 변환
        encoded_image = convert_image_to_base64(image)

        # 입력 이미지 추가
        if input_node_id in workflow_data:
            workflow_data[input_node_id]["inputs"]["base64_data"] = encoded_image
        else:
            print(f"Node ID {input_node_id} not found in workflow.")
            return None
        return {"prompt": workflow_data}
    except Exception as e:
        print(f"Error modifying workflow: {e}")
        return None

# Modify workflow JSON for multiple images (e.g., 인생더하기)
def modify_enhance_workflow_json(images, workflow_path, input_node_ids):
    try:
        with open(workflow_path, "r") as file:
            workflow_data = json.load(file)

        # 단일 이미지를 리스트로 변환
        for img, node_id in zip(images, input_node_ids):
            encoded_image = convert_image_to_base64(img)
            if node_id in workflow_data:
                workflow_data[node_id]["inputs"]["base64_data"] = encoded_image
            else:
                print(f"Node ID {node_id} not found in workflow.")
                return None
        return {"prompt": workflow_data}
    except Exception as e:
        print(f"Error modifying workflow: {e}")
        return None

# Modify workflow JSON for video processing
def modify_video_workflow_json(image, workflow_path, input_node_id):
    return modify_image_workflow_json(image, workflow_path, input_node_id)

# Check status
def check_status(prompt_id, output_node_id, max_attempts=100, interval=10, output_type="images"):
    """Check generation status for images or videos."""
    try:
        history_url = f"http://localhost:{COMFYUI_PORT}/history/{prompt_id}"
        for attempt in range(max_attempts):
            print(f"Checking status (attempt {attempt + 1}/{max_attempts})...")
            response = requests.get(history_url, timeout=10)
            if response.status_code == 200:
                history_data = response.json().get(prompt_id, {})
                outputs = history_data.get("outputs", {})
                if output_node_id in outputs and output_type in outputs[output_node_id]:
                    output_info = outputs[output_node_id][output_type][0]
                    filename = output_info.get("filename")
                    if filename:
                        if output_type == "images":
                            img_url = f"http://localhost:{COMFYUI_PORT}/view?filename={filename}&type=output"
                            img_response = requests.get(img_url, timeout=10)
                            if img_response.status_code == 200:
                                return Image.open(BytesIO(img_response.content))
                        elif output_type == "gifs":
                            video_url = f"http://localhost:{COMFYUI_PORT}/view?filename={filename}&type=output"
                            video_response = requests.get(video_url, stream=True, timeout=20)
                            if video_response.status_code == 200:
                                local_path = f"./{filename}"
                                with open(local_path, "wb") as f:
                                    f.write(video_response.content)
                                return local_path
            time.sleep(interval)
        print("Timeout waiting for generation.")
        return None
    except Exception as e:
        print(f"Error checking status: {e}")
        return None

# Generate content
def generate_image(image, workflow_path, input_node_id, output_node_id):
    payload = modify_image_workflow_json(image, workflow_path, input_node_id)
    return send_request_and_check(payload, output_node_id, output_type="images")

def generate_enhance(images, workflow_path, input_node_ids, output_node_id):
    payload = modify_enhance_workflow_json(images, workflow_path, input_node_ids)
    return send_request_and_check(payload, output_node_id, output_type="images")

def generate_video(image, workflow_path, input_node_id, output_node_id):
    payload = modify_video_workflow_json(image, workflow_path, input_node_id)
    return send_request_and_check(payload, output_node_id, output_type="gifs")

def send_request_and_check(payload, output_node_id, output_type):
    try:
        print("Sending request to ComfyUI...")
        response = requests.post(COMFYUI_API_URL, json=payload, timeout=10)
        response.raise_for_status()
        prompt_id = response.json().get("prompt_id")
        if not prompt_id:
            print("No prompt ID returned from ComfyUI.")
            return None
        return check_status(prompt_id, output_node_id, output_type=output_type)
    except Exception as e:
        print(f"Error sending request: {e}")
        return None

# Gradio Interfaces
iface_generate = gr.Interface(
    fn=lambda image: generate_image(image, WORKFLOW_API_PATH_IMAGE, NODE_IMAGE_INPUT, NODE_IMAGE_OUTPUT),
    inputs=gr.Image(label="입력 이미지"),
    outputs=gr.Image(label="생성된 이미지"),
    title="영정사진 생성",
    description="이미지를 업로드하고 생성 버튼을 클릭하세요."
)

#꿈
iface_enhance = gr.Interface(
    fn=lambda image1, image2, image3: generate_enhance(
        [image1, image2, image3], WORKFLOW_API_PATH_ENHANCE, NODE_ENHANCE_INPUTS, NODE_ENHANCE_OUTPUT
    ),
    inputs=[
        gr.Image(label="첫 번째 입력 이미지"),
        gr.Image(label="두 번째 입력 이미지"),
        gr.Image(label="세 번째 입력 이미지"),
    ],
    outputs=gr.Image(label="생성된 이미지"),
    title="인생 더하기",
    description="세 개의 이미지를 업로드하고 생성 버튼을 클릭하세요."
)

iface_video = gr.Interface(
    fn=lambda image: generate_video(image, WORKFLOW_API_PATH_VIDEO, NODE_VIDEO_INPUT, NODE_VIDEO_OUTPUT),
    inputs=gr.Image(label="입력 이미지"),
    outputs=gr.Video(label="생성된 비디오"),
    title="메모리얼 비디오",
    description="이미지를 업로드하고 비디오를 생성하세요."
)

# Gradio App
with gr.Blocks() as app:
    gr.TabbedInterface(
        [iface_generate, iface_enhance, iface_video],
        tab_names=["영정사진 생성", "인생 더하기", "메모리얼 비디오"]
    )

if __name__ == "__main__":
    print("Starting Gradio server...")
    app.launch(
        server_name="0.0.0.0",
        server_port=PORT,
        share=True,
        allowed_paths=["/home/eardream1/ComfyUI/output/"]
    )
