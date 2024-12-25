import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as gen_ai

# Load the environment variable from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the API key
gen_ai.configure(api_key=GOOGLE_API_KEY)

# Add custom CSS to set the background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://github.com/Nevetha2206/Image/blob/main/one%20p.jpg?raw=true');  /* One Piece image */
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        color: white; /* Adjust the text color to be visible on the background */
    }
    .stButton>button {
        background-color: #FF5733; /* Customize button color */
        color: white;
    }
    .stTextInput>div>input {
        background-color: rgba(0, 0, 0, 0.5); /* Transparent background for input */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI
st.title("Raghu's AI ")

# Text input for user prompt
prompt = st.text_input("Enter your prompt:")

# Submit button
if st.button("Get Response"):
    if prompt.strip():  # Check if the user input is not empty
        try:
            # Initialize the model (Gemini Pro model)
            model = gen_ai.GenerativeModel("models/gemini-pro")  # Correct model identifier for Gemini Pro

            # Generate content using the model
            response = model.generate_content(prompt)

            # Display the response
            st.write("**Response from Raghu:**")
            st.write(response.text)  # Assuming response.text holds the generated content
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")

