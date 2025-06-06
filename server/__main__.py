# from rich import print
from rich.console import Console
from server.selector.mainselector import option_selected
# import os
# import pyfiglet


def main() -> None:
    console = Console()
    option_selected(console)


if __name__ == "__main__":
    main()
