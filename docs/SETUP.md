# Development Setup Guide

Complete guide for setting up the CEANAPSE donation platform development environment.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Database Setup](#database-setup)
4. [Running the Application](#running-the-application)
5. [Common Issues](#common-issues)

## Prerequisites

### Required Software
- **Python 3.10+**: [Download here](https://www.python.org/downloads/)
- **Git**: [Download here](https://git-scm.com/downloads)
- **Code Editor**: VS Code (recommended) or PyCharm
- **Web Browser**: Chrome or Firefox (for testing)

### Optional (for Production)
- **PostgreSQL 15+**: [Download here](https://www.postgresql.org/download/)
- **Docker**: [Download here](https://www.docker.com/get-started) (for database)

### Verify Installations
```bash
python --version    # Should show 3.10 or higher
git --version       # Should show installed version
```

---

## Initial Setup

### 1. Clone Repository
```bash
# Clone the repository
git clone https://github.com/your-org/ceanapse-donation-platform.git
cd ceanapse-donation-platform

# Verify you're on the develop branch
git branch
git checkout develop
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:** Your terminal should show `(venv)` at the beginning.

### 3. Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### 4. Configure Environment Variables
```bash
# Create .env file (if not exists)
cp .env.example .env

# Edit .env with your text editor
# For now, you can leave defaults for development
```

---

## Database Setup

### Option A: SQLite (Default - Easiest for Development)

SQLite is already configured and requires no setup!
```bash
# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Enter username, email, and password when prompted
```

### Option B: PostgreSQL (For Production-like Environment)

**Install PostgreSQL:**
- Windows: Download installer from postgresql.org
- Mac: `brew install postgresql`
- Linux: `sudo apt-get install postgresql`

**Create Database:**
```bash
# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE ceanapse_db;

# Create user (optional)
CREATE USER ceanapse_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ceanapse_db TO ceanapse_user;

# Exit
\q
```

**Update .env:**
```env
DB_ENGINE=postgresql
DB_NAME=ceanapse_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

**Install PostgreSQL adapter:**
```bash
pip install psycopg2-binary
pip freeze > requirements.txt
```

**Run migrations:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Running the Application

### Start Development Server
```bash
# Make sure virtual environment is activated
python manage.py runserver

# Server will start at http://127.0.0.1:8000
```

### Access the Application

- **Main Site**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin
- **Login**: Use the superuser credentials you created

### Stop the Server

Press `CTRL + C` in the terminal

---

## Development Workflow

### Before Starting Work
```bash
# 1. Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 2. Update your local develop branch
git checkout develop
git pull origin develop

# 3. Create feature branch
git checkout -b feature/your-feature-name
```

### While Working
```bash
# Run server
python manage.py runserver

# In another terminal, run migrations if you change models
python manage.py makemigrations
python manage.py migrate

# Collect static files if needed
python manage.py collectstatic --noinput
```

### After Completing Feature
```bash
# 1. Add and commit changes
git add .
git commit -m "Descriptive commit message"

# 2. Push to GitHub
git push origin feature/your-feature-name

# 3. Create Pull Request on GitHub to 'develop' branch

# 4. Request review from Dev 3 (Ismael)
```

---

## Common Issues & Solutions

### Issue: "pip is not recognized"

**Solution:**
```bash
# Windows
python -m pip install --upgrade pip

# Mac/Linux
python3 -m pip install --upgrade pip
```

### Issue: "python manage.py: No such file or directory"

**Solution:** Make sure you're in the project root directory:
```bash
cd ceanapse-donation-platform
ls  # You should see manage.py
```

### Issue: Virtual environment not activating

**Windows Solution:**
```bash
# If activation is restricted
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**Mac/Linux Solution:**
```bash
# Make sure script is executable
chmod +x venv/bin/activate
source venv/bin/activate
```

### Issue: "Port 8000 is already in use"

**Solution:**
```bash
# Find and kill process using port 8000
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9

# Or use different port
python manage.py runserver 8001
```

### Issue: Database locked (SQLite)

**Solution:**
```bash
# Close all other terminals/processes accessing the database
# Or delete db.sqlite3 and run migrations again
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Module not found error

**Solution:**
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

---

## IDE Setup (VS Code Recommended)

### Recommended Extensions
1. **Python** (Microsoft)
2. **Django** (Baptiste Darthenay)
3. **GitLens**
4. **Prettier** (for HTML/CSS/JS)

### VS Code Settings

Create `.vscode/settings.json`:
```json
{
    "python.pythonPath": "venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

---

## Testing Your Setup

Run these commands to verify everything works:
```bash
# 1. Check Django installation
python manage.py --version

# 2. Run checks
python manage.py check

# 3. Test database connection
python manage.py showmigrations

# 4. Start server
python manage.py runserver

# 5. Visit http://127.0.0.1:8000 in browser
# You should see Django welcome page or your landing page
```

---

## Getting Help

1. **Check this documentation first**
2. **Search for error messages online** (Stack Overflow)
3. **Ask in team chat** (don't struggle alone!)
4. **Contact Dev 3 (Ismael)** for setup issues
5. **Create GitHub issue** for bugs

---

## Next Steps

After setup:
1. ✅ Read [API Documentation](API.md)
2. ✅ Review project structure in main README
3. ✅ Start working on your assigned features
4. ✅ Follow Git workflow for all changes

**Happy coding! 🚀**