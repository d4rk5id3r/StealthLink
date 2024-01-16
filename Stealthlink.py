
#!/usr/bin/env python3
# Importing necessary modules
from termcolor import colored # for colored text output
import subprocess  # for running shell commands
import time  # for time-related functions

#Colors
# Defining colors for text output
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_WHITE ='\033[97m'
COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

# Defining colors for ASCII text output
Banner = '\033[95m' + ''' .


                    *********************************** Welcome ************************************ 
          /$$$$$$   /$$                         /$$   /$$     /$$               /$$       /$$           /$$       
         /$$__  $$ | $$                        | $$  | $$    | $$              | $$      |__/          | $$     
        | $$  \__//$$$$$$    /$$$$$$   /$$$$$$ | $$ /$$$$$$  | $$$$$$$         | $$       /$$ /$$$$$$$ | $$   /$$
        |  $$$$$$|_  $$_/   /$$__  $$ |____  $$| $$|_  $$_/  | $$__  $$ /$$$$$$| $$      | $$| $$__  $$| $$  /$$/
        \____  $$ | $$     | $$$$$$$$  /$$$$$$$| $$  | $$    | $$  \ $$|______/| $$      | $$| $$  \ $$| $$$$$$/ 
         /$$  \ $$ | $$ /$$| $$_____/ /$$__  $$| $$  | $$ /$$| $$  | $$        | $$      | $$| $$  | $$| $$_  $$ 
        |  $$$$$$/ |  $$$$/|  $$$$$$$|  $$$$$$$| $$  |  $$$$/| $$  | $$        | $$$$$$$$| $$| $$  | $$| $$ \  $$
         \______/   \___/   \_______/ \_______/|__/   \___/  |__/  |__/        |________/|__/|__/  |__/|__/  \__/ 





 ''' + '\033[0m'

# Printing the banner
print(Banner)

# Printing some introductory text
print(COLOR_BLUE + "[" + COLOR_RESET + COLOR_YELLOW + "Stealth-Link" + COLOR_RESET  + COLOR_BLUE + "] " "Developed by D4RK5ID3 " + COLOR_RESET + COLOR_YELLOW + "Welcome to Stealth-Link script v1.0" + COLOR_RESET)

# Function to validate the URL input
def url_validator(url):
    if not url.startswith('http') and not url.startswith('https'):
        print(COLOR_RED + "[!] Invalid URL. Please use http or https." + COLOR_RESET)
        exit(1)


# Getting input URL from the user and validating it
link = input(COLOR_BLUE + "Input your Phishing URL (http or https): " + COLOR_RESET)

url_validator(link)

# Rebuilding the phishing URL using a web API
print(COLOR_YELLOW + "Rebuilding Phishing URL" + COLOR_RESET)

time.sleep (1) # Sleep for 1 second

print("")

# Compressing the URL using the is.gd API
compress = f"curl -s 'https://v.gd/create.php?format=simple&url={link}'"

comp = subprocess.check_output(compress, shell=True).decode('utf-8').strip()

compressed = comp.replace('https://', '')

print(COLOR_GREEN + " ### Concealing Domain ### " + COLOR_RESET)

mask = input(f"{COLOR_BLUE}Enter a Domain To Conceal The Phishing URL (http or https), ex: https://instagram.com, http://anything.org) :\n=> " + COLOR_RESET)

url_validator(mask)

# add some social engineering words to enabe link tolook more convincing
words = input("Type social engineering words:(like free-money, best-pubg-tricks)\n {COLOR_RED} Don't use space just use '-' between social engineering words\n=> " + COLOR_RESET)

print(COLOR_GREEN + "\n Generating StealthLink ...\n " + COLOR_RESET)

# print final Phishing link
final = f"{mask}-{words}@{compressed}"

print(f"{COLOR_GREEN}Here is the Modified StealthLink URL: \033[32m {final} \033[0m\n ")
