#!/usr/bin/env python3
"""
Simple SMTP Test Script
Test if your email server settings work before using the main tool.
"""

import smtplib
import ssl
import getpass

def test_smtp():
    print("🧪 SMTP Connection Test")
    print("=" * 30)
    
    # Get settings from user
    smtp_server = input("SMTP Server (e.g., smtp.gmail.com): ").strip()
    smtp_port = int(input("SMTP Port (usually 587): ") or "587")
    username = input("Your email address: ").strip()
    password = getpass.getpass("Your password/app password: ")
    
    print(f"\n🔄 Testing connection to {smtp_server}:{smtp_port}...")
    
    try:
        # Test connection
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print("✅ Connected to server")
            
            server.starttls(context=context)
            print("✅ TLS encryption enabled")
            
            server.login(username, password)
            print("✅ Authentication successful")
            
        print("\n🎉 SUCCESS! Your SMTP settings work!")
        print(f"You can now use these settings in the email spoofing tool:")
        print(f"  Server: {smtp_server}")
        print(f"  Port: {smtp_port}")
        print(f"  Username: {username}")
        print(f"  Password: [the password you just entered]")
        
    except Exception as e:
        print(f"\n❌ Connection failed: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("• For Gmail: Enable 2FA and use App Passwords")
        print("• For Outlook: Try your regular password first")
        print("• Check if server address and port are correct")
        print("• Some networks block SMTP - try a different network")

if __name__ == "__main__":
    test_smtp() 