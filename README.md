# 👁️ Theia - AI-Powered Ocular Disease Detection

<div align="center">

![Theia Logo](static/images/theia.png)

**An intelligent web application that empowers optometrists to identify ocular diseases using advanced computer vision and machine learning.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)](https://flask.palletsprojects.com/)
[![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-Latest-orange.svg)](https://www.tensorflow.org/js)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[🚀 Live Demo](https://theiaocular.herokuapp.com/) • [📖 Documentation](#documentation) • [🤝 Contributing](#contributing)

</div>

## 🌟 Overview

Theia is a cutting-edge web application designed to assist optometrists and eye care professionals in the early detection and diagnosis of ocular diseases. Using state-of-the-art machine learning models and computer vision techniques, Theia analyzes retinal images to identify various eye conditions with high accuracy.

### 🎯 Mission
To democratize access to advanced eye care diagnostics and help reduce the global burden of preventable blindness through AI-powered early detection.

## ✨ Features

### 🔬 **AI-Powered Diagnosis**
- **Multi-Disease Detection**: Identifies 7+ different ocular conditions
- **Real-time Analysis**: Instant results with confidence scores
- **High Accuracy**: Trained on extensive medical datasets
- **Professional Grade**: Designed for clinical environments

### 🏥 **Supported Conditions**
- 🩺 **Diabetic Retinopathy** - Early detection of diabetes-related eye damage
- 👁️ **Glaucoma** - Identification of optic nerve damage
- 🌫️ **Cataract** - Detection of lens opacity
- 🎯 **Age-related Macular Degeneration (AMD)** - Central vision deterioration
- 💓 **Hypertensive Retinopathy** - High blood pressure eye effects
- 🔍 **Pathological Myopia** - Severe nearsightedness complications
- ✅ **Normal Eyes** - Healthy eye identification
- 🔬 **Other Abnormalities** - Detection of various other conditions

### 🖥️ **User Experience**
- **Intuitive Interface**: Clean, modern design optimized for medical professionals
- **Interactive Visualizations**: Real-time charts showing probability distributions
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Fast Processing**: Optimized for quick diagnosis in clinical settings

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser with JavaScript enabled
- 2GB+ RAM recommended

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hsultan-tech/Theia.git
   cd Theia
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv theiaenv
   
   # On macOS/Linux:
   source theiaenv/bin/activate
   
   # On Windows:
   theiaenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5001`

## 📱 Usage Guide

### Getting Started
1. **Home Page**: Learn about Theia's capabilities and mission
2. **Click "Get Started"**: Navigate to the diagnosis interface
3. **Upload Image**: Select a retinal image using the "Custom Upload" button
4. **Analyze**: Click "Predict" to run the AI analysis
5. **Review Results**: Examine the probability chart and diagnosis

### Supported Image Formats
- **JPEG/JPG** - Recommended for retinal photography
- **PNG** - High quality images
- **GIF** - Basic support
- **WebP** - Modern format support

### Best Practices
- Use high-resolution retinal images (512x512px minimum)
- Ensure proper lighting and focus in source images
- Center the optic disc and macula when possible
- Use images from standard fundus cameras when available

## 🏗️ Architecture

### Technology Stack
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **AI/ML**: TensorFlow.js for client-side inference
- **Visualization**: Chart.js for interactive charts
- **Styling**: Custom CSS with responsive design
- **Deployment**: Gunicorn WSGI server

### Project Structure
```
Theia/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── .gitignore            # Git ignore rules
├── static/               # Static assets
│   ├── images/           # UI images and icons
│   ├── styles/           # CSS stylesheets
│   ├── javascript/       # Client-side scripts
│   └── theiamodel/       # AI model files
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   └── identify.html     # Diagnosis interface
└── data_preprocessing.ipynb  # Model training notebook
```

## 🧠 AI Model Details

### Model Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Input Size**: 224x224 pixels, RGB
- **Output**: 8-class probability distribution
- **Deployment**: TensorFlow.js for browser-based inference

### Training Data
- Curated dataset of retinal images from medical institutions
- Balanced representation across all condition classes
- Rigorous data validation and quality control
- Compliance with medical imaging standards

### Performance Metrics
- **Accuracy**: 90%+ on validation dataset
- **Sensitivity**: High detection rate for critical conditions
- **Specificity**: Low false positive rate
- **Inference Time**: <2 seconds on modern hardware

## 🌐 Deployment

### Local Development
```bash
# Development server (debug mode)
python app.py
```

### Production Deployment

#### Vercel (Recommended)
The easiest way to deploy Theia:

```bash
# Option 1: Deploy via GitHub (Recommended)
# 1. Go to vercel.com and connect your GitHub
# 2. Import the hsultan-tech/Theia repository
# 3. Deploy automatically!

# Option 2: Deploy via CLI
npm install -g vercel
vercel login
vercel
```

**Live in minutes!** Vercel automatically handles:
- ✅ Serverless deployment
- ✅ Global CDN
- ✅ HTTPS certificates
- ✅ Automatic builds from GitHub

#### Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

#### Docker
```dockerfile
# Dockerfile example
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
```

#### Traditional Server
```bash
# Using Gunicorn
gunicorn --bind 0.0.0.0:5001 app:app
```

## 🔒 Privacy & Security

### Data Protection
- **No Data Storage**: Images are processed locally in the browser
- **HIPAA Considerations**: No patient data leaves the client device
- **Secure Transmission**: HTTPS encryption for all communications
- **Privacy by Design**: Minimal data collection principles

### Medical Disclaimer
⚠️ **Important**: Theia is designed as a diagnostic aid tool and should not replace professional medical judgment. All results should be reviewed by qualified healthcare professionals before making clinical decisions.

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Areas for Contribution
- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **New Features**: Enhance functionality
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Testing**: Add test coverage
- 🎨 **UI/UX**: Design improvements
- 🔬 **Model Enhancement**: Improve AI accuracy

## 📊 Roadmap

### Version 2.0 (Planned)
- [ ] Additional disease classifications
- [ ] Batch processing capabilities
- [ ] Advanced reporting features
- [ ] Integration with EMR systems
- [ ] Mobile app development
- [ ] Multi-language support

### Version 2.1 (Future)
- [ ] 3D visualization of retinal structures
- [ ] Longitudinal analysis capabilities
- [ ] Telemedicine integration
- [ ] Advanced analytics dashboard

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Medical Advisors**: Thanks to the optometrists and ophthalmologists who provided clinical guidance
- **Dataset Contributors**: Appreciation for the medical institutions that provided training data
- **Open Source Community**: Built with amazing open-source tools and libraries
- **TensorFlow Team**: For providing excellent machine learning frameworks

## 📞 Support & Contact

### Getting Help
- 📖 **Documentation**: Check our comprehensive guides
- 🐛 **Issues**: Report bugs on GitHub Issues
- 💬 **Discussions**: Join our community discussions
- 📧 **Email**: Contact the development team

### Links
- **Live Application**: [https://theiaocular.herokuapp.com/](https://theiaocular.herokuapp.com/)
- **GitHub Repository**: [https://github.com/hsultan-tech/Theia](https://github.com/hsultan-tech/Theia)
- **Documentation**: [Coming Soon]

---

<div align="center">

**Made with ❤️ for better eye care worldwide**

*Theia - Helping Others See The World, Crystal Clear*

</div>
