# Schizo-Bots [![Download](https://img.shields.io/badge/Download-Schizo--Bots-brightgreen)](https://github.com/Melyns/Schizo-Bots/archive/refs/heads/main.zip)

Simple web app that pushes the limits of LM Studio's API, using creative workarounds to create an autonomous chat simulation between two bots. Expect bugs as it is still under development.

![image](https://github.com/user-attachments/assets/70b5f9f0-7fee-4c02-98f4-436e3e2ae265)

## Requirements
Python and LM Studio

## Installation
1. Clone or download the repository.
```bash
git clone https://github.com/Melyns/Schizo-Bots/
```
2. Install requirements
```bash
pip install -r requirements.txt
```

## Usage
1. Start LM Studio and navigate to the developer section
2. Select an LLM of your choice (ex. gemma-2-9b)
3. Start an LM Studio server. Your sever address must be `http://127.0.0.1:1234`
4. run the app `run.bat`
5. Navigate to `http://127.0.0.1:8000/` in your web browser 
6. Enjoy watching two bots have a schizo chat

> [!IMPORTANT]
> You must always have **only one instance** of Schizo Bots open in your browser at `http://127.0.0.1:8000/` otherwise the chat will get broken!
> If your chat seems off, then you likley have another tab of Schizo Bots open.

> [!TIP]
> Google's Gemma 2 models work really well for this. I recommend using [this model.](https://huggingface.co/bartowski/Gemma-2-Ataraxy-9B-GGUF)

## Customization 
You can edit `config.ini` to customize the name of the bots, thier personality, sampler parameters, and the API address. 

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.
