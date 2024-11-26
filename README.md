# ConnectDream
Corporate Collaboration Project -Memorial Service Assistance  
ConnectDream은 2024년 이어드림스쿨 4기에서 진행된 기업연계 프로젝트입니다.  
연계기업(커넥트브릭)으로부터 B2B 상조서비스에 사용할 수 있는 서비스를 기획을 하고 구현하는 프로젝트입니다.   
🚀 Team Members  
[곽라흔](https://github.com/rahoney) [성지아](https://github.com/jiasung00)  
Supported by [(주)커넥트브릭](https://connectbrick.com/)  
그 결과를 오픈소스 프로젝트로 정리했습니다.  

## Demo
https://github.com/user-attachments/assets/78cbaae1-fca3-4434-8e22-6da7f7ba8f44  

## Index
  - [About The Project](#about-the-project) 
  - [Overview](#overview)
  - [Operational and Deployment Server Specs](#operational-and-deployment-server-specs)
  - [Multi-Server Deployment of ComfyUI and Gradio](#multi-server-deployment-of-comfyui-and-gradio)  
  - [Getting Started](#getting-started)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)

<!-- ABOUT THE PROJECT -->
## About The Project

### ✨ ${\textsf{\color{Indigo}Task 1: 영정 사진 생성}}$
고인 또는 죽음을 앞둔 분의 **일상 사진 1장**을 입력으로 사용하여,  
스튜디오에서 촬영한 것처럼 품격 있는 **영정 사진**을 생성하는 Task입니다.  



### 🎤 ${\textsf{\color{Indigo}Task 2: 꿈과 취미를 반영한 이미지 생성}}$  
**3장의 사진**을 입력으로 받아,  
생전에 꿈이었거나 취미였던 **노래하는 모습**을 생성하는 Task입니다.  



### 🎥 ${\textsf{\color{Indigo}Task 3: 생동감 있는 영정 영상 제작}}$
유가족을 위해 정적인 영정 사진을 넘어,  
**보다 생동감 있는 모습의 영상**으로 구현하는 Task입니다.  


## Overview  
<!-- Write Overview about this project -->
<b>Task 1: 증명사진 스타일의 영정사진 생성</b>  
* 작업 유형: Image-to-Image  
* 목적: 입력 이미지를 스튜디오에서 촬영한 것처럼 정제된 증명사진 또는 영정사진 형태로 변환.  
* 입력: 일반적인 인물 사진.  
* 출력: 깔끔하고 품격 있는 영정사진 스타일의 이미지.  
* 사용된 기술 및 구성:  
  * Checkpoint Model: DreamShaperXL 2.1 turbo DPMSDE  
 고해상도의 정교한 이미지를 생성하며, 조명과 텍스처 표현이 우수하여 영정사진에 적합한 품질을 보장합니다.
  * LoRA: ip-adapter  
입력 얼굴의 주요 특징을 세밀히 분석하여 정제된 스타일 변환을 지원합니다. 얼굴의 비율, 윤곽, 주요 디테일을 유지하며 증명사진 형식으로 전환합니다.  
  * ControlNet: InstantID  
증명사진의 표준적인 구도와 배경을 유지하면서 입력 이미지의 안정성을 강화합니다. 얼굴 중심의 정렬과 배경 보정 작업을 수행하여 정돈된 결과물을 생성합니다.  

<b>Task1 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_IDPhoto.png" alt="Task1 IDPhoto" width="500">
<b>Task1 Output</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_Out.png" alt="Task1 Out" width="300">

<b>Task 2: 생전 좋아했던 노래하는 모습 생성</b>
* 작업 유형: Image-to-Image
* 목적: 고인이 생전에 즐겼던 활동 중 노래하는 모습을 재현한 이미지를 생성.
* 입력: 고인의 생전 사진 3장.
* 출력: 노래하는 모습을 담은 3개의 사실적이고 감정적인 이미지.
* 사용된 기술:
  * Checkpoint Model: DreamShaperXL v2.1 turbo DPMSDE  
고해상도의 사실적 이미지를 생성하며, 감정을 담은 디테일한 장면을 표현합니다.
  * LoRA: epiCRealismHelper  
감정과 디테일을 강화하여 생동감 있는 이미지를 생성하며, 인물의 표정과 자세에서 깊은 사실성을 제공합니다.
  * ControlNet: TTplanet sdxl v20 fp16  
입력된 다중 이미지의 일관성을 유지하며 노래와 관련된 포즈와 배경을 정밀하게 설정합니다.
  * CLIP: ViT H 14 laion 2B s32B b79k  
텍스트와 이미지 간의 의미적 연결을 강화하여 노래라는 주제와 입력 이미지의 관계를 조화롭게 반영합니다.  

<b>Task2 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task2_ImageTransfer.png" alt="Task2 ImageTransfer" width="500">  
<b>Task2 Output</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task2_Out.png" alt="Task2 Out" width="300">

<b>Task 3: 생동감 있는 영상 생성</b>
* 작업 유형: Image-to-Video
* 목적: 정적인 이미지를 기반으로 눈 깜빡임 및 머리카락 움직임과 같은 생동감을 부여한 짧은 영상 생성.
* 입력: 고인의 정적인 이미지 1장.
* 출력: 눈 깜빡임과 머리카락 움직임이 포함된 짧은 애니메이션 영상.
* 사용된 기술:
  * CLIP: fluxTextencoderT5XxlFp8v10  
입력 이미지에서 구현할 세부적인 애니메이션 스타일과 생동감 있는 특성을 분석합니다. 텍스트 정보를 활용하여 자연스러운 움직임을 생성하는 데 사용됩니다.
  * CogVideo Model: CogVideoX 5b I2V / bf16  
정적인 이미지를 기반으로 눈 깜빡임과 머리카락의 움직임을 포함한 자연스러운 영상을 생성합니다. 애니메이션의 현실감을 높이며, 일관성 있는 결과를 보장합니다.

<b>Task3 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task3_Videowork.png" alt="Task3 Videowork" width="500">
<b>Task3 Output</b>  
  
https://github.com/user-attachments/assets/cc32dee4-4617-4134-b5a1-014c5d38279f  
  
<b>Model Configuration</b>  
| Task                | Type             | 주요 모델 및 구성 요소                                | 입력       | 출력       |
|---------------------|------------------|-----------------------------------------------------|------------|------------|
| **Task 1**          | Image-to-Image  | DreamShaperXL, ip-adapter faceid pluse v2 sdxl, Instantid sdxl | 인물 사진  | 영정사진  |
| **Task 2**          | Image-to-Image  | DreamShaperXL, epiCRealismHelper, TTplanet, CLIP   | 사진 3장   | 노래 모습 |
| **Task 3**          | Image-to-Video  | CogVideo, fluxTextencoder                          | 인물 사진  | 짧은 영상 |

  



## Multi-Server Deployment of ComfyUI and Gradio 

## Operational and Deployment Server Specs

| 서버 이름      | GPU Server 1                                                                                     | EC2 GPU                                                                                     | 배포서버                                                                                     |
|----------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **운영체제**   | Linux                                                                                           | Linux (Ubuntu 22.04)                                                                        | Linux (Ubuntu 22.04)                                                                        |
| **EC2 Instance Type** | -                                                                                       | g5.16xlarge                                                                                 | r7i.xlarge                                                                                  |
| **ComfyUI**    | 0.2.4                                                                                           | 0.2.4                                                                                       | -                                                                                           |
| **Python**     | 3.12.3                                                                                          | 3.12.3                                                                                      | 3.11.7                                                                                      |
| **Torch**      | 2.5.0+cu124                                                                                     | 2.5.0+cu124                                                                                 | -                                                                                           |
| **GPU**        | NVIDIA L4                                                                                       | NVIDIA A10G (4 GPUs)                                                                        | -                                                                                           |
| **vCPUs**      | -                                                                                               | 64                                                                                          | 4                                                                                           |
| **RAM**        | 47 GiB                                                                                          | 256 GiB                                                                                     | 32 GiB                                                                                      |
| **스토리지**   | 1TB                                                                                             | 500GB SSD                                                                                   | 300GB SSD (gp3)                                                                             |
| **프로세서**   | Intel(R) Xeon(R) CPU @ 2.20GHz                                                                  | 2nd Gen Intel Xeon Scalable (Cascade Lake)                                                  | 4세대 Intel Xeon Scalable (Ice Lake)                                                       |
> [!IMPORTANT]
> 영상 생성을 위해서는 최소 24GB VRAM의 GPU를 사용하는 것이 안정적입니다


## Multi-Server Deployment of ComfyUI and Gradio
Stable Diffusion을 기반으로 한 ComfyUI와 Gradio를 활용하여 멀티 서버 환경에서 영상 생성 시스템을 구축 했습니다. 서버간 통신은 SSH로 연결해 통해 연결되며, 이를 통해 안전하고 신뢰할 수 있는 데이터 교환이 가능하도록 설정하였습니다. 
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Architecture.png" alt="Architecture" width="500">  

**시스템 아키텍처** 
세 가지 주요 서버로 구성되어 있습니다
  1. GPU Server 1: 주 연산 서버
  2. EC2 GPU: AWS 클라우드 기반 고성능 GPU 서버
  3. 배포 서버: 사용자 인터페이스 및 서비스 관리
각 서버의 상세 스펙은 위의 표를 참조하시기 바랍니다.



<p align="right">(<a href="#readme-top">back to top</a>)</p>


