# cryptohide
CryptoHide is a secure image steganography project that allows users to hide and extract secret messages inside images using the Least Significant Bit (LSB) technique. This tool provides an intuitive web interface and is ideal for experimenting with secure message encoding.

🔧 Tech Stack
Frontend:
HTML
CSS
JavaScript

Backend:
Python
Flask
Hosting/Local Server:
PHP
WAMP Server (localhost)

Steganography Algorithm:
LSB (Least Significant Bit) Image Encoding

✨ Features
🔐 Encode secret messages into image pixels
🔍 Decode and retrieve hidden messages
🖥️ Simple and clean user interface
💾 Local hosting using WAMP for easy access and testing
🧪 Easy integration between Flask and PHP server environment

🚀 How to Run
1.Make sure WAMP Server is running (PHP + MySQL support).
2.Place your project folder inside www directory of WAMP.
3.Start Flask backend using:
python app.py
4.Open your browser and visit:
http://localhost/crypto-hide

📷 Usage
Encoding a Message:
Upload a clean image (preferably PNG).
Enter your secret message.
Click on "Encode" to generate a stego image.

Decoding a Message:
Upload a stego image that contains hidden text.
Click on "Decode" to reveal the message.
