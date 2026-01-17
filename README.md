🤖 Chatbot Platform API

A production-ready multi-project chatbot platform built with FastAPI, PostgreSQL, and JWT authentication.
Supports custom system prompts, project-based conversations, and AI responses via OpenRouter API.

Live Demo:
👉 https://chatbot-platform-0l28.onrender.com
    https://chatbot-platform-0l28.onrender.com/docs

🚀 Features

✔ User Authentication (JWT)
✔ Project-based chatbot system
✔ Custom system prompts per project
✔ Chat history storage
✔ AI integration using OpenRouter
✔ Secure password hashing
✔ Role-based API protection
✔ Production deployment on Render

🏗 Tech Stack
Layer	Technology
Backend	FastAPI
Database	PostgreSQL
Auth	JWT
ORM	SQLAlchemy
AI	OpenRouter API
Hosting	Render
Version Control	GitHub
📂 Project Structure
chatbot-platform/
│
├── app/
│   ├── auth/
│   ├── users/
│   ├── projects/
│   ├── chat/
│   ├── prompts/
│   ├── core/
│   └── db/
│
├── requirements.txt
├── main.py
└── README.md

🔐 Authentication Flow

Register user

Login to get JWT token

Use token in Authorization header

Access protected routes

Header format:

Authorization: Bearer <your_token>

📌 API Endpoints
Auth
Method	Endpoint	Description
POST	/auth/register	Register user
POST	/auth/login	Login user
GET	/auth/me	Get profile
Projects
Method	Endpoint
POST	/projects/create
GET	/projects/my
Prompts
Method	Endpoint
PUT	/prompts/{project_id}
Chat
Method	Endpoint
POST	/chat/{project_id}

⚠ Swagger UI Note

Swagger UI has OAuth formatting limitations.
Authentication works perfectly via:

✔ Curl
✔ Postman
✔ Frontend clients

Production systems use Postman/clients, not Swagger auth.

🧪 Sample Curl Commands
Login
curl -X POST "https://chatbot-platform-0l28.onrender.com/auth/login" \
-d "username=test@email.com&password=123456"

Create Project
curl -X POST "https://chatbot-platform-0l28.onrender.com/projects/create?name=mybot" \
-H "Authorization: Bearer YOUR_TOKEN"

Update Prompt
curl -X PUT "https://chatbot-platform-0l28.onrender.com/prompts/1?content=You are a math teacher" \
-H "Authorization: Bearer YOUR_TOKEN"

Chat
curl -X POST "https://chatbot-platform-0l28.onrender.com/chat/1?message=Explain AI" \
-H "Authorization: Bearer YOUR_TOKEN"

🔒 Security

✔ Hashed passwords (bcrypt)
✔ JWT token validation
✔ Protected routes
✔ Environment variables for secrets

🌐 Deployment

Hosted on Render
Auto-deploys from GitHub
Uvicorn production server

📈 Future Enhancements

Frontend UI

Chat history UI

Rate limiting

User roles

Webhooks

Analytics dashboard

👨‍💻 Author

Aditya Hegde
Electronics & Communication Engineer
Backend | AI | Embedded Systems

GitHub: https://github.com/hegdeadityaurk

Add project README
