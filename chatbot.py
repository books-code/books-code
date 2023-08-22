# CODE START 
import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Streamlit app title and description
st.title("Chatbot with GPT-3")
st.write("Type your message below and the chatbot will respond.")

# User input text box
user_input = st.text_input("You:", "")

# Generate response from GPT-3
if user_input:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50  # Limit response length for a concise answer
    )
    bot_response = response.choices[0].text.strip()
    st.text("Bot:", bot_response)
#CODE END 







