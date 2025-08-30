# Deployment Guide for Material Selector

## Overview
This guide covers deploying both the web app and mobile-ready PWA (Progressive Web App) version of the Material Selector.

## Architecture
- **Frontend**: React PWA with responsive design
- **Backend**: FastAPI with material recommendation AI
- **Database**: File-based (can be upgraded to PostgreSQL)

## Deployment Options

### Option 1: Quick Deploy (Recommended for Testing)

#### Backend - Railway/Heroku
1. Create account on Railway.app or Heroku
2. Connect your GitHub repository
3. Deploy from `/backend` folder
4. Set environment variables:
   - `ENV=production`
   - `PORT=8000`

#### Frontend - Vercel/Netlify
1. Create account on Vercel or Netlify
2. Connect your GitHub repository
3. Set build settings:
   - Build command: `npm run build`
   - Publish directory: `build`
   - Root directory: `frontend`
4. Set environment variables:
   - `REACT_APP_API_URL=https://your-backend-url.railway.app`

### Option 2: Docker Deployment

#### Local Testing
```bash
# Build and run with docker-compose
docker-compose up --build

# Access:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
```

#### Production with Docker
```bash
# Build backend
cd backend
docker build -t material-selector-backend .
docker run -p 8000:8000 -e ENV=production material-selector-backend

# Build frontend
cd ../frontend
docker build -t material-selector-frontend .
docker run -p 80:80 material-selector-frontend
```

### Option 3: Cloud Platform Deployment

#### AWS/GCP/Azure
- Use the provided Dockerfiles
- Deploy backend to container service (ECS, Cloud Run, Container Apps)
- Deploy frontend to static hosting (S3, Cloud Storage, Static Web Apps)

## Mobile App (PWA)

The frontend is configured as a Progressive Web App with:
- ✅ Offline capability
- ✅ Install prompt on mobile devices
- ✅ App-like experience
- ✅ Responsive design

### PWA Installation
Users can install the app on mobile devices:
1. Visit the deployed URL in mobile browser
2. Tap "Add to Home Screen" when prompted
3. App will function like a native mobile app

## Environment Configuration

### Backend Environment Variables
```
ENV=production
PORT=8000
DATABASE_URL=optional_database_connection_string
```

### Frontend Environment Variables
```
REACT_APP_API_URL=https://your-backend-domain.com
REACT_APP_ENV=production
```

## Post-Deployment Steps

1. **Update CORS**: Update the allowed origins in `backend/main.py` with your frontend domain
2. **SSL/HTTPS**: Ensure both frontend and backend use HTTPS in production
3. **Domain Configuration**: Update environment variables with actual domain names
4. **Monitoring**: Set up application monitoring and error tracking

## Testing Deployment

1. **Frontend Tests**:
   ```bash
   cd frontend
   npm test
   npm run build
   ```

2. **Backend Tests**:
   ```bash
   cd backend
   python -m pytest  # if tests exist
   python main.py     # manual testing
   ```

3. **API Testing**:
   - Visit `https://your-backend-url/docs` for interactive API documentation
   - Test the `/health` endpoint
   - Test material recommendations

## Scaling Considerations

- **Database**: Migrate from file-based to PostgreSQL/MongoDB
- **Caching**: Add Redis for API response caching
- **CDN**: Use CloudFlare or AWS CloudFront for static assets
- **Load Balancing**: Add load balancer for multiple backend instances

## Security Checklist

- [ ] HTTPS enabled on both frontend and backend
- [ ] CORS properly configured with specific domains
- [ ] API rate limiting implemented
- [ ] Environment variables secured
- [ ] Error messages don't expose sensitive information

## Support

For deployment issues:
1. Check application logs
2. Verify environment variables
3. Test API endpoints individually
4. Check CORS configuration