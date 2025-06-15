#!/usr/bin/env python3
"""
Enhanced Email Spoofing Demonstration Tool with Environment Support
===================================================================

IMPORTANT LEGAL AND ETHICAL NOTICE:
This tool is designed EXCLUSIVELY for:
- Security research and education
- Anti-fraud training
- Authorized penetration testing
- Understanding email security vulnerabilities

UNAUTHORIZED USE IS ILLEGAL AND UNETHICAL.
Users are responsible for compliance with all applicable laws.
"""

import smtplib
import ssl
import argparse
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from typing import Optional
import getpass

class EmailSpoofAutoDemo:
    """Enhanced email spoofing demo with environment file support."""
    
    def __init__(self, config_file: str = "email_config.env"):
        self.config_file = config_file
        self.config = {}
        self.load_config()
        
    def load_config(self) -> None:
        """Load configuration from environment file."""
        if not os.path.exists(self.config_file):
            print(f"⚠️ Config file {self.config_file} not found. Using manual input mode.")
            return
            
        try:
            with open(self.config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        self.config[key.strip()] = value.strip()
            print(f"✅ Loaded configuration from {self.config_file}")
        except Exception as e:
            print(f"❌ Error loading config: {e}")
    
    def get_config_value(self, key: str, prompt: str, password: bool = False) -> str:
        """Get value from config or prompt user."""
        if key in self.config and self.config[key] != "your_app_password_here":
            print(f"📋 Using saved {key}: {self.config[key] if not password else '[saved password]'}")
            return self.config[key]
        else:
            if password:
                return getpass.getpass(prompt)
            else:
                return input(prompt).strip()
    
    def display_warning(self) -> None:
        """Display legal and ethical warning."""
        warning = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ⚠️  WARNING ⚠️                                  ║
║                                                                              ║
║  This tool is for EDUCATIONAL and AUTHORIZED TESTING purposes ONLY!         ║
║                                                                              ║
║  Unauthorized email spoofing is:                                            ║
║  • Illegal in most jurisdictions                                            ║
║  • Unethical and harmful                                                    ║
║  • May violate anti-fraud laws                                              ║
║  • Could result in criminal charges                                         ║
║                                                                              ║
║  Only use this tool if you have:                                            ║
║  • Explicit written permission                                              ║
║  • Legitimate security research purposes                                    ║
║  • Educational objectives                                                   ║
║                                                                              ║
║  You are solely responsible for your actions!                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(warning)
        
        response = input("Do you acknowledge and agree to use this tool responsibly? (yes/no): ")
        if response.lower() != 'yes':
            print("Tool usage declined. Exiting...")
            sys.exit(0)
    
    def quick_demo(self) -> None:
        """Run quick demo using saved configuration."""
        print("\n🚀 Quick Demo Mode (Using Saved Config)")
        print("=" * 50)
        
        # Load SMTP settings
        smtp_server = self.get_config_value('SMTP_SERVER', 'SMTP Server: ')
        smtp_port = int(self.get_config_value('SMTP_PORT', 'SMTP Port: ') or "587")
        username = self.get_config_value('SMTP_USERNAME', 'Email address: ')
        password = self.get_config_value('SMTP_PASSWORD', 'Password/App Password: ', password=True)
        
        # Load spoofing settings
        spoofed_from = self.get_config_value('DEFAULT_SPOOFED_EMAIL', 'Email to spoof FROM: ')
        spoofed_name = self.get_config_value('DEFAULT_SPOOFED_NAME', 'Display name: ')
        to_email = self.get_config_value('DEFAULT_TARGET_EMAIL', 'Send TO: ')
        
        # Create and send demo
        subject = self.config.get('DEMO_SUBJECT', '[SECURITY DEMO] Email Spoofing Demonstration')
        
        print(f"\n📤 Sending demo email...")
        print(f"   From (spoofed): {spoofed_name} <{spoofed_from}>")
        print(f"   To: {to_email}")
        print(f"   Via: {smtp_server} ({username})")
        
        success = self.send_spoofed_email(
            smtp_server, smtp_port, username, password,
            spoofed_from, spoofed_name, to_email, subject
        )
        
        if success:
            print("\n🎓 Demo sent! Check your email and examine the headers.")
    
    def send_spoofed_email(self, smtp_server: str, smtp_port: int, username: str, 
                          password: str, spoofed_from: str, spoofed_name: str, 
                          to_email: str, subject: str) -> bool:
        """Send the spoofed demonstration email."""
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        
        # Enhanced spoofing with better headers
        if spoofed_name and spoofed_name.strip():
            from_header = f"{spoofed_name} <{spoofed_from}>"
        else:
            from_header = spoofed_from
        
        # Set multiple header variations to improve spoofing success
        msg['From'] = from_header
        msg['Reply-To'] = spoofed_from
        msg['Return-Path'] = spoofed_from
        msg['Sender'] = from_header
        msg['To'] = to_email
        
        # Add headers to make it look more legitimate
        msg['Message-ID'] = f"<{hash(abs(hash(spoofed_from)))}@{spoofed_from.split('@')[1]}>"
        msg['X-Mailer'] = 'Coinbase Notifications'
        msg['X-Priority'] = '1'
        msg['X-Demo-Purpose'] = 'Security-Education-Only'
        
        # Create body
        body = f""" ███▄ ▄███▓ ▄▄▄       ██▀███   ██▒   █▓▓█████ ▓█████  ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓█   ▀  ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▒███   ▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░▒████▒▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░░ ▒░ ░░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░ ░ ░  ░░ ░░   ░ ▒░
░      ░     ░   ▒     ░░   ░      ░░     ░      ░      ░   ░ ░ 
       ░         ░  ░   ░           ░     ░  ░   ░  ░         ░ 
                                   ░                            
"""
        
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Send email with spoofed envelope
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls(context=context)
                server.login(username, password)
                
                # Send with authenticated account but spoofed headers
                server.sendmail(username, to_email, msg.as_string())
            
            print("✅ Demo email sent successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error sending email: {str(e)}")
            return False
    
    def update_config(self) -> None:
        """Update the configuration file with new values."""
        print("\n⚙️ Configuration Update Mode")
        print("=" * 40)
        
        new_config = {}
        
        # SMTP settings
        new_config['SMTP_SERVER'] = input(f"SMTP Server ({self.config.get('SMTP_SERVER', 'smtp.gmail.com')}): ").strip() or self.config.get('SMTP_SERVER', 'smtp.gmail.com')
        new_config['SMTP_PORT'] = input(f"SMTP Port ({self.config.get('SMTP_PORT', '587')}): ").strip() or self.config.get('SMTP_PORT', '587')
        new_config['SMTP_USERNAME'] = input(f"Email address ({self.config.get('SMTP_USERNAME', '')}): ").strip() or self.config.get('SMTP_USERNAME', '')
        
        update_password = input("Update password? (y/n): ").lower() == 'y'
        if update_password:
            new_password = getpass.getpass("New password/app password: ")
            new_config['SMTP_PASSWORD'] = new_password
        else:
            new_config['SMTP_PASSWORD'] = self.config.get('SMTP_PASSWORD', 'your_app_password_here')
        
        # Spoofing defaults
        new_config['DEFAULT_SPOOFED_EMAIL'] = input(f"Default spoofed email ({self.config.get('DEFAULT_SPOOFED_EMAIL', '')}): ").strip() or self.config.get('DEFAULT_SPOOFED_EMAIL', '')
        new_config['DEFAULT_SPOOFED_NAME'] = input(f"Default spoofed name ({self.config.get('DEFAULT_SPOOFED_NAME', '')}): ").strip() or self.config.get('DEFAULT_SPOOFED_NAME', '')
        new_config['DEFAULT_TARGET_EMAIL'] = input(f"Default target email ({self.config.get('DEFAULT_TARGET_EMAIL', '')}): ").strip() or self.config.get('DEFAULT_TARGET_EMAIL', '')
        
        # Save updated config
        try:
            with open(self.config_file, 'w') as f:
                f.write("# Email Spoofing Demo - Environment Configuration\n")
                f.write("# FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY\n\n")
                
                f.write("# SMTP Server Configuration\n")
                f.write(f"SMTP_SERVER={new_config['SMTP_SERVER']}\n")
                f.write(f"SMTP_PORT={new_config['SMTP_PORT']}\n")
                f.write(f"SMTP_USERNAME={new_config['SMTP_USERNAME']}\n")
                f.write(f"SMTP_PASSWORD={new_config['SMTP_PASSWORD']}\n\n")
                
                f.write("# Default Spoofing Configuration\n")
                f.write(f"DEFAULT_SPOOFED_EMAIL={new_config['DEFAULT_SPOOFED_EMAIL']}\n")
                f.write(f"DEFAULT_SPOOFED_NAME={new_config['DEFAULT_SPOOFED_NAME']}\n")
                f.write(f"DEFAULT_TARGET_EMAIL={new_config['DEFAULT_TARGET_EMAIL']}\n\n")
                
                f.write("# Demo Settings\n")
                f.write("DEMO_SUBJECT=[SECURITY DEMO] Email Spoofing Demonstration\n")
                f.write("DEMO_PURPOSE=Security-Education-Only\n")
            
            print(f"✅ Configuration saved to {self.config_file}")
            self.config = new_config
            
        except Exception as e:
            print(f"❌ Error saving config: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Enhanced Email Spoofing Demo with Environment Support",
        epilog="⚠️ For authorized security research and education only!"
    )
    
    parser.add_argument('--quick', '-q', action='store_true',
                       help='Run quick demo using saved configuration')
    parser.add_argument('--config', '-c', action='store_true',
                       help='Update configuration file')
    parser.add_argument('--file', '-f', default='email_config.env',
                       help='Configuration file to use (default: email_config.env)')
    
    args = parser.parse_args()
    
    demo = EmailSpoofAutoDemo(args.file)
    demo.display_warning()
    
    if args.config:
        demo.update_config()
    elif args.quick:
        demo.quick_demo()
    else:
        print("\nUsage options:")
        print("  --quick, -q    : Run demo with saved settings")
        print("  --config, -c   : Update configuration")
        print("  --file, -f     : Specify config file")
        print(f"\nExample: python3 {sys.argv[0]} --quick")


if __name__ == "__main__":
    main() 