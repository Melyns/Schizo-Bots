import os
import json
from datetime import datetime

log_directory = 'chat_log'
logged_messages = []

def initialize_log_file():
    global log_filename
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    log_filename = os.path.join(log_directory, f'chat_{timestamp}.txt')
    os.makedirs(log_directory, exist_ok=True)

def write_chat_log(messages):
    global logged_messages

    if not os.path.exists(log_filename):
        initialize_log_file()
    
    with open(log_filename, 'a', encoding='utf-8') as file:
        for message in messages:
            if message not in logged_messages:
                if message['role'] in ['user', 'assistant']:
                    content = message['content']
                    if content and not content.startswith(f"Message from {message['sender']}"):
                        file.write(f"{message['sender']}: {content.strip()}\n\n")
                        logged_messages.append(message)

def reset_log():
    global logged_messages
    logged_messages = []
