import openai
import streamlit as st
import streamlit as st
import pandas as pd
import openai


# Set up OpenAI API
# Authenticate with OpenAI API
openai.api_type = "azure"
openai.api_base = 'https://testgpt9212.openai.azure.com/'
openai.api_version = "2023-03-15-preview"
openai.api_key = '6034a67ccf3e4dda98be0b6f4b95835d'
#openai.api_key = st.secrets['path']
#model_engine = "text-davinci-003"

import openai
import streamlit as st



# Available GPT-3 models
gpt3_models = [
    "text-davinci-003",
    "text-davinci-002",
    "gpt-35-turbo"
]

def generate_questions(subject, num_questions, temperature, max_tokens, model_engine, question_level):
    prompt = f"Generate {num_questions} {question_level} level questions on {subject}\n"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    if response.choices[0].text:
        result = response.choices[0].text.strip().split("\n")
        questions = [q for q in result if "?" in q]
        return questions
    else:
        return None

def main():
    st.title("Question Generator")
    subject = st.text_input("Enter a subject:")
    num_questions = st.slider("Number of questions to generate", 1, 20, 10)
    temperature = st.slider("Temperature", 0.1, 1.0, 0.5)
    max_tokens = st.slider("Max Tokens", 0, 8000, 100)
    question_level = st.selectbox("Select question level", ["Basic", "Medium", "Advanced"])
    question_level = question_level.lower()
    model_engine = st.selectbox("Select GPT model", gpt3_models)

    if st.button("Generate"):
        questions = generate_questions(subject, num_questions, temperature, max_tokens, model_engine, question_level)
        if questions:
            st.write("Generated Questions:")
            for q in questions:
                st.write(f"Q: {q}")
        else:
            st.write("No questions were generated.")

if __name__ == "__main__":
    main()
