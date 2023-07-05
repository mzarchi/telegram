import re
import pyfiglet as fig

from colorama import Fore

figlet = fig.Figlet()
fonts = figlet.getFonts()
figlet.setFont(font=fonts[36])

LOGIN_MESSAGE = f""" {Fore.GREEN}{figlet.renderText("Telethon Login")}{Fore.WHITE}
    Enter you're phone number is form of +<country code><phone number>
    example: +989331234567
"""


def ValidatePhone(phone: str) -> bool:
    """Validate user input is a valid phone number
    ~~~~~~~~~~~~~~~~~~~~~
    Args:
        :param `phone`: (str) telegram phone number

    Returns:
        :return: (bool)
    """
    reg = r"^\+[0-9]{12,12}$"
    # example: +981234567891
    return True if re.search(reg, phone) else False