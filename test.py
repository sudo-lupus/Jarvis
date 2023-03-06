import openai
import config
import markdown
import datetime

def request(prompt, model = "gpt-3.5-turbo", api_key = config.api_key):
    prompt += "\nFormulate your whole answer in Markdown Format"
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
      model= model, 
      messages=[{"role": "user", "content": prompt}]
    )
    message = str.strip(completion["choices"][0]["message"]["content"])
    return message

counter = 0
chat_log = []
file_path = ""

markdown.write_to_md_file(f"\# Session of {datetime.datetime.now()}\n  ", file_path= file_path)

while(True):
    prompt = input("What would you like to ask ChatGPT?\nEnter 'Q' to exit\nYou: ")
    if(prompt in ["Q", "q"]):
        print("You have exited the chat")
        break
    if(prompt == "n"):
        file_path = markdown.create_initial_md_file(overwrite=True)
        continue
    message = request(prompt)
    print(f"Current file path = {file_path}")

    print(f"\nChatGPT: {message}\n")
    markdown.write_to_md_file(f'''  \n### Question: {prompt}\n### Answer:\n{message}''', file_path = file_path)

for i, msg in enumerate(chat_log):
    markdown.write_to_md_file(f'''### {i + 1} Question: {msg[0]}  \n### Answer: \n{msg[1]}''', file_path= file_path)
