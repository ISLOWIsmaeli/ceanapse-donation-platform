
## 3. Step-by-Step Branching Guide

### For Dev 1 (Makana) - Frontend Lead

#### Task 1: Landing Page Structure (Week 1, Days 1-3)
```bash
# Step 1: Start from develop
git checkout develop
git pull origin develop

# Step 2: Create feature branch
git checkout -b feature/landing-page-structure

# Step 3: Do your work
# - Edit files in frontend/ folder
# - Create HTML templates
# - Add CSS styling

# Step 4: Commit your changes
git add .
git commit -m "Add landing page structure with navigation and hero section"

# Step 5: Push to GitHub
git push origin feature/landing-page-structure

# Step 6: Create Pull Request on GitHub
# - Go to GitHub repository
# - Click "Compare & pull request"
# - Base: develop ← Compare: feature/landing-page-structure
# - Add description of what you did
# - Request review from Dev 3 (Ismael)
# - Wait for approval

# Step 7: After merge, start next task
git checkout develop
git pull origin develop
git checkout -b feature/donation-form-ui
# Repeat process...
```

#### Task 2: Donation Form UI (Week 1, Days 4-5)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/donation-form-ui

# Work on donation form
# - Create form HTML
# - Add JavaScript validation
# - Style the form

git add .
git commit -m "Create donation form with client-side validation"
git push origin feature/donation-form-ui
# Create PR → Request review → Merge
```

#### Task 3: Response Pages (Week 2, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/response-pages

# Work on success and error pages
git add .
git commit -m "Add success and failure response pages"
git push origin feature/response-pages
# Create PR → Request review → Merge
```

#### Task 4: Landing Page Content (Week 2, Days 3-4)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/landing-page-content

# Add CEANAPSE story, leader profiles, etc.
git add .
git commit -m "Add mission statement and leader profiles"
git push origin feature/landing-page-content
# Create PR → Request review → Merge
```

#### Task 5: Final Polish (Week 3, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/frontend-polish

# Mobile testing, bug fixes, optimization
git add .
git commit -m "Final responsive design and browser compatibility fixes"
git push origin feature/frontend-polish
# Create PR → Request review → Merge
```

---

### For Dev 2 (Alphonce) - Backend Lead

#### Task 1: Donation Model (Week 1, Days 2-3)
```bash
# Step 1: Start from develop
git checkout develop
git pull origin develop

# Step 2: Create feature branch
git checkout -b feature/donation-model

# Step 3: Create the model
# Edit donations/models.py
# Create model with all fields

# Step 4: Create migrations
python manage.py makemigrations
python manage.py migrate

# Step 5: Test the model
python manage.py shell
# >>> from donations.models import Donation
# >>> Donation.objects.create(...)

# Step 6: Commit
git add .
git commit -m "Add Donation model with all required fields"
git push origin feature/donation-model

# Step 7: Create PR on GitHub to develop branch
# Request review from Dev 3
```

#### Task 2: Paystack Service (Week 1, Days 4-5)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/paystack-service

# Create donations/services/paystack.py
# Add initialize_payment() function
# Add verify_payment() function

git add .
git commit -m "Add Paystack service class for payment integration"
git push origin feature/paystack-service
# Create PR → Request review → Merge
```

#### Task 3: Payment Initiation (Week 2, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/payment-initiation

# Create view in donations/views.py
# Handle form submission
# Call Paystack API
# Return authorization URL

git add .
git commit -m "Add payment initiation endpoint"
git push origin feature/payment-initiation
# Create PR → Request review → Merge
```

#### Task 4: Payment Verification (Week 2, Days 3-4)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/payment-verification

# Create callback view
# Verify payment with Paystack
# Update database

git add .
git commit -m "Add payment verification and callback handling"
git push origin feature/payment-verification
# Create PR → Request review → Merge
```

#### Task 5: Webhook Handler (Week 2, Day 5)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/payment-webhook

# Create webhook endpoint
# Verify signature
# Update transaction status

git add .
git commit -m "Add Paystack webhook handler"
git push origin feature/payment-webhook
# Create PR → Request review → Merge
```

#### Task 6: Testing (Week 3, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/payment-testing

