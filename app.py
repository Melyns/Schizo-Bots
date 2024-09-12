from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import json
import requests
import configparser
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'config.ini'))

API_URL = config['api']['url']
MODEL = config['model']['name']
TEMPERATURE = float(config['conversation']['temperature'])
MAX_TOKENS = int(config['conversation']['max_tokens']) if config['conversation']['max_tokens'].isdigit() else None
STREAM = config.getboolean('conversation', 'stream')
WPM = int(config['conversation']['wpm'])
BOT1_NAME = config['personalities']['bot1_name']
BOT2_NAME = config['personalities']['bot2_name']

INITIAL_MESSAGES = [
    {"role": config['initial_messages']['message1_role'],
     "content": config['initial_messages']['message1_content'].format(bot1_name=BOT1_NAME)},
    {"role": config['initial_messages']['message2_role'],
     "content": config['initial_messages']['message2_content'].format(bot2_name=BOT2_NAME)}
]

message_history = INITIAL_MESSAGES
current_personality = BOT1_NAME
paused = False

def chat_with_bot(messages):
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS if MAX_TOKENS > 0 else 1,
        "stream": STREAM,
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "content": {"type": "string"}
                    },
                    "required": ["content"]
                }
            }
        }
    }

    try:
        response = requests.post(API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()

        if "choices" in response_json and len(response_json["choices"]) > 0:
            choice = response_json["choices"][0]
            message = choice.get("message", {})
            content = message.get("content", "")
            if content:
                try:
                    content_json = json.loads(content)
                    result = content_json.get("content", "Empty content received from API.")
                    print(f"API Response: {result}")
                    return result
                except json.JSONDecodeError:
                    print("Error decoding JSON.")
                    return "Error decoding JSON."
            else:
                print("Empty content received from API.")
                return "Empty content received from API."
        else:
            print("No choices found in response.")
            return "No choices found in response."
    except requests.RequestException as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/events")
async def events():
    async def event_generator():
        global message_history, current_personality, paused
        while True:
            if not paused:
                user_message = f"Message from {current_personality}."
                message_history.append({"role": "user", "content": user_message, "sender": current_personality})

                response = chat_with_bot(message_history)
                response_html = response.replace("\n", "<br>")

                message_history.append({"role": "assistant", "content": response, "sender": current_personality})

                current_personality = BOT2_NAME if current_personality == BOT1_NAME else BOT1_NAME

                num_words = len(response.split())
                delay = num_words / WPM * 60

                yield f"data: {response_html}\n\n"
                await asyncio.sleep(delay)
            else:
                await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type='text/event-stream')

@app.post("/pause")
async def pause():
    global paused
    paused = not paused
    return {"paused": paused}
