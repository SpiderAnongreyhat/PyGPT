import time, os
try:
	import openai
except:
	os.system("pip install openai")
import os
import requests
import json
import random
from pyfiglet import Figlet
try:
	from termcolor import colored, cprint
except:
	os.system("pip install termcolor")
from colorama import init
import platform

init()



ass = "\033[1;36;40m 1. Go to >> \033[1;31mhttps://platform.openai.com \033[1;36;40m<< and click on the sign up button. If you already have an account skip this option. I advice you use temp mail to register instead of your actual email.\n"

asd = "\033[1;36;40m 2. After you login/signup go to >> \033[1;31mhttps://platform.openai.com/account/api-keys \033[1;36;40m<< and click on the create new secrete key button, copy your api key, tap on done then paste it below.\n"

# Set up the OpenAI API credentials
os.system("clear")
Keys = 'chatgpt_config'

# create the config directory if it doesn't exist
if not os.path.exists(Keys):
    os.mkdir(Keys)
if not os.path.exists("/sdcard/Text2Image"):
	os.mkdir("/sdcard/Text2Image")

# check if the api key file exists
api_key_file = os.path.join(Keys, 'openai.api_key.txt')
if os.path.exists(api_key_file):
    # read the api key from the file
    with open(api_key_file, 'r') as f:
        openai.api_key = f.readline().strip()
else:
    print(colored("="*59, "green"))
    print(ass)
    print(asd)
    print(colored("="*59, "green"))
    openai.api_key = input("\n Provide your OpenAI API key: ")
    while True:
        if len(openai.api_key) != 51:
            print(colored("\n Oops!!! Invalid API key. Please provide a valid OpenAI API key.", "red"))
            openai.api_key = input("\n Provide your OpenAI API key: ")
        else:
            break

    with open(api_key_file, 'w') as f:
        f.write(openai.api_key)
    for char in "\nAPI key successfully saved.":
        print(colored(char, "green"), end='', flush=True)
        time.sleep(0.05)

time.sleep(1.1)

# Define the main menu function
custom_fig = Figlet(font='graffiti')
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(custom_fig.renderText('   ChatGpt'), color='cyan'))
    print(colored("version 1.1", "yellow").center(110))
      
    authors = "TheNooB | Spider Anongreyhat"
    github = "TheNooB4 | spider863644"
    whatsapp = "+233245222358 | +2349052863644"
    
    print(colored("="*59, "green"))
    print(colored("Authors: ", "white") + colored(authors, "cyan"))
    print(colored("Github: ", "white") + colored(github, "green"))
    print(colored("WhatsApp: ", "white") + colored(whatsapp, "magenta"))
    print(colored("="*59, "green"))
    time.sleep(1)

    print(colored("\n  1. Text To Image", "yellow"))
    print(colored("  2. Chat With AI", "yellow"))
    print(colored("  3. Change Api Key", "yellow"))
    print(colored("  4. Exit", "red"))

    try:
        choice = int(input(colored("\n What would you like to do? ", "cyan")))
        if choice == 1:
            text_to_image()
            input("\n\n Press Enter to continue...")
            main_menu()
        elif choice == 2:
            chat_with_ai()
            input("\n\n Press Enter to continue...")
            main_menu()
        elif choice == 3:
           os.remove("chatgpt_config/openai.api_key.txt")
           os.system("python3 Gpt.py")
           
        elif choice == 4:
           if platform.system() == "Windows":
           	os.system("cls")

           else:
           	os.system("clear")
           print(colored(custom_fig.renderText('ChatGpt'), color='cyan'))
           for letter in list(colored("\n Thank you for using ChatGpt. Goodbye!\n\n", "yellow")):
                print(letter, end='', flush=True)
                time.sleep(0.05)
           time.sleep(1)
           os.system('cls' if os.name == 'nt' else 'clear')
        else:
            raise ValueError()
    except ValueError:
        print(colored("\n Please choose a valid option!", "red"))
        input("\n\n Press Enter to continue...")
        main_menu()

# Define the text to image function
def text_to_image():
    # Prompt user for text input
    os.system("clear")
    print(colored("="*59, "green"))

    print("""\033[36m
      _______        _   ___  _
     |__   __|      | | |__ \(_)
        | | _____  _| |_   ) |_ _ __ ___   __ _
        | |/ _ \ \/ / __| / /| | '_ ` _ \ / _` |
        | |  __/>  <| |_ / /_| | | | | | | (_| |
        |_|\___/_/\_\\__|____|_|_| |_| |_|\__, |
                                           __/ |
                                           |___/
                                      \033[0m""")

    print(colored("="*59, "green"))


    # Prompt user for text input
    text = input("\n \033[1;34mEnter the text to generate an image from: \033[0m")
    # Prompt user for number of images to generate
    num_images = int(input(colored("\n How many images do you want to generate? ", "cyan")))

    if num_images > 0:
        print("\n \033[1;33mMay take a while depending on your network speed so please wait..\n\033[0m")

    for i in range(num_images):
        #Generate a random filename for each image

        filename = f"result_{i+1}_{random.randint(1000,9999)}.jpg"

        # Use API to generate image
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024",
            response_format="url"
        )

        # Get the image url from the response
        image_url = response['data'][0]['url']

        # Download image and save to local storage
        response = requests.get(image_url)
        with open(f"/sdcard/Text2Image/{filename}", 'wb') as f:
            f.write(response.content)

        # Inform user of successful save location
        print(colored("="*59, "green"))
        print(f"\033[1;32mImage {i+1} saved as \033[1;36m{filename}\033[1;32m in \033[1;35ma folder called Text2Image inside your storage\033[1;32m directory.\033[0m")
        print(colored("="*59, "green"))


# Define the chat with AI function
def chat_with_ai():
    # Define the prompt that the chatbot will use to start the conversation
    prompt = "Hello, how can I help you today?"

    # Initialize the conversation history
    conversation_history = ""
    os.system("clear")
    print(colored("="*59, "green"))
    print(colored(custom_fig.renderText('      Ask_AI'), color='cyan'))
    print(colored("\n Start chatting with AI","green"))
    print(colored("\n You can type 'exit', 'quit', or 'bye'\n to end the conversation.","green"))
    print(colored("="*59, "green"))

    # Start the main loop
    while True:
        try:
            # Get the user's input
            user_input = input(colored("\n\n You >>  ", "cyan"))
            if user_input == "":
                raise ValueError()

            # Add the user's input to the conversation history
            conversation_history += f"User: {user_input}\n"

            # Set up the OpenAI API request
            model_engine = "text-davinci-003" # Change this to the appropriate GPT-3 model for your use case
            prompt_with_history = f"{prompt}\n{conversation_history}\nAI:"

            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_history,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
                timeout=10
            )

            # Get the AI's response
            ai_response = response.choices[0].text.strip()
            print(colored("\n AI: ", "green"), end="")
            for char in ai_response:
                typing_speed = 0.05 # Change this value to modify the typing speed
                time.sleep(typing_speed)
                print(char, end="", flush=True)


            # Add the AI's response to the conversation history
            conversation_history += f"AI: {ai_response}\n"

            if user_input.lower() in ["exit", "quit", "bye"]:
                # End the conversation if the user types one of these keywords
                break

        except ValueError:
            print(colored("\n Please enter a valid input!", "red"))

# Call the main menu function on startup
main_menu()