# Add tests, handle edge cases
git add .
git commit -m "Add comprehensive payment testing and error handling"
git push origin feature/payment-testing
# Create PR → Request review → Merge
```

---

### For Dev 3 (Ismael - YOU) - Backend Support

#### Task 1: Initial Setup (Week 1, Day 1 - Already Done!)
```bash
# This was done directly on main, then merged to develop
# No feature branch needed for initial setup
```

#### Task 2: Environment Config (Week 1, Day 2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/environment-config

# Configure settings.py
# Set up .env handling
# Configure static files, email, etc.

git add .
git commit -m "Configure environment variables and Django settings"
git push origin feature/environment-config
# Create PR → Self-review → Merge (you're the lead!)
```

#### Task 3: Base Templates (Week 1, Days 3-4)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/base-templates

# Create templates/base.html
# Create email templates
# Set up template inheritance

git add .
git commit -m "Add base template structure and email templates"
git push origin feature/base-templates
# Create PR → Merge
```

#### Task 4: Email Notifications (Week 2, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/email-notifications

# Create core/email_service.py
# Create email sending functions
# Create HTML email templates

git add .
git commit -m "Add email notification system for donations"
git push origin feature/email-notifications
# Create PR → Merge
```

#### Task 5: Admin Customization (Week 2, Days 3-4)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/admin-customization

# Edit donations/admin.py
# Add filters, search, custom display

git add .
git commit -m "Customize Django admin for donation management"
git push origin feature/admin-customization
# Create PR → Merge
```

#### Task 6: Transaction Logging (Week 2, Day 5)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/transaction-logging

# Add logging throughout app
# Create log viewing interface

git add .
git commit -m "Add comprehensive transaction logging"
git push origin feature/transaction-logging
# Create PR → Merge
```

#### Task 7: Admin Dashboard (Week 3, Days 1-2)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/admin-dashboard

# Create custom admin dashboard
# Add statistics views

git add .
git commit -m "Add admin dashboard with donation statistics"
git push origin feature/admin-dashboard
# Create PR → Merge
```

#### Task 8: Deployment (Week 3, Days 3-5)
```bash
git checkout develop
git pull origin develop
git checkout -b feature/deployment-config

# Add gunicorn config
# Add nginx config files
# Add deployment scripts

git add .
git commit -m "Add production deployment configuration"
git push origin feature/deployment-config
# Create PR → Merge

# After merge to develop, merge develop to main for production
git checkout main
git merge develop
git push origin main
```

---

## 4. Integration Points (When Developers Need Each Other)

### Integration 1: Frontend + Backend Models (Week 1 End)

**Dependency:** Dev 1 needs to know what fields the donation form should have

**Process:**
1. Dev 2 finishes `feature/donation-model` first (Week 1, Days 2-3)
2. Dev 2 creates PR and gets it merged to `develop`
3. Dev 1 pulls `develop` to see the model structure
4. Dev 1 creates form fields matching the model
5. Dev 3 creates base templates that both can use

**Communication:**
```
Dev 2: "I've merged the Donation model. Fields are: donor_name, donor_email, donor_phone, amount"
Dev 1: "Perfect! I'll create the form with those exact fields"
Dev 3: "I'll create the base template for both of you to extend"
```

### Integration 2: Form Submission + Payment API (Week 2, Days 1-2)

**Dependency:** Dev 1's form needs to submit to Dev 2's API endpoint

**Process:**
1. Dev 2 creates payment initiation endpoint first
2. Dev 2 documents the endpoint (what data it expects, what it returns)
3. Dev 2 merges to `develop`
4. Dev 1 pulls `develop`
5. Dev 1 updates form submission JavaScript to call the endpoint

**Communication:**
```
Dev 2: "Payment endpoint ready at /api/donations/initiate/
        Send: {donor_name, donor_email, donor_phone, amount}
        Returns: {authorization_url, reference}"
Dev 1: "Got it! I'll submit the form there and redirect to authorization_url"
```

### Integration 3: Email After Payment (Week 2, Days 3-4)

**Dependency:** Dev 2 needs to trigger Dev 3's email service

**Process:**
1. Dev 3 creates email service first
2. Dev 3 provides function signature: `send_donation_email(donation_id)`
3. Dev 3 merges to `develop`
4. Dev 2 pulls `develop`
5. Dev 2 calls email function after successful payment verification

**Communication:**
```
Dev 3: "Email service ready in core/email_service.py
        Call: send_donation_email(donation_object)
        It handles everything automatically"
