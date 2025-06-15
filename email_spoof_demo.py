#!/usr/bin/env python3
"""
Email Spoofing Demonstration Tool
==================================

IMPORTANT LEGAL AND ETHICAL NOTICE:
This tool is designed EXCLUSIVELY for:
- Security research and education
- Anti-fraud training
- Authorized penetration testing
- Understanding email security vulnerabilities

UNAUTHORIZED USE IS ILLEGAL AND UNETHICAL.
Users are responsible for compliance with all applicable laws.

Author: Security Research Tool
License: Educational Use Only
"""

import smtplib
import ssl
import argparse
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from typing import Optional
import getpass

class EmailSpoofDemo:
    """
    Educational email spoofing demonstration class.
    
    This class demonstrates how email spoofing works by showing
    how email headers can be manipulated. It's designed to help
    security professionals understand vulnerabilities.
    """
    
    def __init__(self):
        self.smtp_server: Optional[str] = None
        self.smtp_port: int = 587
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        
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
    
    def configure_smtp(self, server: str, port: int, username: str, password: str) -> None:
        """Configure SMTP settings."""
        self.smtp_server = server
        self.smtp_port = port
        self.username = username
        self.password = password
    
    def create_spoofed_message(self, 
                             spoofed_from: str,
                             spoofed_name: str,
                             to_email: str,
                             subject: str,
                             body: str,
                             html_body: Optional[str] = None) -> MIMEMultipart:
        """
        Create a message with spoofed headers for demonstration purposes.
        
        Args:
            spoofed_from: The email address to appear as sender
            spoofed_name: The display name to appear as sender
            to_email: Recipient email address
            subject: Email subject
            body: Plain text body
            html_body: Optional HTML body
            
        Returns:
            MIMEMultipart: The crafted email message
        """
        
        # Create message container
        msg = MIMEMultipart('alternative')
        
        # Set headers - this is where the "spoofing" happens
        msg['Subject'] = subject
        msg['From'] = formataddr((spoofed_name, spoofed_from))
        msg['To'] = to_email
        
        # Add a custom header to identify this as a demo
        msg['X-Demo-Purpose'] = 'Security-Education-Only'
        
        # Create plain text part
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Create HTML part if provided
        if html_body:
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)
        
        return msg
    
    def send_demo_email(self, message: MIMEMultipart, to_email: str) -> bool:
        """
        Send the demonstration email.
        
        Args:
            message: The crafted email message
            to_email: Recipient email address
            
        Returns:
            bool: True if successful, False otherwise
        """
        
        if not all([self.smtp_server, self.username, self.password]):
            print("❌ SMTP configuration incomplete!")
            return False
        
        try:
            # Create secure SSL context
            context = ssl.create_default_context()
            
            # Connect to server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.username, self.password)
                
                # Send the email
                text = message.as_string()
                server.sendmail(self.username, to_email, text)
                
            print("✅ Demo email sent successfully!")
            print("📧 Check the recipient's inbox and examine the email headers.")
            return True
            
        except Exception as e:
            print(f"❌ Error sending email: {str(e)}")
            return False
    
    def educational_demo(self) -> None:
        """Run an interactive educational demonstration."""
        print("\n🎓 Email Spoofing Educational Demonstration")
        print("=" * 50)
        
        print("\n📚 What you'll learn:")
        print("• How email headers can be manipulated")
        print("• Why email authentication is important")
        print("• How to identify potentially spoofed emails")
        
        print("\n⚙️ SMTP Configuration")
        print("You need access to an SMTP server to send the demo email.")
        print("Common options: Gmail, Outlook, or your organization's SMTP server")
        
        # Get SMTP configuration
        smtp_server = input("SMTP Server (e.g., smtp.gmail.com): ").strip()
        smtp_port = int(input("SMTP Port (usually 587): ") or "587")
        username = input("Your email address: ").strip()
        password = getpass.getpass("Your email password/app password: ")
        
        self.configure_smtp(smtp_server, smtp_port, username, password)
        
        print("\n📧 Demo Email Configuration")
        spoofed_from = input("Email to spoof FROM (e.g., ceo@company.com): ").strip()
        spoofed_name = input("Display name to spoof (e.g., CEO Name): ").strip()
        to_email = input("Send demo TO (your test email): ").strip()
        
        # Create educational content
        subject = "[SECURITY DEMO] Email Spoofing Demonstration"
        
        body = f"""This is a demonstration of email spoofing for educational purposes.

WHAT THIS DEMONSTRATES:
• This email appears to come from: {spoofed_name} <{spoofed_from}>
• But it was actually sent through: {username}
• This shows how email headers can be manipulated

HOW TO DETECT SPOOFED EMAILS:
1. Check the email headers (View Source/Raw)
2. Look for SPF, DKIM, and DMARC authentication results
3. Verify unusual requests through other channels
4. Be suspicious of urgent requests for sensitive information

REMEMBER: This is for educational purposes only!
Unauthorized email spoofing is illegal and unethical.

Security Research Tool - {self.username}
"""

        html_body = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="background-color: #ffe6e6; border: 2px solid #ff9999; padding: 15px; margin-bottom: 20px;">
        <h2 style="color: #cc0000; margin-top: 0;">🛡️ SECURITY DEMONSTRATION</h2>
        <p><strong>This is an educational email spoofing demonstration.</strong></p>
    </div>
    
    <h3>What This Demonstrates:</h3>
    <ul>
        <li>This email <em>appears</em> to come from: <strong>{spoofed_name} &lt;{spoofed_from}&gt;</strong></li>
        <li>But it was actually sent through: <strong>{username}</strong></li>
        <li>This shows how email headers can be manipulated</li>
    </ul>
    
    <h3>🔍 How to Detect Spoofed Emails:</h3>
    <ol>
        <li><strong>Check email headers</strong> (View Source/Raw in your email client)</li>
        <li><strong>Look for authentication results</strong> (SPF, DKIM, DMARC)</li>
        <li><strong>Verify through other channels</strong> for unusual requests</li>
        <li><strong>Be suspicious</strong> of urgent requests for sensitive information</li>
    </ol>
    
    <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; padding: 10px; margin-top: 20px;">
        <p><strong>⚠️ Remember:</strong> This is for educational purposes only!<br>
        Unauthorized email spoofing is illegal and unethical.</p>
    </div>
    
    <p style="margin-top: 20px; font-size: 0.9em; color: #666;">
        Security Research Tool - {self.username}
    </p>
