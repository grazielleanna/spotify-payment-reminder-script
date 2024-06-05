from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from datetime import datetime
from typing import Literal
from classes.SpotifyPerson import SpotifyPerson

class Main:
    def __init__(self) -> None:
        self._identifies_paying_user_for_month_and_next()

    def _start_selenium(self):
        """
        Create the chrome driver

        Author:
        Grazielle Conceição

        Date: 
        2024-05-05
        """
        chrome_path = 'C:\chrome-driver\chromedriver.exe'

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(r"user-data-dir=C:\Users\grazi\AppData\Local\Google\Chrome\User Data")

        service = ChromeService(executable_path=chrome_path)

        driver = webdriver.Chrome(options=chrome_options, service=service)

        driver.get("https://web.whatsapp.com/")
        time.sleep(10)
        self.driver = driver

    def _close_selenium(self):
        self.driver.quit()

    def _send_message_whatsapp(self, contact_name: str, message: str):
        """
        Args:
        contact_name (str): The name of the contact on WhatsApp who will send the message
        message (str): Message that will be sent
        """
        search_box = self.driver.find_element(by=By.XPATH, value="//div[@contenteditable='true'][@aria-label='Search input textbox']")
        search_box.click()
        search_box.send_keys(contact_name + Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        contact = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@title='{contact_name}']")))
        contact.click()

        message_box =  wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@contenteditable='true'][@aria-label='Type a message']")))

        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)

    def _identifies_paying_user_for_month_and_next(self):
        """
        Based on the current month, it identifies the paying user and the user who must pay in the next month.

        Author:
        Grazielle Conceição

        Date:
        2024-05-05
        """

        spotify_users= ['Marllon', 'Grazielle', 'Thayná', 'Beathriz', 'Mauro', 'Raiana']

        """
            On the left side is the person's name and on the right side is the name of their contact on your WhatsApp
        """
        spotify_users_contact = {
            'Marllon': 'Marllon ❤️',
            'Grazielle': 'Grazi',
            'Thayná': 'Thayná ❤️',
            'Beathriz': 'Enfermagem por Amor ❤️',
            'Mauro': 'Dindo Mauro ❤️',
            'Raiana': 'Rai ❤️'
        }

        current_month = datetime.now().month
        current_year = datetime.now().year

        """
        Adapted so that when the month is longer than 6, you can get the person who must pay, as Spotify only allows up to 6 people on the plan
        """
        paying_user_index = current_month - 1 if current_month < 7 else (current_month - 7) % len(spotify_users)
        paying_user = spotify_users[paying_user_index]
      
        next_month = current_month + 1
        next_month = 1 if next_month == 13 else next_month

        next_paying_user_index = next_month - 1 if next_month < 7 else (next_month - 7) % len(spotify_users)
        paying_user_next_month = spotify_users[next_paying_user_index]

        people_send_message = [SpotifyPerson(paying_user, 'paying_user'), SpotifyPerson(paying_user_next_month, 'next_paying_user')]

        time.sleep(5)

        self._start_selenium()

        for person in people_send_message:
            if person.name != 'Grazielle':
                message = self._get_messages_to_send(current_month=current_month, current_year=current_year, message=person.type)
                contact_name_whatsapp = spotify_users_contact[person.name]
                self._send_message_whatsapp(contact_name=contact_name_whatsapp, message=message)

        self._close_selenium()

    def _get_messages_to_send(self, current_month: int, current_year: int, message: Literal['paying_user', 'next_paying_user']):
        """
        Args:
        current_month (int): The current month
        current_year (int): The current year

        Returns:
        str

        Author: 
        Grazielle Conceição

        Date:
        2024-05-05
        """
        if message == 'paying_user':
            message_to_paying_user = f'''
                Atenção: O envio dessa mensagem é automático.

                Olá, essa mensagem está sendo enviada pelo robô da Grazi. Este é um lembrete que este mês (08/{current_month}/{current_year}) é a sua vez de realizar o pagamento do Spotify.
                O valor atual é de R$ 34,90 e pode ser transferido para a chave pix: CPF 191.281.727-60

                Você será avisado com 1 mês de antecedência quando for a próxima vez de realizar o pagamento do Spotify. Obrigada!
            '''

            return message_to_paying_user
        else:
            next_month = current_month + 1 if current_month < 12 else 1
            year_next_month_alert = (current_year + 1) if next_month == 1 else current_year

            message_to_next_paying_user = f'''
                Atenção: O envio dessa mensagem é automático.

                Olá, essa mensagem está sendo enviada pelo robô da Grazi. Este é um lembrete informando que no próximo mês (08/{next_month}/{year_next_month_alert}) é a sua vez de realizar o pagamento do Spotify.
                Mas não se preocupe, quando iniciar o próximo mês você receberá um novo lembrete. Obrigada!
            '''

            return message_to_next_paying_user

if __name__ == '__main__':
    Main()