Dev 2: "Perfect! I'll call it after payment verification"
```

---

## 5. Daily Workflow Example

### Dev 1's Typical Day
```bash
# Morning (9:00 AM)
git checkout develop
git pull origin develop  # Get latest changes from team

# Check if dependencies ready
git log --oneline  # See what's been merged

# Start your work
git checkout -b feature/your-task
# Code, code, code...

# Afternoon (3:00 PM)
git add .
git commit -m "Progress on feature"
git push origin feature/your-task  # Backup your work

# End of day (5:00 PM)
git add .
git commit -m "Complete feature X"
git push origin feature/your-task
# Create PR on GitHub
```

### Dev 2's Typical Day
```bash
# Morning (9:00 AM)
git checkout develop
git pull origin develop

# Check what frontend needs from you
# Start your API endpoint
git checkout -b feature/payment-endpoint

# Test your endpoint
python manage.py runserver
# Use Postman or curl to test

# Afternoon
git add .
git commit -m "Add payment endpoint with tests"
git push origin feature/payment-endpoint
# Create PR

# Communicate with team
"@Dev1 Payment endpoint ready for testing!"
```

### Dev 3's Typical Day (YOU)
```bash
# Morning (9:00 AM)
git checkout develop
git pull origin develop

# Review PRs from Dev 1 and Dev 2
# Go to GitHub → Pull Requests tab
# Review code, test locally if needed
# Approve and merge to develop

# Your own work
git checkout -b feature/email-service
# Work on your feature

# Afternoon - More PR reviews
# Test integration between features
python manage.py runserver
# Test that form submission → payment → email all work together

# Communication
"@team Latest changes merged to develop. Please pull before continuing"
```

---

## 6. Rules to Avoid Conflicts

### Rule 1: File Ownership

**Clear boundaries prevent conflicts:**

| Developer | Primary Files | Don't Touch |
|-----------|---------------|-------------|
| **Dev 1** | `frontend/`, `templates/pages/` | `donations/models.py`, `donations/views.py` |
| **Dev 2** | `donations/models.py`, `donations/views.py`, `donations/services/` | `frontend/`, `administration/` |
| **Dev 3** | `config/settings.py`, `administration/`, `core/`, deployment files | `donations/views.py`, `frontend/assets/` |

**Exception:** You can all edit `templates/` but coordinate!

### Rule 2: Always Pull Before Creating Branch
```bash
# WRONG ❌
git checkout -b feature/my-feature  # Might be outdated!

# CORRECT ✅
git checkout develop
git pull origin develop  # Get latest
git checkout -b feature/my-feature  # Now you're up to date
```

### Rule 3: Small, Focused Commits
```bash
# WRONG ❌
git commit -m "Fixed stuff"  # What stuff?

# CORRECT ✅
git commit -m "Add email validation to donation form"
git commit -m "Style donation button with hover effect"
```

### Rule 4: One Feature = One Branch
```bash
# WRONG ❌
feature/everything  # Doing multiple things in one branch

# CORRECT ✅
feature/donation-form-ui  # Just the form UI
feature/form-validation   # Just the validation
```

### Rule 5: Merge Develop Often
```bash
# If your feature takes multiple days:
# Day 1
git checkout feature/my-long-feature
# Code...
git commit -m "Progress on day 1"

# Day 2 - Get latest changes from team
git checkout develop
git pull origin develop
git checkout feature/my-long-feature
git merge develop  # Bring in team's changes
# Continue coding...
```

---

## 7. Handling Merge Conflicts (If They Happen)

### What's a Merge Conflict?

When two people edit the same line in the same file.

**Example:**
- Dev 1 edits line 10 in `style.css`
- Dev 2 also edits line 10 in `style.css`
- Git doesn't know which change to keep

### How to Resolve:
```bash
# You try to merge and see:
git merge develop
# CONFLICT (content): Merge conflict in style.css

# Open style.css, you'll see:
<<<<<<< HEAD
background-color: blue;  # Your change
=======
background-color: red;   # Their change
>>>>>>> develop

# Choose which to keep (or keep both):
background-color: blue;

