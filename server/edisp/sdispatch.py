import re
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from rich import print
from email.utils import formatdate

email_validator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co)$"
#content_validator_ptn = r"--subject\s([^\r\n]+)\n--header\s([^\r\n]+)\n--to\s([^\r\n]+)\n--message\s([^\r\n]+)"
load_dotenv()
mail = os.getenv("MAIL")
password = os.getenv("PASS")

class ContentValidator:
  
  def __init__(self , subject, header, to, message):
     self.subject = subject
     self.header = header
     self.to = to 
     self.message = message
     
  def check_content_pattn(self):
    
    is_valid_email_format = re.match(email_validator, self.to)
    
    if is_valid_email_format:
      return {
        "subject" : self.subject,
        "header" : self.header,
        "to_email" : self.to,
        "message" : self.message
      }
    else:
      print("invalid")
      
  def dispatch_email(self):
    content = self.check_content_pattn()
    msg = EmailMessage()
    msg.set_content(f'hey there i just want to check in.')
    msg['Reply-To'] = 'Abdulrokibadebisi@gmail.com'
    msg['subject'] = f'{content["subject"]}'
    msg['from'] = 'Abdulrokibadebisi@gmail.com'
    msg['Date'] = formatdate(localtime=True)
    msg['to'] = content['to_email']
    
    msg.add_alternative(f"""
        <div>
          <h2>{content["header"]}</h2>
          <p style='font-size:0.8rem;'>
            {content["message"]}
          </p>
          <h3>from [Black Chameleon]</h3>
        </div>
      """ , subtype='html')
    
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp:
      smtp.login( mail , password)
      smtp.send_message(msg)
      print(f'\n✔️ [bold]Sent[/bold]')
      
