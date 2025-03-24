# 1. Python 3.12 베이스 이미지 사용
FROM python:3.12-slim

# 환경 변수 설정
#ENV OLLAMA_MODEL_NAME="gemma3"
#ENV OLLAMA_BASE_URL="http://host.docker.internal:11434"
#ENV MERMAID_PROMPT="Given the following question, generate a Mermaid.js flowchart. Do not include parentheses `()` in the diagram. Ensure that square brackets `[]` are used correctly and never include parentheses `()` inside them. Please write the diagram content in Korean as much as possible.\nQuestion: {question}"
# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일을 복사
COPY requirements.txt .

# 4. 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 애플리케이션 소스 코드 복사
COPY . .

# 6. Flask 애플리케이션 실행
CMD ["python", "app.py"]