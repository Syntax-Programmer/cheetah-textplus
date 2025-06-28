from rich import print
from server.edisp.single import singlemails
from server.common_utils import choice_selector, clear_screen
import pyfiglet
from rich.console import Console


def print_email_banner(console: Console) -> None:
    clear_screen()
    banner = pyfiglet.figlet_format("CH . MAIL", font="ansi_shadow")
    console.print(banner, justify="center")
    console.print(
        "[bold green]Deliver personalized or bulk messages straight to your clients inboxes.\n[/bold green]",
        justify="center",
    )


def email_navigator(console: Console) -> None:
    while True:
        print_email_banner(console)

        option = choice_selector(["Single message", "Bulk message", "Back to Home"])

        if option == "Back to Home":
            break
        elif option == "Single message":
            singlemails.single_mails()
        elif option == "Bulk message":
            print(
                "[bold yellow]Bulk message functionality is not implemented yet.[/bold yellow]"
            )
