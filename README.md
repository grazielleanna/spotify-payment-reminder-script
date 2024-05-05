# Spotify Payment Reminder Script

This script was developed with a particular need in mind: I have the Spotify family plan and share it with some family members. Each month, a person pays the amount that is automatically deducted from my credit card.

Pain point: People forgot what their payment month was, so I created a WhatsApp group to remind them, but I also forgot to update it. With that, came the idea of ​​creating a script that would check the person paying for the current month and the next. When identified, an automatic message is sent to their WhatsApp via Selenium

## Instalation

Clone the project, create your venv, and install the packages from the requirements.txt file.

You need to download the Google Chrome drive which must be compatible with the version you have installed on your computer and enter it in the path: ```C:\chrome-driver```

## Settings
In lines 67 to 76 of the code of main.py file, configure the participating users.

Then open Google Chorme by running the command: ```"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222```, open WhatsApp web and authenticate, leave the tab open.

Then run the script.