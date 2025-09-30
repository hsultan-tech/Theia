# 🚀 Deployment Guide for Theia

This guide covers multiple deployment options for the Theia AI-powered ocular disease detection application.

## 🌐 Vercel Deployment (Recommended for Frontend)

Vercel is perfect for deploying Theia as it handles the serverless architecture automatically.

### Prerequisites
- [Vercel CLI](https://vercel.com/cli) installed globally
- GitHub account connected to Vercel
- Node.js installed on your machine

### Quick Deploy

#### Option 1: Deploy via GitHub (Recommended)

1. **Push your code to GitHub** (already done!)
   ```bash
   # Your code is already on GitHub at:
   # https://github.com/hsultan-tech/Theia
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub
   - Click "New Project"
   - Import your `hsultan-tech/Theia` repository
   - Vercel will auto-detect the configuration

3. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy automatically
   - Your app will be live at `https://your-project-name.vercel.app`

#### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from your project directory**
   ```bash
   cd /path/to/Theia-main
   vercel
   ```

4. **Follow the prompts**
   - Choose your scope (personal/team)
   - Confirm project settings
   - Deploy!

### Configuration Files

The following files have been created for Vercel deployment:

- **`vercel.json`**: Main configuration file
- **`api/index.py`**: Serverless Flask application
- **`api/requirements.txt`**: Python dependencies for serverless functions

### Environment Variables

If you need environment variables:

1. **Via Vercel Dashboard**
   - Go to your project settings
   - Navigate to "Environment Variables"
   - Add variables as needed

2. **Via CLI**
   ```bash
   vercel env add VARIABLE_NAME
   ```

### Custom Domain

To use a custom domain:

1. Go to your project dashboard on Vercel
2. Navigate to "Settings" → "Domains"
3. Add your custom domain
4. Configure DNS settings as instructed

## 🐳 Docker Deployment

### Build Docker Image

```bash
# Create Dockerfile (if not exists)
cat > Dockerfile << EOF
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]
EOF

# Build image
docker build -t theia-app .

# Run container
docker run -p 5001:5001 theia-app
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  theia:
    build: .
    ports:
      - "5001:5001"
    environment:
      - FLASK_ENV=production
```

## ☁️ Heroku Deployment

Your app is already configured for Heroku with the `Procfile`.

```bash
# Install Heroku CLI
# Create Heroku app
heroku create your-theia-app

# Deploy
git push heroku main

# Open app
heroku open
```

## 🖥️ Traditional Server Deployment

### Using Gunicorn

```bash
# Install gunicorn (already in requirements.txt)
pip install gunicorn

# Run with gunicorn
gunicorn --bind 0.0.0.0:5001 app:app

# Or with more workers
gunicorn --workers 4 --bind 0.0.0.0:5001 app:app
```

### Using Nginx (Production)

```nginx
# /etc/nginx/sites-available/theia
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/theia/static;
    }
}
```

## 🔧 Environment-Specific Configurations

### Production Settings

Create a `config.py` file:

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## 📊 Monitoring and Analytics

### Add Analytics (Optional)

Add to your base template:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

## 🚨 Important Notes

### Medical Application Considerations

- **HIPAA Compliance**: Ensure your deployment meets healthcare data requirements
- **SSL/HTTPS**: Always use HTTPS in production (Vercel provides this automatically)
- **Data Privacy**: No patient data should be stored or transmitted to servers
- **Backup**: Regularly backup your model files and configurations

### Performance Optimization

- **CDN**: Vercel provides global CDN automatically
- **Caching**: Configure appropriate cache headers for static assets
- **Compression**: Enable gzip compression (automatic on Vercel)

## 🔍 Troubleshooting

### Common Issues

1. **Static Files Not Loading**
   - Check `vercel.json` routes configuration
   - Ensure static folder structure is correct

2. **Python Dependencies**
   - Verify `api/requirements.txt` has all dependencies
   - Check Python version compatibility

3. **Template Not Found**
   - Verify template folder path in `api/index.py`
   - Check file permissions

### Getting Help

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- **GitHub Issues**: Report issues in the repository

---

## 🎉 Quick Start Summary

For the fastest deployment to Vercel:

1. Push code to GitHub ✅ (Done!)
2. Connect GitHub to Vercel
3. Import repository
4. Deploy!

Your Theia application will be live and accessible worldwide in minutes!