</body>
</html>
"""
        
        # Create and send the demo message
        message = self.create_spoofed_message(
            spoofed_from, spoofed_name, to_email, subject, body, html_body
        )
        
        print(f"\n📤 Sending demo email...")
        print(f"   From (spoofed): {spoofed_name} <{spoofed_from}>")
        print(f"   To: {to_email}")
        print(f"   Subject: {subject}")
        
        success = self.send_demo_email(message, to_email)
        
        if success:
            print("\n🎓 Educational Points:")
            print("1. Check your email and examine the headers")
            print("2. Notice how the 'From' field can be misleading")
            print("3. Look for authentication warnings in your email client")
            print("4. This demonstrates why email authentication (SPF/DKIM/DMARC) is crucial")


def main():
    parser = argparse.ArgumentParser(
        description="Educational Email Spoofing Demonstration Tool",
        epilog="⚠️  For authorized security research and education only!"
    )
    
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run interactive educational demonstration')
    parser.add_argument('--info', action='store_true',
                       help='Display information about email spoofing')
    
    args = parser.parse_args()
    
    demo = EmailSpoofDemo()
    demo.display_warning()
    
    if args.info:
        print("\n📖 About Email Spoofing:")
        print("=" * 40)
        print("""
Email spoofing is the creation of email messages with a forged sender address.
This is possible because the Simple Mail Transfer Protocol (SMTP) does not 
provide mechanisms for authentication.

DEFENSIVE MEASURES:
• SPF (Sender Policy Framework) - Validates sending server
• DKIM (DomainKeys Identified Mail) - Cryptographic signatures  
• DMARC (Domain-based Message Authentication) - Policy framework
• User education and awareness training

LEGITIMATE USES:
• Security research and penetration testing
• Anti-phishing training and awareness
• Understanding email vulnerabilities
• Developing email security solutions

This tool helps security professionals understand these vulnerabilities
to better protect their organizations.
        """)
    
    elif args.interactive:
        demo.educational_demo()
    
    else:
        print("\nUse --interactive to run the demo or --info for more information")
        print("Example: python email_spoof_demo.py --interactive")


if __name__ == "__main__":
    main() 