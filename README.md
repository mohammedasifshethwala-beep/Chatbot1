# Professional LLM Chatbot

A Streamlit web app powered by OpenAI GPT models for professional, topic-adaptive conversations.  
Supports dynamic chat, session state, and is ready for deployment or sharing.

## Features

- Interactive chat with GPT-3.5 (or other OpenAI models)
- Professional prompt system, adaptable to any topic
- Session state: persistent chat history
- Streamlit web interface
- Easy setup and deployment

## Requirements

- Python 3.10 or newer
- OpenAI API key (get from [platform.openai.com](https://platform.openai.com))
- The following Python packages (see `requirements.txt`):
    - streamlit
    - openai
    - python-dotenv

## How to Run Locally

1. Clone the repository:
    ```
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Start the application:
    ```
    streamlit run app.py
    ```

4. Open your browser to `http://localhost:8501`, enter your OpenAI API key in the sidebar, and start chatting!

## How to Deploy (Optional)

### Using Streamlit Cloud

- Push your files to GitHub.
- Go to [share.streamlit.io](https://share.streamlit.io), log in with GitHub.
- Deploy your repository (choose your `app.py` file).
- Add your OpenAI API key as a secret in `secrets.toml`.

## Troubleshooting

- If you see errors about OpenAI API compatibility, check that your code matches your `openai` library version.  
- See [OpenAI migration guide](https://github.com/openai/openai-python/discussions/742) for updates.
- For issues, downgrade with `pip install "openai<1.0.0"` or update your code for `openai>=1.0.0`.

## License

MIT License (see `LICENSE` file)

---

Enjoy chatting!
