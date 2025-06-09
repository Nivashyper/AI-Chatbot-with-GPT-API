# AI Chatbot with GPT API

This project provides a minimal example of building a command-line chatbot that uses OpenAI's GPT API. The bot accepts user input in the terminal and returns responses from the model.

## Setup

1. Create and activate a Python virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your-key-here
```

4. Run the chatbot:

```bash
python main.py
```

Type `exit` or `quit` to stop the conversation.
