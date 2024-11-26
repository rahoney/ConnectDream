# ConnectDream
Corporate Collaboration Project -Memorial Service Assistance  
ConnectDream은 2024년 이어드림스쿨 4기에서 진행된 기업연계 프로젝트입니다.  
연계기업(커넥트브릭)으로부터 B2B 상조서비스에 사용할 수 있는 서비스를 기획을 하고 구현하는 프로젝트입니다.   
🚀 Team Members  
[곽라흔](https://github.com/rahoney) [성지아](https://github.com/jiasung00)  
Supported by [(주)커넥트브릭](https://connectbrick.com/)  
그 결과를 오픈소스 프로젝트로 정리했습니다.  

### ConnectDream - Video Demo  
https://github.com/user-attachments/assets/78cbaae1-fca3-4434-8e22-6da7f7ba8f44  
  
## Index
  - [About The Project](#about-the-project) 
  - [Overview](#overview)
  - [Model Configuration](#Model-Configuration)
  - [Getting Started](#getting-started)
  - [Tech Stack](#tech-stack)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)  
인공지능 생성형 이미지를 활용하여 상조 서비스로 쓰일 수 있는 기획과 구현을 목표로 한 프로젝트입니다.  
저희는 본 프로젝트에서 3가지 기획안을 구현하는 Task를 수행했습니다.  
1. 고인 또는 죽음을 앞둔 분의 일상 사진을 1장 입력에 사용하여 스튜디오에서 촬영한 것 같은 영정 사진을 생성하는 Task입니다.  
2. 3장의 이미지를 입력에 사용하여 생전에 꿈이였거나 취미였던 노래하는 모습을 생성하는 Task입니다.  
3. 유가족을 위해 정적인 영정 사진을 넘어서 보다 생동감있는 모습의 영상으로 구현하는 Task입니다.  

ComfyUI를 이용하여 이미지 생성을 구현하였고, 배포는 Gradio를 활용하여 한 화면에서 구현했습니다.  

<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Architecture.png" alt="Architecture" width="500">  
## Overview  
<!-- Write Overview about this project -->
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/스크린샷_IDPhoto.png" alt="스크린샷_IDPhoto" width="500">
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_Output.png" alt="Task1_Output" width="500">
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Screenshot_IDPhoto.png" alt="Screenshot_IDPhoto" width="500">
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_Output.png" alt="Task1_Output" width="500">



## Model Configuration  
**영정 사진 생성**  
checkpoint model: DreamShaperXL v2.1 turbo DPMSDE  
LoRA: ip-adapter faceid pluse v2 sdxl  
Controlnet: Instantid sdxl  

**노래하는 이미지 생성**  
checkpoint model: DreamShaperXL-v2.1-turboDPMSDE  
LoRA: epiCRealismHelper  
Controlnet: TTplanet sdxl v20 fp16  
CLIP: ViT H 14 laion 2B s32B b79k  
  
**영정 사진 만들기**  
CLIP: fluxTextencoderT5XxlFp8v10  
CogVideo Model: CogVideoX 5b I2V / bf16  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Tech Stack
- ![Python](https://path-to-your-python-icon.png) **Programming Language**: Python 3.12
- ![Stable Diffusion](https://path-to-your-stable-diffusion-icon.png) **Base Model**: Stable Diffusion
- ![ComfyUI](https://path-to-your-comfyui-icon.png) **Tools**: ComfyUI, Gradio
- ![AWS EC2](https://path-to-your-aws-ec2-icon.png) **Cloud Infrastructure**: AWS EC2, GPU Server
- ![NVIDIA](https://path-to-your-nvidia-icon.png) **GPU Server**: NVIDIA L4, A10
- 영상 생성을 위해서는 최소 24GB VRAM의 GPU를 사용하는 것이 안정적입니다.
