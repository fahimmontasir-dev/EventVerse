# EventVerse 🎟️

**A Python-Based Student Event Management System**

EventVerse is a terminal-based event management application developed using Python. It allows students to discover events, register for activities, manage tickets, earn rewards, and track their participation.

The system also provides administrative features for managing events, monitoring registrations, recording attendance, and generating reports.

## ✨ Features

### Student Features
- Student account registration and login
- Email verification using a six-digit code
- Secure password hashing using PBKDF2-HMAC-SHA256
- Forgot password and email verification
- Browse available events
- Register for events and receive ticket IDs
- View and cancel registrations
- View registered event tickets
- Track attendance, rewards, points, levels, and badges

### Admin Features
- Admin login
- Create and manage events
- Edit and delete events
- View registered students
- Manage event attendance
- View system reports and analytics
- Monitor event popularity and attendance statistics

## 🛠️ Technologies Used

- Python
- JSON for data storage
- Git and GitHub for version control
- SMTP for email verification
- `python-dotenv` for environment variable management

## 📁 Project Structure

```text
EventVerse/
├── main.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── users.json
│   ├── events.json
│   ├── registrations.json
│   └── rewards.json
│
├── modules/
│   ├── user_management.py
│   ├── event_management.py
│   ├── registration.py
│   ├── ticket_management.py
│   ├── rewards.py
│   ├── analytics.py
│   └── email_service.py
│
└── utils/
    ├── helpers.py
    └── validation.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/fahimmontasir-dev/EventVerse.git
```

### 2. Navigate to the project directory

```bash
cd EventVerse
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure email verification

Create a `.env` file in the project root directory:

```env
EMAIL_ADDRESS=your_gmail_address
EMAIL_APP_PASSWORD=your_gmail_app_password
```

Use a Gmail App Password rather than your regular Gmail password.

### 7. Run EventVerse

```bash
python3 main.py
```

## 💾 Data Storage

EventVerse uses JSON files to store student accounts, events, registrations, and reward information.

The application loads and updates these files as users interact with the system.

## 🔐 Security

- Passwords are hashed using PBKDF2-HMAC-SHA256 with individual salts.
- Passwords are not stored in plaintext.
- Email verification codes are generated securely.
- Email credentials are stored in environment variables and excluded from version control.

## 🎓 Project Information

Developed as part of an Applied Python Programming assignment.

**Project:** EventVerse  
**Language:** Python  
**Repository:** [GitHub - EventVerse](https://github.com/fahimmontasir-dev/EventVerse)

---

*Discover. Connect. Experience.*