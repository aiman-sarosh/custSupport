# Customer Support Chatbot

This is an enterprise-level customer support chatbot application built using Streamlit and the Groq API. The application provides a conversational interface for handling customer support queries with empathetic and helpful responses.

## Features

- Conversational AI powered by Groq's Llama model
- Persistent chat history during the session
- Error handling for API communication issues
- Clean, user-friendly Streamlit interface

## Project Structure

- `main.py`: Contains the core business logic for the chatbot, including API integration and response generation
- `streamlit.py`: The Streamlit application that provides the web interface
- `requirements.txt`: Lists all Python dependencies required to run the application
- `.env`: Environment variables file (not committed to version control)
- `README.md`: This documentation file

## Setup Instructions

1. **Clone or download the project files** to your local machine.

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Obtain a Groq API key from [Groq Console](https://console.groq.com/)
   - Create a `.env` file in the project root and add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```
   - Alternatively, set the environment variable directly:
     - On Windows: `set GROQ_API_KEY=your_api_key_here`
     - On Linux/Mac: `export GROQ_API_KEY=your_api_key_here`

4. **Run the application**:
   ```
   streamlit run streamlit.py
   ```

5. **Access the app**:
   - Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

## Usage

- Enter your customer support query in the chat input box
- The AI assistant will provide helpful and empathetic responses
- Chat history is maintained throughout the session

## Security Note

Ensure your Groq API key is kept secure and not committed to version control. Use environment variables or secure configuration management for production deployments.

## Contributing

For enterprise-level contributions, please follow standard coding practices and ensure all changes are tested.
