# Personal Website

jscunnin.com
A fully-featured personal portfolio website showcasing projects, skills, and contact information. Built with Flask and deployed on a self-managed Linux server.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## About

This is a personal portfolio website designed to provide employers, collaborators, and visitors with a central hub to learn about my background, view my projects, and get in touch. The site emphasizes[...]

## Features

- ✨ **Portfolio Showcase** - Display of projects with descriptions and links
- 👤 **Professional Profile** - Overview of skills, experience, and background
- 📧 **Contact System** - Easy way for visitors to reach out
- 📱 **Responsive Design** - Works across desktop, tablet, and mobile devices
- ⚡ **Fast Performance** - Lightweight frontend and optimized backend

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML, CSS |
| **Backend** | Flask (Python) |
| **Server** | Linux (self-managed) |
| **Deployment** | systemd service |

## Project Structure

```
personal-website/
├── README.md
├── main.py                # Flask application entry point
├── requirements.txt       # Python dependencies
├── static/               # Static assets (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/            # Jinja2 HTML templates
    ├── base.html
    ├── index.html
    ├── projects.html
    └── contact.html
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Linux server (for production deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jscunnin/personal-website.git
   cd personal-website
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

Start the development server:

```bash
python main.py
```

The site will be available at `http://localhost:5000`

For development with auto-reload:

```bash
export FLASK_ENV=development
flask run
```

## Deployment

### Linux Server Setup

1. **SSH into your server**
   ```bash
   ssh user@your_server_ip
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/Jscunnin/personal-website.git
   cd /path/to/personal-website
   ```

3. **Install Python dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set up a systemd service** (for automatic startup and restarts)
   
   Create `/etc/systemd/system/personal-website.service`:
   ```ini
   [Unit]
   Description=Professional Personal Website
   After=network.target

   [Service]
   Type=simple
   ExecStart=/bin/python3 /home/websites/personalWebsite/main.py
   Restart=always
   User=websites
   WorkingDirectory=/home/websites/personalWebsite

   [Install]
   WantedBy=multi-user.target
   ```

   Enable and start the service:
   ```bash
   sudo systemctl enable personal-website
   sudo systemctl start personal-website
   ```

5. **Manage the service**
   
   - Check status: `sudo systemctl status personal-website`
   - Restart: `sudo systemctl restart personal-website`
   - View logs: `sudo journalctl -u personal-website -f`

## Contributing

This is a personal project, but suggestions and improvements are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request
---
