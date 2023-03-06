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

while(True):
    prompt = input("What would you like to ask ChatGPT?\nEnter 'Q' to exit\nYou: ")
    if(prompt in ["Q", "q"]):
        print("You have exited the chat")
        break
    message = request(prompt)

    print(f"\nChatGPT: {message}\n")
    chat_log.append([prompt, message])
    counter += 1

markdown.write_to_md_file(f"\#Session of {datetime.datetime.now()}\n  ")

for i, msg in enumerate(chat_log):
    markdown.write_to_md_file(f'''  \#\#\#{i + 1} Question: {msg[0]}  \n\#Answer: {msg[1]}''')
