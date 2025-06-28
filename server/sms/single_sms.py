from server.common_utils import return_buffer
from server.sms.sms_utils import get_number
from rich.prompt import Prompt


def single_sms() -> None:
    to = get_number()
    msg = Prompt.ask("\n[bold][green]╾➤ [/green] Message[/bold]")

    return_buffer()
