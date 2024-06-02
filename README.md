# Hack 4 Tomorrow

## Talim Aushakhman

## Ludus AI

## Ludus AI - AI assistant for game designers. Powered by OpenAI: ChatGPT, DALL-E and Kadinsky.

### What can it do?
Ludus AI очень сильно упрощает работу гейм-дизайнерам. Он может создавать персонажей, диалоги, скетчи, концепты и сами ассеты и спрайты. Все что ему надо дать - вашу идею игры.

## Setup

### PostgreSQL (docker or postgresql are needed)

```bash
docker-compose up --build
```

### Backend (python are needed)
```bash
cd backend
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app
```

### Frontend (Node.js and npm are needed)
```bash
cd frontend
npm install
npm run dev
```
