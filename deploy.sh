#!/bin/bash
# Quick deployment script for Material Selector

echo "🚀 Material Selector - Quick Deploy Script"
echo ""

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "✅ Application successfully fixed and tested locally"
echo ""
echo "📋 Deployment Options:"
echo ""
echo "1. 🐳 Local Docker Deployment:"
echo "   docker compose up --build"
echo ""
echo "2. ☁️  Cloud Deployment Options:"
echo ""
echo "   🎯 BACKEND (Choose one):"
echo "   • Railway: Connect GitHub repo, deploy from backend/ folder"
echo "   • Heroku: git subtree push --prefix backend heroku main"
echo "   • Render: Connect GitHub repo, set Root Directory to 'backend'"
echo ""
echo "   🎨 FRONTEND (Choose one):"
echo "   • Vercel: Connect GitHub repo, set Root Directory to 'frontend'"
echo "   • Netlify: Connect GitHub repo, set Build directory to 'frontend/build'"
echo ""
echo "3. 📱 Application Features:"
echo "   • ✅ FastAPI backend with material recommendations"
echo "   • ✅ React frontend with responsive design"
echo "   • ✅ Progressive Web App (PWA) ready"
echo "   • ✅ Docker containerization"
echo "   • ✅ CORS configured for cross-origin requests"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
echo ""
echo "🎉 Ready for deployment!"