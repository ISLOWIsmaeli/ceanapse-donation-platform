# Deployment Guide

Complete guide for deploying CEANAPSE Donation Platform to production.

## Table of Contents
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [DigitalOcean Setup](#digitalocean-setup)
3. [Server Configuration](#server-configuration)
4. [Database Setup](#database-setup)
5. [Django Deployment](#django-deployment)
6. [Domain & SSL](#domain--ssl)
7. [Post-Deployment](#post-deployment)

---

## Pre-Deployment Checklist

### Code Preparation

- [ ] All features tested locally
- [ ] All tests passing
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] Environment variables documented
- [ ] Debug mode disabled in production settings
- [ ] Secret keys generated (not from repository)
- [ ] Paystack production keys obtained
- [ ] Email settings configured

### Required Accounts

- [ ] DigitalOcean account (for hosting)
- [ ] Namecheap account (for domain)
- [ ] Paystack account (production keys)
- [ ] Gmail/SMTP service (for emails)

---

## DigitalOcean Setup

### 1. Create Droplet

1. **Log in to DigitalOcean**
2. **Create → Droplets**
3. **Choose options:**
   - **Image**: Ubuntu 22.04 LTS
   - **Plan**: Basic ($6/month recommended for start)
   - **CPU**: Regular Intel (1 GB RAM)
   - **Datacenter**: Choose closest to Kenya (Amsterdam or Frankfurt)
   - **Authentication**: SSH Key (recommended) or Password
   - **Hostname**: `ceanapse-production`

4. **Create Droplet** and note the IP address

### 2. Initial Server Access
```bash
# SSH into server
ssh root@your_droplet_ip

# Update system
apt update && apt upgrade -y
```

---

## Server Configuration

### 1. Create Deploy User
```bash
# Create user
adduser deploy

# Add to sudo group
usermod -aG sudo deploy

# Switch to deploy user
su - deploy
```

### 2. Install Required Software
```bash
# Install Python and dependencies
sudo apt install python3.11 python3.11-venv python3-pip -y

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Install Nginx
sudo apt install nginx -y

# Install Git
sudo apt install git -y

# Install system dependencies
sudo apt install build-essential libpq-dev python3-dev -y
```

### 3. Configure Firewall
```bash
# Allow SSH, HTTP, HTTPS
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

---

## Database Setup

### 1. Create PostgreSQL Database
```bash
# Switch to postgres user
sudo -u postgres psql

# In PostgreSQL prompt:
CREATE DATABASE ceanapse_production;
CREATE USER ceanapse_user WITH PASSWORD 'STRONG_PASSWORD_HERE';
ALTER ROLE ceanapse_user SET client_encoding TO 'utf8';
ALTER ROLE ceanapse_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ceanapse_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ceanapse_production TO ceanapse_user;

# Exit
\q
```

### 2. Test Database Connection
```bash
psql -U ceanapse_user -d ceanapse_production -h localhost
# Enter password when prompted
# If successful, you'll see PostgreSQL prompt
\q
```

---

## Django Deployment

### 1. Clone Repository
```bash
# As deploy user
cd /home/deploy
git clone https://github.com/your-org/ceanapse-donation-platform.git
cd ceanapse-donation-platform
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3.11 -m venv venv

# Activate
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install production dependencies
pip install -r requirements.txt
pip install gunicorn
```

### 3. Configure Environment Variables
```bash
# Create .env file
nano .env
```

Add:
```env
SECRET_KEY=GENERATE_NEW_SECRET_KEY_HERE
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,your_droplet_ip

# Database
DB_ENGINE=postgresql
DB_NAME=ceanapse_production
DB_USER=ceanapse_user
DB_PASSWORD=YOUR_DATABASE_PASSWORD
DB_HOST=localhost
DB_PORT=5432

# Email (Gmail example)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password

# Paystack PRODUCTION keys
PAYSTACK_SECRET_KEY=sk_live_xxxxx
PAYSTACK_PUBLIC_KEY=pk_live_xxxxx
PAYSTACK_WEBHOOK_SECRET=your_webhook_secret

# Site
SITE_URL=https://your-domain.com
```

Save and exit (Ctrl+X, Y, Enter)

### 4. Run Migrations and Collect Static
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 5. Test with Gunicorn
```bash
# Test gunicorn
gunicorn --bind 0.0.0.0:8000 config.wsgi

# Visit http://your_droplet_ip:8000 in browser
# Press Ctrl+C to stop
```

### 6. Create Gunicorn Service
```bash
# Create systemd service file
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=Gunicorn daemon for CEANAPSE
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/home/deploy/ceanapse-donation-platform
Environment="PATH=/home/deploy/ceanapse-donation-platform/venv/bin"
ExecStart=/home/deploy/ceanapse-donation-platform/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/deploy/ceanapse-donation-platform/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

Save and exit.
```bash
# Start and enable service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

---

## Nginx Configuration

### 1. Create Nginx Config
```bash
sudo nano /etc/nginx/sites-available/ceanapse
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/deploy/ceanapse-donation-platform/staticfiles/;
    }
    
    location /media/ {
        alias /home/deploy/ceanapse-donation-platform/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/deploy/ceanapse-donation-platform/gunicorn.sock;
    }
}
```

Save and exit.

### 2. Enable Site
```bash
# Create symbolic link
sudo ln -s /etc/nginx/sites-available/ceanapse /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

---

## Domain & SSL

### 1. Configure Domain (Namecheap)

1. **Log in to Namecheap**
2. **Go to Domain List → Manage**
3. **Advanced DNS tab**
4. **Add Records:**
   - Type: `A Record`, Host: `@`, Value: `your_droplet_ip`, TTL: Automatic
   - Type: `A Record`, Host: `www`, Value: `your_droplet_ip`, TTL: Automatic

5. **Wait 5-30 minutes for DNS propagation**

### 2. Install SSL Certificate (Let's Encrypt)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Follow prompts:
# - Enter email
# - Agree to terms
# - Choose: Redirect HTTP to HTTPS (option 2)

# Test auto-renewal
sudo certbot renew --dry-run
```

Your site should now be accessible at `https://your-domain.com` 🎉

---

## Post-Deployment

### 1. Verify Everything Works

- [ ] Visit https://your-domain.com
- [ ] Test donation form
- [ ] Make test payment (