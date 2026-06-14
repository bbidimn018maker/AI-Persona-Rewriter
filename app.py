import streamlit as st
import google.generativeai as genai
import os


api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


model = genai.GenerativeModel("models/gemini-3.5-flash")


st.title("💬 말투 변환기")

# 사용자 입력
persona_name = st.text_input("따라 할 인물을 적어주세요:", " ")
user_text = st.text_area("변환할 문장을 입력하세요:", height=150)

if st.button("✨ 변환하기"):
    if not user_text.strip():
        st.warning("문장을 입력해주세요!")
    else:
        with st.spinner(f"{persona_name}의 말투로 변환 중..."):
            # 프롬프트 구성
            prompt = f"당신은 지금부터 '{persona_name}'입니다. 다음 문장을 '{persona_name}'의 말투, 성격, 화법을 그대로 살려 다시 써주세요. 문장: {user_text}"

            # Gemini 모델 호출
            response = model.generate_content(prompt)

            st.markdown("### 📝 변환 결과:")
            st.write(response.text)
