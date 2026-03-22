# My Project
"""
QR Code Generator
==================
A simple Python script to generate QR codes from text or URLs.

Author: [Syed Noman]
Date: March 2026


Usage:
    1. Replace the text in the 'url' variable with your desired content
    2. Run: python Qr.py
    3. Find the generated qrcode.png in the same directory

Requirements:
    - Python 3.6+
    - qrcode library: pip install qrcode[pil]
"""

import qrcode

# =============================================================================
# CONFIGURATION
# =============================================================================

# Enter your text or URL here
# Examples:
#   - Website: "https://www.github.com"
#   - Text: "Hello World!"
#   - Email: "mailto:someone@example.com"
#   - Phone: "tel:+1234567890"
#   - WiFi: "WIFI:T:WPA;S:NetworkName;P:Password;;"

url = "enter text or url here"

# Output filename (you can change this)
output_filename = "qrcode.png"

# =============================================================================
# QR CODE GENERATION
# =============================================================================

# Generate the QR code image
img = qrcode.make(url)

# Save the QR code as a PNG image
img.save(output_filename)

# Display success message
print(f"✓ QR code created successfully!")
print(f"✓ Saved as: {output_filename}")
print(f"✓ Content: {url}")
