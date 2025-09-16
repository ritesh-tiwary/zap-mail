import os
import smtplib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email.message import EmailMessage


app = FastAPI(title="⚡ ZapMail")

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    html: bool = False

@app.post("/send")
async def send_email(req: EmailRequest):
    if not SMTP_USER or not SMTP_PASSWORD:
        raise HTTPException(status_code=500, detail="SMTP credentials are not configured on server.")

    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = req.to
    msg["Subject"] = req.subject

    if req.html:
        msg.set_content("This message contains HTML. Open in an HTML-capable client.")
        msg.add_alternative(req.body, subtype="html")
    else:
        msg.set_content(req.body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise HTTPException(status_code=502, detail=f"SMTP error: {e}")

    return {"status": "success", "message": f"Send successfully to {req.to}"}
