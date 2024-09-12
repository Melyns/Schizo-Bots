# Schizo-Bots

This web app pushes the limits of LM Studio's API, using creative workarounds to create an autonomous chat simulation between two bots. Expect bugs as it is still under development.

![image](https://github.com/user-attachments/assets/70b5f9f0-7fee-4c02-98f4-436e3e2ae265)

## Requirements
Python and LM Studio

## Installation
1. Clone or the repository. [![Download](https://img.shields.io/badge/Download-Schizo--Bots-brightgreen)](https://github.com/Melyns/Schizo-Bots/archive/refs/heads/main.zip)
```bash
git clone https://github.com/Melyns/Schizo-Bots/
```
3. Install requirements
```bash
pip install -r requirements.txt
```

## Usage
1. Start LM Studio and navigate to the developer section
2. Select an LLM of your choice (ex. gemma-2-9b)
3. Start a LM Studio server. Your sever address must be `http://127.0.0.1:1234`
4. run the app `run.bat`
5. Navigate to `http://127.0.0.1:8000/` in your web browser 
6. Enjoy watching two bots have a schizo chat
> [!IMPORTANT]
> You must *always* keep one browser window open at `http://127.0.0.1:8000/` otherwise the chat will get messed up!

## Customization 
You can change `config.ini` to customize the name of the bots, thier personality, sampler parameters, and the API address. 

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.
