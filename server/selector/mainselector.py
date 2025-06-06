import os
import questionary
import pyfiglet
from rich.console import Console
from server.sms.checkpoint import SmsCheckpoint
from server.edisp.epoint import ECheckpoint


def clear_screen() -> None:
    if os.name == "nt":  # windows system.
        os.system("cls")
    else:  # unix based system.
        os.system("clear")


def option_selected(console: Console) -> None:
    while True:
        clear_screen()
        banner = pyfiglet.figlet_format("CHEETAH", font="ansi_shadow")
        console.print(banner, justify="center")
        console.print(
            "__________welcome to cheetah textpulse__________\n",
            style="bold white",
            justify="center",
        )

        option = questionary.select(
            "SELECT CHOICES",
            choices=["Send to email inbox", "Send to sms", "Get help", "Exit"],
        ).ask()
        d_sms = SmsCheckpoint(option)
        d_email = ECheckpoint(option)

        if option == "Send to sms":
            d_sms.checkpoint()
        elif option == "Send to email inbox":
            d_email.checkpoint()
        elif option == " Get help":
            pass
        elif option == "Exit":
            break
