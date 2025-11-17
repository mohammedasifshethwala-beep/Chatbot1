import streamlit as st
import openai
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="NCERT & CBSE Tutor Bot",
    page_icon="📚",
    layout="wide"
)

# Title and description
st.title("📚 NCERT & CBSE Student Problem Solving Tutor")
st.markdown("Ask me any questions related to NCERT textbooks, CBSE syllabus, or academic problems!")

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Settings")

    # API Key input
    api_key = st.text_input(
        "Enter your OpenAI API Key:",
        type="password",
        help="Get your API key from platform.openai.com"
    )

    # Subject selection
    subject = st.selectbox(
        "Select Subject:",
        ["General", "Mathematics", "Physics", "Chemistry", "Biology", "English", "Social Science"]
    )

    # Class selection
    grade = st.selectbox(
        "Select Class:",
        ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
    )

    st.markdown("---")
    st.markdown("### About")
    st.info("This AI tutor helps NCERT and CBSE students with their academic queries.")

    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Set OpenAI API key
if api_key:
    openai.api_key = api_key
else:
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial system message
    system_message = {
        "role": "system",
        "content": f"""You are an expert NCERT and CBSE tutor. You specialize in helping students understand concepts, solve problems, and prepare for exams.
        Current Subject: {subject}
        Current Grade: {grade}

        Guidelines:
        - Provide clear, step-by-step explanations
        - Use simple language appropriate for the student's grade level
        - Include relevant NCERT concepts and formulas
        - Encourage critical thinking
        - Be patient and supportive
        - If a question is outside NCERT/CBSE syllabus, politely mention it but still help
        """
    }
    st.session_state.messages.append(system_message)

    # Add welcome message
    welcome_message = {
        "role": "assistant",
        "content": f"Hello! 👋 I'm your NCERT & CBSE tutor. I'm here to help you with **{subject}** for **{grade}**. Ask me any question related to your studies!"
    }
    st.session_state.messages.append(welcome_message)

# Display chat messages (excluding system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to session state
    user_message = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_message)

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Create messages list for API (including system message)
            api_messages = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in st.session_state.messages
            ]

            # Call OpenAI API with streaming
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=api_messages,
                temperature=0.7,
                max_tokens=1000,
                stream=True
            )

            # Stream the response
            for chunk in response:
                if chunk.choices[0].delta.get("content"):
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

            # Add assistant response to session state
            assistant_message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(assistant_message)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please check your API key and try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <small>Powered by OpenAI GPT-3.5 Turbo | Built with Streamlit</small>
    </div>
    """,
    unsafe_allow_html=True
)
