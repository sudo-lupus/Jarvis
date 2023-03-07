#!/usr/bin/env python3

import openai
import config           # Supply your own API Key
import markdown_editor
import datetime

messages = [{"role": "system", "content" : f"You are a helpful assistant. Your answers are elaborated. The user's name is '{config.user_name}'"}]

def request(prompt, model = "gpt-3.5-turbo", api_key = config.api_key, markdown = True):
    global messages
    if markdown == True:
        prompt += "Structure your answer and output it in a markdown format."
    messages.append({"role": "user", "content": prompt})
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
      model= model,
      messages = messages,
    )
    message = str.strip(completion["choices"][0]["message"]["content"])
    tokens_used = completion["usage"]["total_tokens"]
    return {"response" : message, "tokens" : tokens_used}

chat_log = []
counter = 1

file_path = markdown_editor.create_initial_md_file(overwrite=True)
markdown_editor.write_to_md_file(f"\n# Session of {datetime.datetime.now()}\n  ", file_path= file_path)

while(True):
    prompt = input("What would you like to ask ChatGPT?\nEnter 'Q' to exit\nYou: ")
    if(prompt in ["Q", "q"]):
        print("You have exited the chat")
        break
    response = request(prompt)
    message = response["response"]
    token_usage = response["tokens"]
    print(f"Current file path = {file_path}")
    print(f"\nChatGPT: {message}\n")
    if prompt == "continue":
        markdown_editor.write_to_md_file(f'''\n{message}''', file_path = file_path)
    else:
        markdown_editor.write_to_md_file(f'''  \n### {counter}. Question:  \n*{prompt}*  \n{message}''', file_path = file_path)
        counter += 1
    print(token_usage)