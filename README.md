# Mermaid Diagram Generator using Flask and LangChain

이 프로젝트는 `Flask` 웹 애플리케이션을 통해 사용자가 입력한 질문에 대해 Mermaid 다이어그램을 생성하는 API를 제공합니다. `LangChain`과 `Ollama` 모델을 활용하여 다이어그램을 생성하며, `.env` 파일을 통해 환경 설정을 관리합니다.

## 기술 스택

- **Flask**: 웹 애플리케이션 프레임워크
- **LangChain**: 자연어 처리 및 언어 모델 체인 라이브러리
- **Ollama**: 모델 인터페이스로 사용
- **Mermaid**: 다이어그램 생성 언어
- **dotenv**: 환경 변수 관리
- **CORS**: Cross-Origin Resource Sharing 활성화

## 기능

1. **Mermaid 다이어그램 생성**: 사용자로부터 받은 질문을 기반으로 Mermaid 다이어그램 코드를 생성.
2. **REST API**: `GET /diagram` 엔드포인트를 통해 질문을 전달하고, Mermaid 다이어그램을 반환.
3. **Flask 서버**: 환경 설정에 따라 Flask 서버가 실행됩니다.

## 설치 및 실행

### 1. 클론

먼저, 해당 레포지토리를 클론합니다:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. 가상 환경 설정 (권장)

가상 환경을 생성하고 활성화합니다:

```bash
python -m venv venv
source venv/bin/activate  # Windows에서는 venv\Scripts\activate
```

### 3. 의존성 설치

필요한 Python 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

### 4. 환경 설정

`.env` 파일을 프로젝트 루트 디렉토리에 생성하고, 아래와 같은 설정을 추가합니다:

```ini
OLLAMA_MODEL_NAME=gemma3
OLLAMA_BASE_URL=http://172.17.0.1:11434
MERMAID_PROMPT=Mermaid 다이어그램 생성을 위한 프롬프트 예시
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
```

### 5. 서버 실행

서버를 실행하려면 다음 명령어를 입력합니다:

```bash
python app.py
```

서버가 실행되면 `http://localhost:5000`에서 애플리케이션을 확인할 수 있습니다.

## API 엔드포인트

### `GET /diagram`

질문을 파라미터로 받아 Mermaid 다이어그램을 생성하고 반환하는 API 엔드포인트입니다.

#### 요청 예시

```bash
GET http://localhost:5000/diagram?question=소프트웨어 개발 프로세스
```

#### 응답 예시

```json
{
  "success": true,
  "mermaid": "graph TD; A[소프트웨어 요구 사항] --> B[설계]; B --> C[구현]; C --> D[테스트]; D --> E[배포];"
}
```

## 개발 및 기여

이 프로젝트는 오픈 소스 프로젝트입니다. 기여를 원하시면, 다음 단계를 따르세요:

1. Fork 저장소
2. 새 브랜치를 생성하고, 기능을 추가합니다.
3. Pull Request를 제출하여 변경 사항을 제안합니다.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
