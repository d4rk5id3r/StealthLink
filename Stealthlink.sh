#!/bin/bash


#Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
grayColour="\e[0;37m\033[1m"

echo -e "${yellowColour}"
echo -e "*********************************** Welcome ************************************ "
ART='
          /$$$$$$   /$$                         /$$   /$$     /$$               /$$       /$$           /$$       
         /$$__  $$ | $$                        | $$  | $$    | $$              | $$      |__/          | $$     
        | $$  \__//$$$$$$    /$$$$$$   /$$$$$$ | $$ /$$$$$$  | $$$$$$$         | $$       /$$ /$$$$$$$ | $$   /$$
        |  $$$$$$|_  $$_/   /$$__  $$ |____  $$| $$|_  $$_/  | $$__  $$ /$$$$$$| $$      | $$| $$__  $$| $$  /$$/
        \____  $$ | $$     | $$$$$$$$  /$$$$$$$| $$  | $$    | $$  \ $$|______/| $$      | $$| $$  \ $$| $$$$$$/ 
         /$$  \ $$ | $$ /$$| $$_____/ /$$__  $$| $$  | $$ /$$| $$  | $$        | $$      | $$| $$  | $$| $$_  $$ 
        |  $$$$$$/ |  $$$$/|  $$$$$$$|  $$$$$$$| $$  |  $$$$/| $$  | $$        | $$$$$$$$| $$| $$  | $$| $$ \  $$
        \______/   \___/   \_______/ \_______/|__/   \___/  |__/  |__/        |________/|__/|__/  |__/|__/  \__/  '

printf "${ART}\n"

 echo -e "${blueColour}[${endColour}${yellowColour}Stealth-Link${endColour}${blueColour}] Developed by D4RK5ID3${endColour} ${yellowColour}Welcome to Stealth-Link script v1.0 ${endColour}"
url_validator() {
    if [ ! "${1//:*}" = http ]; then 
       if [ ! "${1//:*}" = https ]; then 
           echo -e "\e[31m[!] Invalid Web URL. Please Use http or https.\e[0m"
           exit 1
       fi 
    fi

}

echo -e "\n ${blueColour}Input your Phishing URL (http or https):" 

read link

url_validator $link

sleep 1 

echo  -e "\n ${yellowColour} Rebuilding Phishing URL"

echo   ""

compress=$(curl -s "https://is.gd/create.php?format=simple&url=${link}")

url=${compress#https://}

echo -e "\n ${greenColour} ### Concealing Domain ### ${endColour}"

echo -e "\n ${blueColour} Enter a Domain To Conceal The Phishing URL (http or https), ex: https://instagram.com, http://anything.org) :"

echo -en "${greenColour}"

read mask

url_validator $mask

echo -e '\n Add Social Engineering Words:(like Password-Reset OR Free-Gift-Cards)'

echo -e  "\ ${redColour}Don't use space just use '-' between social engineering words \e[0m"  

echo -en "\ ${greenColour}"

read words 

if [[ -z "$words" ]]; then

echo -e "\ ${redColour} [!] No Words Detected."

echo -e "\n ${greenColour} Generating StealthLink ...\n"

final="${mask}"@"${url}"

echo -e "Here Is your StealthLink URL: ${grayColour} ${final}"

exit 

fi

if [[ "$words" =~ " " ]]; then

echo -e "${redColours} Invalid words. Please avoid Spaces."

echo -e "\n Generating StealthLink... \n"

final=$mask@$url

echo -e "Here is the StealthLink URL: ${grayColour} ${final}"

exit

fi

echo -e "\n Generating your StealthLink... \n"

final="$mask"-"$words"@"$url"

echo -e "Here is the Modified StealthLink URL: ${redColour} ${final}" 


