import openai
import config       # Supply your own API Key
import markdown
import datetime

messages = []

def request(prompt, model = "gpt-3.5-turbo", api_key = config.api_key):
    global messages
    messages.append({"role": "user", "content": prompt})
    prompt += "\nFormulate your whole answer in Markdown Format"
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
      model= model,
      messages = messages
    )
    message = str.strip(completion["choices"][0]["message"]["content"])
    return message

counter = 0
chat_log = []
file_path = ""

file_path = markdown.create_initial_md_file(overwrite=True)
markdown.write_to_md_file(f"\n# Session of {datetime.datetime.now()}\n  ", file_path= file_path)

while(True):
    prompt = input("What would you like to ask ChatGPT?\nEnter 'Q' to exit\nYou: ")
    if(prompt in ["Q", "q"]):
        print("You have exited the chat")
        break
    message = request(prompt)
    print(f"Current file path = {file_path}")
    print(f"\nChatGPT: {message}\n")
    if prompt == "continue":
        markdown.write_to_md_file(f'''\n{message}''', file_path = file_path)
    markdown.write_to_md_file(f'''  \n### Question: {prompt}\n### Answer:\n{message}''', file_path = file_path)