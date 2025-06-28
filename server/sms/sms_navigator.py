from server.common_utils import choice_selector, clear_screen
from server.sms.single_sms import single_sms
from server.sms.bulk_sms import bulk_sms
import pyfiglet
from rich.console import Console


def print_sms_banner(console: Console) -> None:
    clear_screen()
    banner = pyfiglet.figlet_format("CH . SMS", font="ansi_shadow")
    console.print(banner, justify="center")
    console.print(
        "[bold green]Deliver SMS straight to your clients inboxes.\n[/bold green]",
        justify="center",
    )


def sms_navigator(console: Console) -> None:
    while True:
        print_sms_banner(console)

        option = choice_selector(["Single SMS", "Bulk SMS", "Back to Home"])

        if option == "Back to Home":
            break
        elif option == "Single SMS":
            single_sms()
        elif option == "Bulk SMS":
            bulk_sms()
