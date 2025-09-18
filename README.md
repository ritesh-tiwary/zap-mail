# ⚡ ZapMail  

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python) ![SMTP](https://img.shields.io/badge/SMTP-Gmail-red?logo=gmail) ![License](https://img.shields.io/badge/License-MIT-green.svg)


## ZapMail – Fast, Simple, Gmail-Powered Email API
**ZapMail** is your go-to **lightweight FastAPI backend** for sending emails via **Gmail SMTP**, built for consumers who want **speed, simplicity, and control**.
Say goodbye to heavy third-party platforms — **ZapMail** lets you **run your own email backend** and expose it publicly with minimal setup.

Deploy it on **Heroku, Render, or any server** and start zapping emails ⚡ in minutes. 

🔥 **Tagline:** Stop snail mail 🐌. Start ZapMail ⚡.

---

## ✨ Features
- ⚡ **Lightning Fast** email delivery with Gmail SMTP  
- 🌐 **Public API** – expose endpoints for any app or service
- 🔌 **Easy API Integration** for any app, website, or service
- 📬 **Rich Emails** – HTML, attachments, multiple recipients  
- 🔐 **Environment-based Config** – no secrets in code  
- 🛠 **Open Source & Extensible** – hack, fork, contribute  
- ☁️ **Deploy Anywhere** – Heroku, Render, Docker, or bare metal  

---
## 📂 Project Structure
```css
zap-mail/
 ├── main.py
 ├── requirements.txt
 ├── Dockerfile
 ├── README.md
 ├── .gitignore
 └── LICENSE
```

---
## 🚀 Quick Start  

#### 1️⃣ Clone the Repo
```bash
git clone https://github.com/ritesh-tiwary/zap-mail.git
cd zap-mail
```

#### 2️⃣ Create Virtual Environment & Install
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

#### 3️⃣ Run the App
```bash
  uvicorn main:app --reload
```
```bash
  curl -X POST "http://localhost:8000/send" \
    -H "Content-Type: application/json" \
    -d '{"to":"recipient@example.com","subject":"Hello","body":"Hi from ⚡ ZapMail!!","html":false}'
```
```bash
curl -X POST "https://zap-mail-production.up.railway.app/send" \
    -H "Content-Type: application/json" \
    -d '{"to":"recipient@example.com","subject":"Hello from ⚡ ZapMail","body":"<p>Congrats on sending your first <strong>⚡ ZapMail</strong>!</p>"}'
```
---
### 📡 API Endpoints
**POST:** /send

**Request Example:**

```json
headers: 
{
  "from": "sender@gmail.com",
  "pass": "sender_email_app_password"
}

body:
{
  "to": ["recipient@example.com"],
  "subject": "Hello from ZapMail ⚡",
  "body": "<h1>This is a test email</h1>",
  "attachments": []
}
```
**Response Example:**
```json
{
  "status": "success",
  "message": "Send successfully to recipient@example.com"
}
```

---
### ☁️ Deploy to the Cloud
#### 🔹 Deploy on Render
**1.** Push this repo to GitHub. \
**2.** Login to Render. \
**3.** Create New Web Service → Connect your repo. \
**4.** Set:
- **Build Command:** pip install -r requirements.txt
- **Start Command:** gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
- **Environment Variables:** SMTP_USER, SMTP_PASSWORD

**5.** Deploy 🚀
  

#### 🔹 Deploy on Heroku
```bash
curl https://cli-assets.heroku.com/install.sh | sh
echo "export HEROKU_API_KEY=your_api_key_here" >> ~/.bashrc
source ~/.bashrc

heroku auth:whoami   # check current user
heroku auth:token    # verify token works

heroku create zapmail-app
git push heroku main
```

#### 🔹 Deploy on railway.com
```bash
curl -fsSL https://railway.com/install.sh | sh
echo "export RAILWAY_TOKEN=your_token" >> ~/.bashrc
source ~/.bashrc

railway login --browserless
railway whoami   # check current user
```

---
### 🛡️ Security Notes
- Always use App Passwords with Gmail (not your main password)
- Never commit .env files to GitHub
- Use HTTPS in production

---
### 🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

---
### 📜 License
MIT License © 2025 – Made with ❤️ by the ZapMail community.
