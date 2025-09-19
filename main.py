import ssl
import resend
import smtplib
from dotenv import load_dotenv
from functools import lru_cache
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from email.message import EmailMessage
from pydantic_settings import BaseSettings
load_dotenv()


class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    html: bool = False

class Settings(BaseSettings):
    smtp_host: str = Field("SMTP_HOST")
    smtp_port: int = Field("SMTP_PORT")
    smtp_user: str = Field("SMTP_USER")
    smtp_password: str = Field("SMTP_PASSWORD")
    secret_key: str = Field("SECRET_KEY")
    resend_api_key: str = Field("RESEND_API_KEY")

class SMTPClient:
    def __init__(self, host: str, port: int, user_id: str, password: str) -> None:
        self.host = host
        self.port = port
        self.user_id = user_id
        self.password = password

    def Send(self, email_request: EmailRequest) -> bool:
        msg = EmailMessage()
        msg["From"] = self.user_id
        msg["To"] = email_request.to
        msg["Subject"] = email_request.subject

        if email_request.html:
            msg.set_content("This message contains HTML. Open in an HTML-capable client.")
            msg.add_alternative(email_request.body, subtype="html")
        else:
            msg.set_content(email_request.body)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.host, self.port, timeout=30) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.user_id, self.password)
            server.send_message(msg)

class ResendClient:
    def __init__(self, resend_api_key: str):
        self.resend_api_key = resend_api_key

    def Send(self, email_request: EmailRequest) -> bool:
        resend.api_key = self.resend_api_key
        try:
            r = resend.Emails.send({
                "from": "info@spiritualtours.com <onboarding@resend.dev>",
                "to": email_request.to,
                "subject": email_request.subject,
                "html": email_request.body
            })
        except resend.exceptions.ResendError as e:
            return str(e)
        return True


app = FastAPI(title="⚡ ZapMail")
settings = Settings()
origins = ["http://localhost:8000", "https://spiritualtours.web.app", "https://spiritualtours.com"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@lru_cache
def verify_secret(x_secret: str = Header(...)):
    if x_secret != settings.secret_key:
        raise HTTPException(status_code=412, detail="Invalid or missing secret")

@app.post("/send")
async def send_email(email_request: EmailRequest, dep: None = Depends(verify_secret)):
    try:
        # SMTPClient(settings.smtp_host, settings.smtp_port, settings.smtp_user, settings.smtp_password).Send(email_request)
        r = ResendClient(settings.resend_api_key).Send(email_request)
        if r != True:
            return r
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=502, detail=f"SMTP error: {e}")

    return {"status": "success", "message": f"Send successfully to {email_request.to}"}
