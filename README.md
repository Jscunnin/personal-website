# Personal Website

**Live Site:** [jscunnin.com](https://jscunnin.com)

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

## About

This is a personal portfolio website designed to provide employers, collaborators, and visitors with a central hub to learn about my background, view my projects, and get in touch. The site emphasizes clean design, responsiveness, and user experience.

## Features

- ✨ **Portfolio Showcase** - Display of projects with descriptions and links
- 👤 **Professional Profile** - Overview of skills, experience, and background
- 📧 **Contact System** - Static contact page with contact details
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
├── main.py                # Flask application entry point (runs on port 5001 by default)
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
- A Linux server (for production deployment)

### Installation

Note: this project includes a `requirements.txt`. Prefer installing from that file for reproducible installs.

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jscunnin/personal-website.git
   cd personal-website
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Running Locally

Start the development server directly (the application uses port 5001 by default):

```bash
python main.py
```

Then open `http://localhost:5001` in your browser.

## Deployment

### Linux Server Setup

1. **SSH into your server**
   ```bash
   ssh user@server_ip
   ```

2. **Clone the repository on the server**
   ```bash
   git clone https://github.com/Jscunnin/personal-website.git
   cd personal-website
   ```

3. **Install Python dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Prepare runtime directories and permissions**

   The application writes connection logs to `.data/connections.log`. Create the `.data` directory with appropriate permissions:

   ```bash
   mkdir -p .data
   chmod 700 .data
   ```

5. **Set up a systemd service**

   Create a systemd unit file (e.g., `/etc/systemd/system/personal-website.service`):

   ```ini
   [Unit]
   Description=Personal Website (Flask)
   After=network.target

   [Service]
   Type=simple
   User=<service_user>
   WorkingDirectory=<project_path>
   ExecStart=<project_path>/venv/bin/python <project_path>/main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Replace `<service_user>` with your service user and `<project_path>` with the full path to your project directory.

   Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable personal-website
   sudo systemctl start personal-website
   ```

   Manage the service:
   - Check status: `sudo systemctl status personal-website`
   - Restart: `sudo systemctl restart personal-website`
   - View logs: `sudo journalctl -u personal-website -f`

## Logging and Privacy

- `main.py` writes simple connection logs to `.data/connections.log` and uses a cookie-based `userID` flow for basic logging. Ensure `.data` is created and secured on the server; do not commit logs to version control.
- The contact page includes contact details in `templates/contact.html`. If you prefer to collect messages instead of exposing contact details, implement a contact form or email-proxy endpoint.

## Contributing

This is a personal project, but suggestions and improvements are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request
