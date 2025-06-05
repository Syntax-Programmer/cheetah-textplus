import re
from rich import print
from rich.prompt import Prompt
import shlex
from server.edisp.sdispatch import ContentValidator

def single_mails():

  subject = Prompt.ask("\n[bold][green]╾➤ [/green] Subject[/bold]")
  header = Prompt.ask("\n[bold][green]╾➤ [/green] Header[/bold]")
  to = Prompt.ask("\n[bold][green]╾➤ [/green] To[/bold]")
  message = Prompt.ask("\n[bold][green]╾➤ [/green] Message[/bold]")
    
  if subject == "" or header == "" or to=="" or message=="":
    print(f"\n[bold red] ❗ invalid prompt format dectected___[/bold red]")
  else:
    p = ContentValidator(subject, header, to, message)
    
    if subject and header and to and message:
      p.dispatch_email()
      
    
  
  
  
  
  
  
  