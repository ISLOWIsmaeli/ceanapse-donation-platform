# CEANAPSE Online Donation Platform

A secure and user-friendly web platform that enables supporters to make monetary donations to CEANAPSE projects through Paystack payment gateway.

## 🎯 Project Overview

**Project CEANAPSE** is an online donation platform designed to:
- Provide a simple donation interface for users
- Process secure payments via Paystack
- Log all transactions in a database
- Send email confirmations to donors
- Provide admin dashboard for transaction monitoring

## 👥 Development Team

- **Dev 1 (Makana)**: Frontend Lead - Landing page, donation forms, UI/UX
- **Dev 2 (Alphonce)**: Backend Lead - Paystack integration, payment processing
- **Dev 3 (Ismael)**: Backend Support - Admin dashboard, email notifications, deployment

## 🛠️ Tech Stack

- **Backend**: Django 5.1 (Python)
- **Database**: SQLite (Development) → PostgreSQL (Production)
- **Payment**: Paystack API
- **Frontend**: HTML5, CSS3, JavaScript
- **Hosting**: DigitalOcean
- **Domain**: Namecheap

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Git
- Virtual environment tool

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/ISLOWIsmaeli/ceanapse-donation-platform.git
   cd ceanapse-donation-platform
```

2. **Create and activate virtual environment**
```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run database migrations**
```bash
   python manage.py migrate
```

5. **Create a superuser (admin account)**
```bash
   python manage.py createsuperuser
```

6. **Run the development server**
```bash
   python manage.py runserver
```

7. **Access the application**
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## 📁 Project Structure
```
ceanapse-donation-platform/
├── config/              # Django project settings
    ├── templates/           # Django HTML templates
    ├── static/              # Static files (CSS, JS, images) 
├── donations/           # Donations app (models, views, payment logic)
├── administration/      # Admin customization and dashboard
├── docs/                # Project documentation (please ignore for now)
└── manage.py            # Django management script
```

## 📚 Documentation (IGNORE FOR NOW WILL UPDATE WITH TIME)

- [Setup Guide](docs/SETUP.md) - Detailed development environment setup
- [API Documentation](docs/API.md) - API endpoints and usage
- [Deployment Guide](docs/DEPLOYMENT.md) - Production deployment instructions
- [SpoonFeeding Guide](docs/spoonFeeding.md) - Baby steps instructions

## 🔄 Git Workflow

1. **Always work on feature branches**
```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
```

2. **Commit your changes**
```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
```

3. **Create Pull Request**
   - Go to GitHub
   - Create PR from your feature branch to `develop`
   - Request review from Dev 3 (Ismael)
   - Wait for approval before merging

## 🌿 Branch Structure

- `main` - Production-ready code
- `develop` - Integration branch (main working branch)
- `feature/*` - Feature branches (create from develop)
- `bugfix/*` - Bug fix branches
- `hotfix/*` - Critical production fixes

## ⚙️ Environment Variables

Create a `.env` file in the root directory (copy from `.env.example` when available):
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Add Paystack keys when ready
PAYSTACK_SECRET_KEY=sk_test_xxx
PAYSTACK_PUBLIC_KEY=pk_test_xxx
```

## 🧪 Running Tests
```bash
python manage.py test
```

## 📝 Development Timeline

- **Week 1**: Setup, database models, basic structure
- **Week 2**: Payment integration, frontend development
- **Week 3**: Testing, deployment, documentation

## 🤝 Contributing

1. Create your feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request to `develop` branch

## 📞 Support

For questions or issues:
- Create an issue in GitHub
- Contact Dev 3 (Ismael) - Project Lead
- Check documentation in `/docs` folder

## 📄 License

This project is proprietary and confidential. All rights reserved by CEANAPSE.

---

**Built with ❤️ by the KIJIJI Development Team**