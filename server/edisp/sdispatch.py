import re
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from rich import print
from email.utils import formatdate

# content_validator_ptn = r"--subject\s([^\r\n]+)\n--header\s([^\r\n]+)\n--to\s([^\r\n]+)\n--message\s([^\r\n]+)"


class EmailHandler:
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co)$"

    def __init__(self, subject: str, header: str, to: str, message: str) -> None:
        self.data: dict[str, str] | None = None
        load_dotenv()
        self.FROM = os.getenv("FROM", "")
        self.PASSWD = os.getenv("PASSWD", "")
        self.REPLY_TO = os.getenv("REPLY_TO", "")

        if self.__check_content_pattern(subject, header, to, message):
            self.data = {
                "subject": subject,
                "header": header,
                "to_email": to,
                "message": message,
            }

    def __check_env_vars(self) -> bool:
        if not self.FROM or not self.PASSWD or not self.REPLY_TO:
            print(
                "[bold red]❗ Environment variables are not set properly. "
                "Please check your .env file.[/bold red]"
            )
            return False
        return True

    def __check_email_format(self, to: str) -> bool:
        if re.match(self.EMAIL_REGEX, to) is None:
            print("[bold red]❗ Invalid email format detected.[/bold red]")
            return False
        return True

    def __check_content_pattern(
        self, subject: str, header: str, to: str, message: str
    ) -> bool:
        if not subject or not header or not to or not message:
            print("[bold red]❗ Missing required fields.[/bold red]")
            return False
        return bool(self.__check_email_format(to) and self.__check_env_vars())

    def dispatch(self) -> bool:
        if (self.data is None) or not self.data:
            print(
                "[bold red]❗ Invalid data format detected. Can't dispatch email.[/bold red]"
            )
            return False
        msg = EmailMessage()
        msg.set_content("Hey there, I just want to check in.")
        msg["Reply-To"] = self.REPLY_TO
        msg["Subject"] = self.data["subject"]
        msg["From"] = self.FROM
        msg["Date"] = formatdate(localtime=True)
        msg["To"] = self.data["to_email"]

        msg.add_alternative(
            f"""
        <div>
          <h2>{self.data["header"]}</h2>
          <p style='font-size:0.8rem;'>
            {self.data["message"]}
          </p>
          <h3>from [Black Chameleon]</h3>
        </div>
            """,
            subtype="html",
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.FROM, self.PASSWD)
            smtp.send_message(msg)
            print("✔️ [bold green]Sent[/bold green]")

        return True
