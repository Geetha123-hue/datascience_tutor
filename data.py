import streamlit as st
import google.generativeai as ai
import os

# Set up API key
API_KEY = "YOUR API KEY"
os.environ["GOOGLE_API_KEY"] = API_KEY
ai.configure(api_key=API_KEY)

# System prompt for the AI model
sys_prompt = """You are a helpful AI Tutor for Data Science. 
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible. 
Make sure to take examples while explaining a concept.
If a student asks any question outside the data science scope, 
politely decline and tell them to ask a question from the data science domain only."""

# Initialize the AI model
model = ai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt)

# Streamlit UI
st.title("🧠 Data Science Tutor")

st.write("Ask any question related to Data Science, and I'll do my best to help you! 😊")

user_prompt = st.text_area("Enter your query:", placeholder="Type your data science-related question here...")

if st.button("Generate Answer"):
    if user_prompt.strip():
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(user_prompt)
                answer = response.candidates[0].content.parts[0].text  # Extracting text from the response
                st.markdown(f"### 🤖 AI Tutor's Response:\n\n{answer}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid query before clicking the button.")

# Optional: Add a sidebar for extra features
st.sidebar.header("About This App")
st.sidebar.write("This AI-powered tutor helps you learn Data Science concepts with detailed explanations and examples.")

