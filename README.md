# Text Completion GUI Application

A simple GUI application that allows users to interact with OpenAI's GPT-3.5-turbo model through a user-friendly interface.

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key:
   - Create an account at [OpenAI](https://platform.openai.com/) if you don't have one
   - Generate an API key from your OpenAI dashboard
   - Open the `.env` file and replace `your_api_key_here` with your actual OpenAI API key (ex: OPENAI_API_KEY=xyz123)

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Type your prompt in the input text box
2. Click the "Submit" button
3. The completion result will appear in the output text box below

## Features

- Clean and intuitive GUI interface
- Scrollable input and output text areas
- Error handling for API calls
- Secure API key storage using environment variables