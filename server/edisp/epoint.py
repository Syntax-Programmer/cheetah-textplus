from rich import print
from server.edisp.esingle import singlemails
import os
import questionary
import pyfiglet


class ECheckpoint:
    def __init__(self, is_selected) -> None:
        self.is_selected = is_selected

    def checkpoint(self):
        os.system("clear")
        banner = pyfiglet.figlet_format("CH . MAIL", font="ansi_shadow")
        print(banner)
        print(
            "[bold green]Deliver personalized or bulk messages straight to your clients inboxes.\n[/bold green]"
        )

        option = questionary.select(
            "Select a send method:",
            choices=["Single message", "Bulk message", "Back to Home"],
        ).ask()

        if option == "Back to Home":
            return
        elif option == "Single message":
            singlemails.single_mails()

        return option
