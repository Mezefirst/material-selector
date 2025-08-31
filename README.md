# Material Selector AI Backend Scaffold
## material-selector 
-Sustainable solution

🚀 **Now ready for production deployment!**

## Features

- FastAPI backend for material recommendation
- Rule-based and ML-based material selection
- Natural language query parsing (OpenAI/Hugging Face ready)
- Simulation of performance trade-offs
- RL integration stub for future development
- **Progressive Web App (PWA) support**
- **Mobile-responsive design**
- **Docker containerization**
- **Production deployment configurations**

## Quick Start

### Development
```bash
# Backend
cd backend
pip install -r requirements.txt
python main.py

# Frontend
cd frontend
npm install
npm start
```

### Production Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide.

Quick deploy options:
- **Frontend**: Deploy to Vercel or Netlify
- **Backend**: Deploy to Railway, Heroku, or any container platform
- **Full Stack**: Use Docker Compose

## Endpoints

- **/**: API status and version
- **/health**: Health check endpoint
- **/recommend**: Recommend materials (supports structured and NLP queries)
- **/alternatives**: Suggest alternative materials
- **/tradeoff**: Simulate trade-offs between materials
- **/plan_rl**: Placeholder for RL-driven recommendations

## Mobile App

The frontend is a Progressive Web App (PWA) that provides:
- Native app-like experience on mobile devices
- Offline functionality
- Installation on home screen
- Responsive design for all screen sizes

## How to Extend

- Connect to your actual database for real data
- Enhance `services/nlp.py` with real NLP model or API
- Expand `services/recommender.py` with production logic
- Implement RL in `services/rl_stub.py` when ready
- Add authentication and user management
- Integrate with external material databases

## Technology Stack

- **Frontend**: React, Progressive Web App, Responsive Design
- **Backend**: FastAPI, Python, uvicorn
- **AI/ML**: scikit-learn, pandas, joblib
- **Deployment**: Docker, Docker Compose
- **Hosting**: Vercel/Netlify (frontend), Railway/Heroku (backend)

 
