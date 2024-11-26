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
  - [Model Configuration](#Model-Configuration)
  - [Getting Started](#getting-started)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)

<!-- ABOUT THE PROJECT -->
## About The Project
---
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
<b>Task1 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_IDPhoto.png" alt="Task1 IDPhoto" width="500">
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task1_Out.png" alt="Task1 Out" width="300">
<b>Task2 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task2_ImageTransfer.png" alt="Task2 ImageTransfer" width="500">
<b>Task2 Output</b> 
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task2_Out.png" alt="Task2 Out" width="300">
<b>Task3 Workflow</b>  
<img src="https://raw.githubusercontent.com/rahoney/ConnectDream/main/workfiles/Task3_Videowork.png" alt="Task3 Videowork" width="500">
<b>Task3 Output</b>  
  
https://github.com/user-attachments/assets/cc32dee4-4617-4134-b5a1-014c5d38279f  



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


