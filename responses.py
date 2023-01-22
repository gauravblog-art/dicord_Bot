import random

# def handle_respose(message):
#     p_message=message.lower()

#     if p_message=="hello":

#         return "Hey there!"
#     if p_message=="roll":

#         return str(random.randint(1,6))
#     if   p_message=='!help':

#         return "This is help message that you can modify"
#     if "name" in p_message:
#         return "My name is Bot"
#     if "where are you from" in p_message:
#         return " I am from internet"
#     return " I dont understand this message!"

import openai

def handle_respose(message):
  openai.api_key ="your_api"
  # ask=input("Enter the Question: ")
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )

  text=response['choices'][0]["text"]
  return text

