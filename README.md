# Email Spoofing Demo

This repository contains a demonstration of email spoofing techniques for educational and security awareness purposes. It is designed to help security professionals and developers understand how email spoofing works and how to protect against it.

## ⚠️ Important Notice

This project is for **EDUCATIONAL PURPOSES ONLY**. Using these techniques for malicious purposes is illegal and unethical. Always ensure you have proper authorization before testing email security.

## Features

- SMTP server implementation for email sending
- Email spoofing demonstration
- Local SMTP server for testing
- Configuration management
- Security best practices documentation

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/email-spoof-demo.git
cd email-spoof-demo
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example configuration:
```bash
cp config_example.txt email_config.env
```

5. Edit `email_config.env` with your settings (see Configuration section)

## Configuration

Create an `email_config.env` file with the following structure:

```env
# SMTP Server Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Default Spoofing Configuration
DEFAULT_SPOOFED_EMAIL=example@domain.com
DEFAULT_SPOOFED_NAME=Example Name
DEFAULT_TARGET_EMAIL=target@example.com

# Demo Settings
DEMO_SUBJECT=[Demo] Test Email
DEMO_PURPOSE=Security-Education-Only
```

## Usage

1. Run the demo script:
```bash
python email_spoof_demo.py
```

2. For local testing:
```bash
python local_smtp_server.py
```

## Security Best Practices

1. Always use App Passwords for Gmail
2. Never commit real credentials to version control
3. Use this tool only in controlled environments
4. Implement proper email authentication (SPF, DKIM, DMARC)
5. Regular security audits of email systems

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is provided for educational purposes only. The authors are not responsible for any misuse or damage caused by this program. Users are responsible for ensuring they have proper authorization before using this tool. 