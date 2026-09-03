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

This is a personal portfolio website designed to provide employers, collaborators, and visitors with a central hub to learn about my background, view my projects, and get in touch. The site emphasizes a simple, fast frontend and a small Flask backend.

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
| **Deployment** | systemd service (example)

## Project Structure

```
personal-website/
├── README.md
├── main.py                # Flask application entry point (runs on port 5001 by default)
├── requirements.txt       # Python dependencies (added)
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

Note: this project now includes a minimal `requirements.txt`. Prefer installing from that file for reproducible installs.

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jscunnin/personal-website.git
   cd personal-website
   ```

2. **Create and activate a virtual environment** (only once)
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   If you have `requirements.txt` (recommended):
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If you don't have `requirements.txt` (not recommended):
   ```bash
   python -m pip install --upgrade pip
   pip install Flask
   ```

Notes
- The repository now contains a minimal `requirements.txt` (Flask dependency). Pin versions there if you need strict reproducibility.
- Do not recreate the virtual environment multiple times; create it once and activate it for subsequent steps.

## Running Locally

Start the development server directly (the application uses port 5001 by default):

```bash
python main.py
# Open http://localhost:5001
```

To run with the Flask CLI (set the FLASK_APP environment variable):

```bash
export FLASK_APP=main
export FLASK_ENV=development
flask run --port 5001
```

Windows PowerShell equivalents:
```powershell
$env:FLASK_APP = 'main'
$env:FLASK_ENV = 'development'
flask run --port 5001
```

Notes
- `flask run` requires `FLASK_APP` to be set (or an installed Flask app). The `python main.py` approach works without the Flask environment variables.
- main.py currently calls app.run(..., port=5001). If you prefer the standard 5000 port, change the port in `main.py`.

## Deployment

### Linux Server Setup (example)

1. **SSH into your server**
   ```bash
   ssh user@your_server_ip
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

   The application writes connection logs to `.data/connections.log`. Create the `.data` directory and ensure the service user can write to it:

   ```bash
   mkdir -p .data
   sudo chown -R websites:websites .data   # adjust user:group as appropriate
   chmod 700 .data
   ```

5. **Set up a systemd service** (example)

   Create `/etc/systemd/system/personal-website.service` with contents similar to:
   ```ini
   [Unit]
   Description=Personal Website (Flask)
   After=network.target

   [Service]
   Type=simple
   User=websites
   WorkingDirectory=/home/websites/personal-website
   ExecStart=/home/websites/personal-website/venv/bin/python /home/websites/personal-website/main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Important: update `User`, `WorkingDirectory`, and `ExecStart` to match your server paths and service user. The example above assumes the project is at `/home/websites/personal-website` and that you are using the virtualenv's python as ExecStart.

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

Notes
- The README previously used `/home/websites/personalWebsite` (no hyphen). Make sure the paths in the unit file match where you actually deploy the repository.
- The repository does not include the systemd unit file by default; the example above is intended as a starting point — commit it to the deployment tooling if you want it tracked.

## Logging and privacy

- `main.py` writes simple connection logs to `.data/connections.log` and uses a cookie-based `userID` flow for basic logging. Ensure `.data` is created and secured on the server; do not commit logs to the repository.
- The contact page includes a phone number and email in `templates/contact.html`. If you prefer to collect messages instead of exposing contact details, implement a form or an email-proxy endpoint and remove the static contact details.

## Contributing

This is a personal project, but suggestions and improvements are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---
