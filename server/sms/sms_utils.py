from rich.prompt import Prompt
from server.common_utils import choice_selector


def get_number() -> str:
    ph_no = Prompt.ask("\n[bold][green]╾➤ [/green] Phone Number[/bold]")

    return ph_no
