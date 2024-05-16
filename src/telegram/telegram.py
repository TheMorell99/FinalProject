import telepot
from telepot.loop import MessageLoop
from enclosure.enclosure import Enclosure


help_msg = '1- If the command is /add_printer <printer_id>, we add a new printer to the farm.\n2- If the command is /printers_list, we list all the printers.\n3- If the command is /activate <fan or gate> <printer_id>, we activate the fan or gate of the specified printer.'


class TelegramBot(object):

    def __init__(self, farm):
        """
        Initializes a Telegram object.
        We start the Loop to listen for messages.

        Args:
            farm (Farm): The Farm object containing the token and chat ID.

        Returns:
            None
        """
        self.farm = farm 
        self.bot = telepot.Bot(self.farm.token)
        MessageLoop(self.bot, self.handle).run_as_thread()
        
        


    def handle(self, msg):
        """
        Handles the incoming message from the Telegram bot.

        1- If the command is /add_printer <printer_id>, we add a new printer to the farm.
        2- If the command is /printers_list, we list all the printers.
        3- If the command is /activate <fan or gate> <printer_id>, we activate the fan or gate of the specified printer.
        4- If the command is /help, we send a help message to the user.
        5- If the command is unknown, we send an error message to the user.

        Args:
            msg (dict): The message received from the Telegram bot.

        Returns:
            None
        """
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        print(telepot.glance(msg))

        if content_type == 'text':
            
            if msg['text'].startswith('/add_printer'):
                """
                This command adds a new printer. 
                First we split the message and look if the length is correct.
                We also make sure the id is not under zero.
                Then do a cast to make sure the input is an integer. 
                If it's an integer we look if the printer exist, and call the farm 
                method add_printer() to add to the dictinary.
                If the message is not correct or the id is not an integer 
                send the proper message.
                """

                msg_list = msg['text'].split(' ')
                printer_id = msg_list[1]

                if len(msg_list) == 2:
                    try:
                        printer_id = int(printer_id)

                        if printer_id > 0:

                            if 'printer'+str(printer_id) in self.farm.printers.keys():
                                self.bot.sendMessage(chat_id, f'Printer with id {printer_id} already exist.')

                            else:
                                self.farm.add_printer(printer_id)
                                self.bot.sendMessage(chat_id, f'Printer with id {printer_id} added correctly.')
                        else:
                            self.bot.sendMessage(chat_id, 'Printer id should be positive integer.')
  
                    except:
                        self.bot.sendMessage(chat_id,
                                            'Incorrect type of id. It shoud be an integer.')
                
                else:
                    self.bot.sendMessage(chat_id, 
                                        'Incorrect input. Message structure should be: /add_printer <printer_id>')

                


            elif msg['text'] == '/printers_list':
                """
                This command returns the printers list calling the correspondign method from the farm.
                """
                self.bot.sendMessage(chat_id, str(self.farm.get_printers()))
            
            


            elif msg['text'].startswith('/activate'):
                """
                This command activates the fan or gate of a printer.
                First we split the message and look if the message structure is correct.
                If all is correct we do a try/except to make sure the id of the printer is 
                an integer. If it is, we look if the printer exist and the call the corresponding
                method from the encosure class.

                """
                
                msg_list = msg['text'].split(' ')
                actuator = msg_list[1]
                printer_id = msg_list[2]

                if len(msg_list) != 3:
                    self.bot.sendMessage(chat_id, 
                                         'Incorrect input. Message structure should be: /activate <fan or gate> <printer_id>')
                
                elif actuator in ['fan', 'gate']:

                    try:
                        printer_id = int(printer_id)

                        if 'printer'+str(printer_id) in self.farm.printers.keys():
                            if actuator == 'fan':
                                Enclosure(self.farm, printer_id).activate_fan()                                
                            else:
                                Enclosure(self.farm, printer_id).open_gate()
                        
                        else:
                            self.bot.sendMessage(chat_id,
                                         f'Printer id: {printer_id} doesn''t exist')
                            
                    except:
                        self.bot.sendMessage(chat_id,
                                         'Incorrect type of id. It shoud be an integer.')
                else:
                    self.bot.sendMessage(chat_id,
                                        'Incorrect input. It shoud be <fan> or <gate>.')



            elif msg['text'] == '/help':
                """
                This command sends the user a help message with all the comands.
                """
                self.bot.sendMessage(chat_id, help_msg)
            


            else:
                self.bot.sendMessage(chat_id, 'Command unknown, it must be text. Type /help for more.')
        


        else:
            self.bot.sendMessage(chat_id, 'Command unknown, it must be text. Type /help for more.')
        



    def sendMessage(self, msg):
        """
        Sends a message to the user.

        Args:
            msg (str): The message to be sent.

        Returns:
            None
        """
        self.bot.sendMessage(self.farm.chat_id, msg)
        