# Save file, then:
git add style.css
git commit -m "Resolve merge conflict in style.css"
```

### Best Way to Avoid Conflicts:

1. **Communicate**: "I'm working on style.css today"
2. **Small branches**: Merge often, don't wait days
3. **File ownership**: Stick to your assigned files

---

## 8. Quick Reference Commands

### Starting New Feature
```bash
git checkout develop
git pull origin develop
git checkout -b feature/feature-name
```

### Saving Progress (Daily)
```bash
git add .
git commit -m "Descriptive message"
git push origin feature/feature-name
```

### Creating Pull Request

1. Go to GitHub repository
2. Click "Pull requests" → "New pull request"
3. Base: `develop` ← Compare: `feature/feature-name`
4. Add title and description
5. Request review from Dev 3 (Ismael)
6. Click "Create pull request"

### After PR is Merged
```bash
git checkout develop
git pull origin develop
git branch -d feature/old-feature  # Delete old branch
```

### Getting Team's Latest Changes
```bash
git checkout develop
git pull origin develop
```

### Checking What Branch You're On
```bash
git branch
# * feature/my-feature  ← You're here
#   develop
#   main
```

---

## 9. Communication Flow

### Daily Standup (9:00 AM - 15 minutes)

**Format:**
```
Dev 1: "Yesterday: Finished landing page structure. 
        Today: Working on donation form UI. 
        Blockers: Need to know form field names"

Dev 2: "Yesterday: Created donation model, merged to develop. 
        Today: Starting Paystack integration. 
        Blockers: None. 
        Note: @Dev1 form fields are in donations/models.py"

Dev 3: "Yesterday: Set up project, reviewed PRs. 
        Today: Working on email templates. 
        Blockers: None. 
        Note: Everyone pull develop before starting today"
```

### Slack/WhatsApp Messages
```
# When you finish a feature
"✅ Merged feature/donation-model to develop. Everyone please pull!"

# When you need help
"🆘 Having issues with Paystack API. @Dev3 can you take a look?"

# When you're blocked
"⏸️ Waiting for payment endpoint before I can continue. @Dev2 ETA?"

# When you push changes
"📤 Pushed progress on feature/email-service, not ready for PR yet"
```

---

## 10. Visual Workflow Diagram
```
Week 1:
Dev 1: [Setup] → [Landing Page] → [Form UI] ────────────┐
Dev 2: [Setup] → [Model] ────────→ [Paystack Service] ──┤→ [Integration Testing]
Dev 3: [Setup] → [Config] → [Templates] ────────────────┘

Week 2:
Dev 1: [Response Pages] → [Content] ────────────────────┐
Dev 2: [Payment Init] → [Verification] → [Webhook] ─────┤→ [Integration Testing]
Dev 3: [Emails] → [Admin] ──────────────────────────────┘

Week 3:
Dev 1: [Polish] → [Testing] ────────────────────────────┐
Dev 2: [Testing] → [Bug Fixes] ─────────────────────────┤→ [Deployment]
Dev 3: [Dashboard] → [Deployment] → [Production] ───────┘
```

---

## Summary

### Dev 1 (Makana) - 5 Branches:
1. `feature/landing-page-structure`
2. `feature/donation-form-ui`
3. `feature/response-pages`
4. `feature/landing-page-content`
5. `feature/frontend-polish`

### Dev 2 (Alphonce) - 6 Branches:
1. `feature/donation-model`
2. `feature/paystack-service`
3. `feature/payment-initiation`
4. `feature/payment-verification`
5. `feature/payment-webhook`
6. `feature/payment-testing`

### Dev 3 (Ismael - YOU) - 7 Branches:
1. ~~Initial setup~~ (already done on main)
2. `feature/environment-config`
3. `feature/base-templates`
4. `feature/email-notifications`
5. `feature/admin-customization`
6. `feature/transaction-logging`
7. `feature/admin-dashboard`
8. `feature/deployment-config`

### Key Principles:
✅ Always branch from `develop`  
✅ Always pull before creating new branch  
✅ One feature = One branch  
✅ Small, frequent commits  
✅ Create PR to `develop` (not `main`)  
✅ Dev 3 reviews all PRs  
✅ Communicate daily  
✅ Test after each merge
