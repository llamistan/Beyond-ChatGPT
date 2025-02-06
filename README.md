# 🤖 Beyond ChatGPT: Building Your First LLM App

This is an updated implementation of the LLM application from AI Makerspace's "[Beyond ChatGPT: Build Your First LLM Application](https://www.youtube.com/watch?v=pRbbZcL0NMI)" video tutorial. This repo maintains a modified working version of the [original Beyond ChatGPT repo](https://github.com/AI-Maker-Space/Beyond-ChatGPT) for running the application locally.

## 🖥️ Environment Setup

1. Clone [this](https://github.com/llamistan/Beyond-ChatGPT/tree/main) repo.

     ``` bash
     git clone https://github.com/llamistan/Beyond-ChatGPT.git
     ```

1. Navigate inside this repo
     ``` bash
     cd Beyond-ChatGPT
     ```

1. Create a new Python virtual environment.
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
     
1. Install the packages required for this python envirnoment in `requirements.txt`.
     ``` bash
     pip install -r requirements.txt
     ``` 

1. Add a `.env` file by copying the `.env.sample` file. Replace the `YOUR_KEY_HERE` in your `.env` file with your OpenAI Key and save the file.
     ``` bash
     OPENAI_API_KEY=sk-proj-1ka3d...
     ```


## 🚀 Running the Chatbot

1. Run the Chainlit app.
     ``` bash
     chainlit run app.py -w
     ```
1. The app should open in your browser at `http://localhost:8000`.

## ✨ Customizing the Chatbot
You can influence the chatbot's behavior by modifying the system prompt, the user prompt template, the AI model, and the temperature.

### Modify the System Prompt
Change the system_template to adjust the chatbot’s personality. For example:

```python
system_template = """You are a fun assistant who loves jokes!
"""

user_template = """{input}
Make your response short and concise."""
```

### Change the AI Model
Switch between different models (e.g., gpt-4o) in settings:

```python
"model": "gpt-4o",
```

### Adjust Response Style
Modify temperature for more or less randomness:

* Lower values (e.g., 0.2) → More predictable responses.
* Higher values (e.g., 0.8) → More creative responses.
