# 🖼️ Image Encryption Tool using Modular Arithmetic

This project is a simple image encryption and decryption tool built in Python. It applies **modular arithmetic** on each pixel’s RGB values to encrypt and decrypt the image.

---

## 📌 Features

- File picker popup to select image
- Modular arithmetic-based encryption and decryption
- Works with PNG, JPG, JPEG formats
- Command-line based — no GUI needed

---

## 🔐 How It Works

### 🔸 Encryption
For each RGB pixel `(r, g, b)`, apply:
(r + key) % 256, (g + key) % 256, (b + key) % 256

### 🔸 Decryption
For each RGB pixel `(r, g, b)`, apply:
(r - key + 256) % 256, (g - key + 256) % 256, (b - key + 256) % 256


---

## 🛠️ Requirements

- Python 3.x
- PIL (Pillow)
- tkinter (comes with Python)

Install dependencies (if needed):

```bash
pip install Pillow
