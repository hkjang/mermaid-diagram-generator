import configparser
import time
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import re
import os
from dotenv import load_dotenv

# 환경 설정 로드
# .env 파일 로드
load_dotenv()

# 환경 변수 값 사용
model_name = os.getenv('OLLAMA_MODEL_NAME')
base_url = os.getenv('OLLAMA_BASE_URL')
mermaid_prompt = os.getenv('MERMAID_PROMPT')

# 환경 변수에서 Flask 서버 설정 값 읽기
host = os.getenv("FLASK_HOST", "0.0.0.0")  # 기본값은 "0.0.0.0"
port = int(os.getenv("FLASK_PORT", 5000))  # 기본값은 5000
debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"  # 기본값은 False

print(model_name)  # gemma3
print(base_url)    # http://172.17.0.1:11434

# Flask 앱 생성 및 CORS 활성화
app = Flask(__name__, static_folder="templates")
CORS(app)  # CORS를 모든 경로에 대해 활성화

# LangChain 및 Ollama 설정
llm = ChatOllama(
    model=model_name,
    base_url=base_url
)

# 프롬프트 템플릿 정의
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=mermaid_prompt
)

# 다이어그램 생성 체인 정의
diagram_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="mermaid_diagram")

# Mermaid 다이어그램 생성 함수
def generate_mermaid_diagram(question):
    try:
        diagram_output = diagram_chain.invoke({"question": question})
        mermaid_code = diagram_output["mermaid_diagram"]
        return {"success": True, "mermaid": mermaid_code}
    except Exception as e:
        return {"success": False, "error": str(e)}

# HTML 페이지 제공
@app.route("/")
def serve_index():
    return send_from_directory("templates", "index.html")

# Mermaid 다이어그램 API
@app.route("/diagram", methods=["GET"])
def diagram():
    question = request.args.get("question")
    if not question:
        return jsonify({"success": False, "error": "❌ 'question' 쿼리 매개변수가 필요합니다."}), 400

    # Mermaid 코드 생성
    mermaid_code = generate_mermaid_diagram(question)

    if mermaid_code.get("success"):
        # Mermaid 코드를 ```mermaid로 바인딩하여 반환
        # "mermaid": f"```mermaid\n{mermaid_code['mermaid']}\n```"
        # "mermaid": f"{mermaid_code['mermaid']}"
        # print(re.search(r'```(.*?)```', mermaid_code['mermaid'], re.DOTALL))
        match = re.search(r'```(.*?)```', mermaid_code['mermaid'], re.DOTALL)

        if match:
            # 추출된 결과를 문자열로 변환
            mermaid_code['mermaid'] = match.group(1)
            mermaid_code['mermaid'] = mermaid_code['mermaid'].replace('mermaid', '').replace('(', "'").replace(')', "'")

            print(mermaid_code['mermaid'])
        return jsonify({
            "success": True,
            "mermaid": mermaid_code['mermaid']
        })
    else:
        return jsonify({"success": False, "error": "❌ 다이어그램 생성에 실패했습니다."}), 500

# Flask 서버 실행
if __name__ == "__main__":
    app.run(
        host=host,
        port=port,
        debug=debug
    )
