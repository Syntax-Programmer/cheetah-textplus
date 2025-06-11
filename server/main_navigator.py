import pyfiglet
from rich.console import Console
from server.sms.sms_navigator import sms_navigator
from server.edisp.email_navigator import email_navigator
from server.common_utils import choice_selector, clear_screen


def print_main_banner(console: Console) -> None:
    clear_screen()
    banner = pyfiglet.figlet_format("CHEETAH", font="ansi_shadow")
    console.print(banner, justify="center")
    console.print(
        "__________welcome to cheetah textpulse__________\n",
        style="bold white",
        justify="center",
    )


def main_navigator(console: Console) -> None:
    while True:
        print_main_banner(console)

        option = choice_selector(
            ["Send to email inbox", "Send to sms", "Get help", "Exit"],
        )

        if option == "Send to sms":
            sms_navigator(console)
        elif option == "Send to email inbox":
            email_navigator(console)
        elif option == " Get help":
            pass
        elif option == "Exit":
            break
