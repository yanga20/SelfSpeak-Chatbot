import requests
import asyncio
import edge_tts
import os
from config import PASSWORD

def authenticate():
    password = input("Enter project password: ")

    if password != PASSWORD:
        print("Access denied.")
        exit()

    print("Access granted.\n")
def play_my_voice():
    print("Playing your voice sample...\n")
    os.system("start Myvoice_sample.wav")

async def speak(text):
    communicate = edge_tts.Communicate(
        text,
        voice="en-IN-NeerjaNeural", 
        rate="-10%",                  
        pitch="+2Hz"                  
    )
    await communicate.save("output.mp3")
    os.system("start output.mp3")

def chat_with_ai(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "phi",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    return response.json()['response']

authenticate()
print("SelfSpeak AI Chatbot (type 'exit' to quit)\n")

play_my_voice()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    answer = chat_with_ai(user_input)

    answer = "So, according to me, " + answer

    print("AI:", answer)

    asyncio.run(speak(answer))