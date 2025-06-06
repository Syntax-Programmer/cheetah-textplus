import re
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from rich import print
from email.utils import formatdate

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co)$"
# content_validator_ptn = r"--subject\s([^\r\n]+)\n--header\s([^\r\n]+)\n--to\s([^\r\n]+)\n--message\s([^\r\n]+)"
load_dotenv()
mail = os.getenv("MAIL")
password = os.getenv("PASS")


class ContentValidator:
    def __init__(self, subject, header, to, message) -> None:
        self.subject = subject
        self.header = header
        self.to = to
        self.message = message

    def check_content_pattern(self) -> dict[str, str | None]:
        is_valid_email_format = re.match(EMAIL_REGEX, self.to)

        if is_valid_email_format:
            return {
                "subject": self.subject,
                "header": self.header,
                "to_email": self.to,
                "message": self.message,
            }
        print("invalid")
        # Default return if the email format is invalid to satisfy type checker.
        return {
            "subject": None,
            "header": None,
            "to_email": None,
            "message": None,
        }

    def dispatch_email(self):
        content = self.check_content_pattern()
        msg = EmailMessage()
        msg.set_content("hey there i just want to check in.")
        msg["Reply-To"] = "Abdulrokibadebisi@gmail.com"
        msg["subject"] = f"{content['subject']}"
        msg["from"] = "Abdulrokibadebisi@gmail.com"
        msg["Date"] = formatdate(localtime=True)
        msg["to"] = content["to_email"]

        msg.add_alternative(
            f"""
        <div>
          <h2>{content["header"]}</h2>
          <p style='font-size:0.8rem;'>
            {content["message"]}
          </p>
          <h3>from [Black Chameleon]</h3>
        </div>
      """,
            subtype="html",
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(mail, password)
            smtp.send_message(msg)
            print("\n✔️ [bold]Sent[/bold]")
