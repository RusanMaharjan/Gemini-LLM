import streamlit as st
from model import prompt_llm

st.header("Gemini 3 LLM")
st.subheader("Generate content with Gemini 3")

user_input = st.text_area(
    "Enter your question?",
    placeholder="Ask me anything..."
)

if st.button("Ask LLM"):
    if user_input.strip() == "":
        st.error("Please enter valid prompt!!!")
    else:
        with st.spinner("Generating response..."):
            answer = prompt_llm(user_input)
        
        st.success("Generated Response!!")
        st.write(answer)