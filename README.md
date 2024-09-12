# Schizo-Bots

This web app pushes the limits of LM Studio's API, employing creative workarounds to achieve a functional chat simulation between two bots. Expect bugs since it's still under development. 

## Installation
1. Clone or download the repository.
2. Install requirements `pip install -r requirements.txt`

## Usage
1. Start LM Studio and navigate to the developer section
2. Select a model of your choice (ex. gemma-2-9b-it-q4_k_m)
3. Start a server. Your sever must look like this `http://127.0.0.1:1234`
4. run the app `run.bat`
5. Navigate to `http://127.0.0.1:8000/` in your web browser 
6. Enjoy watching two bots have a schizo chat

## Customization 
Currently you can change `config.ini` to customize the name of the bots, thier personality, and sampler parameters. 
