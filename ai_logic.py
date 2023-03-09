import ast
import os
import openai
from glob import glob
import pandas as pd

openai.api_key = os.environ["OPENAI_API_KEY"]


def _words(history):
    return len(str(history).split(" "))


def generate_plan(code):
    system_message = "You are a helpful assistant for software engineers. Your most important job is to help avoid bugs in the production deployment."

    history = [
        {"role": "system", "content": system_message},
        {
            "role": "user",
            "content": f"generate a test plan for the following code: {code}",
        },
    ]

    print(
        f"Before plan, have {len(history)} messages in history | {_words(history)} words"
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", temperature=1, messages=history
    )
    history.append(
        {"role": "assistant", "content": chat["choices"][0]["message"]["content"]}
    )
    history.append(
        {
            "role": "user",
            "content": "write a typescript playwright file to execute the test plan. use localhost as the host for the server. provide instructions for how to execute the test file.",
        }
    )

    print(
        f"After plan, have {len(history)} messages in history | {_words(history)} words"
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", temperature=0, messages=history
    )

    return chat["choices"][0]["message"]["content"]
