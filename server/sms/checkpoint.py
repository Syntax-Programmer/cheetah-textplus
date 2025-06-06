from rich import print


class SmsCheckpoint:
    def __init__(self, is_selected) -> None:
        self.is_selected = is_selected

    def checkpoint(self) -> None:
        print(f"[bold red] {self.is_selected} service is not available [/bold red]")
