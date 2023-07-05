import sys
import getpass
import telethon
import utils
import config as ac
from telethon.sync import TelegramClient

sys.path.append('./')

class ClientManager:
    """Base Class For login"""
    __phoneNumber = None
    __TwoFactor = None
    __LoginCode = None
    __Client = None

    def GetPhoneNumber(self):
        """Get User Phone Number"""
        while True:
            print(utils.LOGIN_MESSAGE)
            x = input(": ")
            if not utils.ValidatePhone(x):
                print("Invalid Phone number :(")
                continue
            else:
                self.__phoneNumber = x

    def GetLoginCode(self):
        """Get Telegram Code in Hidden Mode"""
        self.__LoginCode = getpass.getpass("LoginCode: ")

    def GetTwoStepCode(self):
        """Get 2-Step code in hidden mode"""
        self.__TwoFactor = getpass.getpass("2-Step Code: ")


    def LoginClient(self):
        """Login Method"""
        self.GetPhoneNumber()
        client = TelegramClient(
            f'sessions/{self.__phoneNumber.replace("+", "")}', ac.api_id, ac.api_hash)
        client.connect()
        client.send_code_request(self.__phoneNumber, force_sms=False)
        self.GetLoginCode()
        try:
            client.sign_in(self.__phoneNumber, code=self.__LoginCode)
        except telethon.errors.SessionPasswordNeededError:
            self.GetTwoStepCode()
            client.sign_in(password=self.__TwoFactor)
        print("Successfully Connect!\nSession created at sessions dir")
        self.__Client = client


    def GetClient(self):
        """Use This Method For Getting <TelegramClient> client"""
        return self.__Client





client = ClientManager()
client.LoginClient()
