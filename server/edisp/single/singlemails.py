from rich.prompt import Prompt
from server.edisp.sdispatch import EmailHandler
from server.common_utils import return_buffer


def single_mails():
    subject = Prompt.ask("\n[bold][green]╾➤ [/green] Subject[/bold]")
    header = Prompt.ask("\n[bold][green]╾➤ [/green] Header[/bold]")
    to = Prompt.ask("\n[bold][green]╾➤ [/green] To[/bold]")
    message = Prompt.ask("\n[bold][green]╾➤ [/green] Message[/bold]")

    handler = EmailHandler(subject, header, to, message)
    handler.dispatch()

    return_buffer()
