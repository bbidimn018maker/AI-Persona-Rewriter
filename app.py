import streamlit as st
import google.generativeai as genai
import os

# 1. 모델을 한 번만 불러오도록 캐싱 처리
@st.cache_resource
def get_model():
    api_key = os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    # 캐시를 통해 모델을 메모리에 고정시킴
    return genai.GenerativeModel("models/gemini-3.5-flash")

model = get_model()

st.title("💬 말투 변환기")

# 사용자 입력
persona_name = st.text_input("따라 할 인물을 적어주세요:", " ")
user_text = st.text_area("변환할 문장을 입력하세요:", height=150)

if st.button("✨ 변환하기"):
    if not user_text.strip():
        st.warning("문장을 입력해주세요!")
    else:
        # 아까 배운 spinner로 사용자 경험 개선
        with st.spinner(f"{persona_name}의 말투로 변환 중..."):
            prompt = f"당신은 지금부터 '{persona_name}'입니다. 다음 문장을 '{persona_name}'의 말투, 성격, 화법을 그대로 살려 다시 써주세요. 문장: {user_text}"
            
            response = model.generate_content(prompt)
            
            st.markdown("### 📝 변환 결과:")
            st.write(response.text)

            
