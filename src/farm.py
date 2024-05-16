from telegram.telegram import TelegramBot
from enclosure.enclosure import Enclosure
import time

class Farm(object):
    def __init__(self, cfg):
        """
        Initializes a Farm object.

        Args:
            cfg (dict): A dictionary containing the configuration settings.

        Attributes:
            cfg (dict): The configuration settings.
            token (str): The Telegram token.
            chatId (str): The Telegram chat ID.
            timer (int): The time between iterations. 
            bot (Telegram_Bot): The Telegram bot instance.
            printers (dict): A dictionary of printers.
        """
        
        self.cfg = cfg
        self.token = cfg['telegram']['token']
        self.chat_id = cfg['telegram']['chat_id']
        self.timer = cfg['farm']['timer']
        self.bot = TelegramBot(self) 
        self.printers = {"printer1": {"id": 1}, "printer2": {"id": 2}, "printer3": {"id": 3}}

       
    def get_bot(self):
        """
        Returns the bot associated with the farm.
        """
        return self.bot.bot.getMe()

    def get_printers(self):
        """
        Returns the list of printers available in the farm.

        Returns:
            list: A list of printers.
        """
        return list(self.printers.keys())

    def add_printer(self, id):
        """
        Adds a printer to the farm.

        Parameters:
        - id (int): The ID of the printer to be added.

        Returns:
        None
        """
        name = "printer"+str(id)
        self.printers[name] = {"id": id}


    def printers_list(self):  
        """
        Returns a formatted string containing the list of registered printers.

        Returns:
            str: A formatted string representing the printer list.
        """
        return list(self.printers.keys())


    def start(self):
        """
        Starts the farm simulation.

        This method continuously loops through each printer in the farm and generates new data
        for the printer and filament enclosures. It simulates the behavior of the printer and filament
        enclosures by calling their respective `loop_once` methods. The loop is repeated indefinitely
        until the program is interrupted.

        The duration of each iteration is controlled by the `timer` value specified in the `farm` section
        of the configuration file.

        Note: This method blocks the execution of the program until it is interrupted.

        Returns:
            None
        """
       
       
        while 1:
            for printer in list(self.printers.values()):
                """
                Here we do a for loop to go through all the printers inside the dictionary.
                We transform it to a list to make a copy of the values. We do it because when we modify
                the dictionary it chanches it size during the iteration and apears an error.

                We create a enclosure object for every prinetr and we pass as arguments the Farm() class
                and the printer id. Then we call the Enclosure() method loop_once() to generate, send, and
                check the data from the sensors.

                Finally we use the time module to stop some seconds (value we set on the config.yaml) 
                between iterations.
        
                """
                enclosure = Enclosure(self, printer["id"])
                enclosure.loop_once()
            

                time.sleep(self.timer)
            





