# [B-05] AI Local Worker (Python) Init & Run Guide

이 문서는 무거운 AI 추론(Inference) 작업을 클라우드 환경에서 분리하여, **사용자 소유의 로컬 PC GPU**를 통해 무료로, 무제한 실행하기 위한 **하이브리드(Hybrid) 아키텍처** 워커의 세팅 및 실행 가이드입니다.

## 1. 아키텍처 사상 (Why Local?)
- 클라우드 환경(AWS EC2, GPU 지원)에서 딥러닝 모델(SadTalker 등)을 상시 구동하면 월별 유지 비용이 막대합니다.
- 우리는 이를 해결하기 위해 웹 제어 서버(Next.js, Firebase)와 **비동기 작업 큐(Job Queue) 방식**을 채택했습니다.
- 웹상에서 텍스트 수집 및 거대언어모델(LLM, Gemini)까지 구동을 완료한 후, 무거운 단순 노동(`TTS`, `아바타 렌더링`)만을 로컬 PC의 RTX 4060과 같은 GPU 인스턴스에 위임합니다.

## 2. 권장 기술 스택 (Tech Stack)
- **Language**: Python 3.11+
- **Database/Queue**: Firebase Admin SDK (`firestore`, `storage`)
- **TTS Generator**: `edge-tts` (무료, 인터넷 스트리밍 방식)
- **Lip-Sync Avatar**: `SadTalker` (PyTorch, CUDA 가속 필요)

---

## 3. 프로젝트 초기 세팅 (Installation)

### 3.1 Python 설치 및 폴더 생성
Global 환경의 어지러움을 피하기 위해 철저한 `venv` (가상환경) 사용을 원칙으로 합니다.
```bat
# 1. 원하는 워커 디렉토리 생성 및 진입
mkdir AI-Local-Worker && cd AI-Local-Worker

# 2. 메인 워커 가상환경 생성 및 진입
python -m venv venv
call venv\Scripts\activate.bat

# 3. 필수 패키지 설치
pip install firebase-admin edge-tts moviepy python-dotenv
```

### 3.2 딥러닝 서브 모듈(SadTalker) 연동 주의사항
메인 워커 스크립트(`main.py`)가 구동되는 가상환경에 *절대* PyTorch 등 무거운 라이브러리를 섞지 마십시오.
딥러닝 모델은 **서브 디렉토리에 별도의 가상환경을 파고**, 이를 메인 파이썬 스크립트 내에서 `subprocess` 모듈로 호출(Invoke)하는 형태를 지향합니다.

```python
# 올바른 호출 패턴 예시 (avatar_generator.py)
import subprocess

def run_sadtalker_inference():
    # 서브 모듈의 독립된 가상환경 내 python.exe 경로 지정
    python_exe = "SadTalker/venv/Scripts/python.exe"
    script_path = "SadTalker/inference.py"
    
    subprocess.run([python_exe, script_path, "--driven_audio", "audio.mp3", ...])
```

---

## 4. 실행 방법 (Run)

### 4.1 Firebase SDK 권한 키 삽입
워커 폴더 최상단에 `serviceAccountKey.json` 이라는 이름으로 Firebase 비공개 키를 배치해야 합니다.

### 4.2 데몬 주기능 실행
```bat
cd AI-Local-Worker
call venv\Scripts\activate.bat
python main.py
```
*(성공 시 콘솔에 `🚀 AI Local Worker Started (Listening to Firebase...)`라는 메시지와 함께, 10초마다 작업을 폴링하는 마침표(`.`)가 찍히게 됩니다.)*

---

## 5. 트러블슈팅 (Troubleshooting)

- **Q. SadTalker 설치 중 `ERROR: Could not build wheels for dlib`가 뜹니다.**
  - **A.** Windows 환경에서의 C++ 컴파일러 부재 이슈입니다. `pip install dlib-bin` 이라는 빌드된 바이너리를 다운로드함으로써 우회하십시오.
- **Q. CUDA가 잡히지 않고 CPU로 연산하여 속도가 너무 느립니다.**
  - **A.** `nvcc --version` 명령어로 본인 PC의 쿠다 버전을 확인한 뒤 대응하는 PyTorch 버전을 설치해야 합니다. (예: 최신 RTX 계열은 `--index-url https://download.pytorch.org/whl/cu121` 옵션을 붙여 설치)
