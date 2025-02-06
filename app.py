# OpenAI Chat completion
from openai import AsyncOpenAI
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

# ChatOpenAI Templates
system_template = """You are a helpful assistant who always speaks in a pleasant tone!
"""

user_template = """{input}
Think through your response step by step.
"""


@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)
    cl.user_session.set(
        "chat_history", [{"role": "system", "content": system_template}]
    )


@cl.on_message  # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: cl.Message):
    settings = cl.user_session.get("settings")
    chat_history = cl.user_session.get("chat_history")

    client = AsyncOpenAI()

    print(message.content)

    # Create messages directly in OpenAI format
    chat_history.append(
        {"role": "user", "content": user_template.format(input=message.content)},
    )

    print(chat_history)

    msg = cl.Message(content="")

    # Call OpenAI
    async for stream_resp in await client.chat.completions.create(
        messages=chat_history, stream=True, **settings
    ):
        token = stream_resp.choices[0].delta.content
        if token is None:
            token = ""
        await msg.stream_token(token)

    # Store the prompt and completion in message metadata if needed
    msg.metadata = {
        "prompt": {
            "messages": chat_history,
            "settings": settings,
            "completion": msg.content,
        }
    }

    # Send and close the message stream
    await msg.send()
