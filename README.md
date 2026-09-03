# Personal Website

A fully-featured personal portfolio website showcasing projects, skills, and contact information. Built with Flask and deployed on a self-managed Linux server.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## About

This is a personal portfolio website designed to provide employers, collaborators, and visitors with a central hub to learn about my background, view my projects, and get in touch. The site emphasizes clean design and user experience while maintaining robust backend functionality.

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
| **Deployment** | Manual Linux server |

## Project Structure

```
personal-website/
├── README.md
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── static/               # Static assets (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   └── contact.html
└── config/              # Configuration files
    └── config.py
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

## Configuration

Create a `.env` file in the project root with the following variables (example):

```env
FLASK_ENV=development
FLASK_DEBUG=False
SECRET_KEY=your_secret_key_here
```

Update `config/config.py` with your site-specific settings:
- Site title and metadata
- Contact email address
- Social media links
- Project details

## Running Locally

Start the development server:

```bash
python app.py
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
   cd personal-website
   ```

3. **Install Python dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure your web server** (nginx recommended)
   - Use Gunicorn as the WSGI application server
   - Set up a reverse proxy with nginx
   - Configure SSL/TLS certificates (Let's Encrypt)

5. **Start the application**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

6. **Set up a systemd service** (for automatic restarts)
   Create `/etc/systemd/system/personal-website.service`:
   ```ini
   [Unit]
   Description=Personal Website
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/path/to/personal-website
   Environment="PATH=/path/to/personal-website/venv/bin"
   ExecStart=/path/to/personal-website/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Enable and start the service:
   ```bash
   sudo systemctl enable personal-website
   sudo systemctl start personal-website
   ```

## Contributing

This is a personal project, but suggestions and improvements are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

[Add your license here - e.g., MIT License]

---

**Note:** The live domain is currently offline. You can view this repository for the source code and setup instructions.
