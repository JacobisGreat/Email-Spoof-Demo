#!/bin/bash

# Email Spoofing Demonstration Tool - Demo Script
# For educational and authorized security research purposes only

echo "🛡️ Email Spoofing Demonstration Tool"
echo "======================================"
echo ""
echo "⚠️  FOR EDUCATIONAL PURPOSES ONLY ⚠️"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.6+ to use this tool."
    exit 1
fi

echo "✅ Python 3 detected: $(python3 --version)"
echo ""

# Display available options
echo "📋 Available demo options:"
echo ""
echo "1. 📚 Learn about email spoofing (--info)"
echo "2. 🎓 Run interactive educational demo (--interactive)"
echo "3. ❓ Show help and usage (--help)"
echo ""

# Ask user what they want to do
read -p "Select an option (1-3): " choice

case $choice in
    1)
        echo ""
        echo "📖 Displaying educational information about email spoofing..."
        python3 email_spoof_demo.py --info
        ;;
    2)
        echo ""
        echo "🎓 Starting interactive educational demonstration..."
        echo "Note: You'll need SMTP server access to complete the demo."
        echo ""
        python3 email_spoof_demo.py --interactive
        ;;
    3)
        echo ""
        echo "❓ Displaying help information..."
        python3 email_spoof_demo.py --help
        ;;
    *)
        echo ""
        echo "❌ Invalid option. Please run the script again and choose 1, 2, or 3."
        exit 1
        ;;
esac

echo ""
echo "🎯 Demo completed!"
echo ""
echo "📚 Additional Resources:"
echo "• Check the README.md for detailed documentation"
echo "• Review the email_spoof_demo.py source code to understand the implementation"
echo "• Visit security resources to learn more about email authentication"
echo ""
echo "⚖️  Remember: Use this knowledge responsibly and only for authorized purposes!" 