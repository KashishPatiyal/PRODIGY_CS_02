from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Encrypt using modular arithmetic
def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert('RGB')
    encrypted_image = Image.new('RGB', image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            encrypted_image.putpixel((x, y), (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            ))

    encrypted_image.save(output_path)
    print("✅ Encrypted image saved to:", output_path)

# Decrypt using reverse of modular arithmetic
def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert('RGB')
    decrypted_image = Image.new('RGB', image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            decrypted_image.putpixel((x, y), (
                (r - key + 256) % 256,
                (g - key + 256) % 256,
                (b - key + 256) % 256
            ))

    decrypted_image.save(output_path)
    print("✅ Decrypted image saved to:", output_path)

# Main function
def main():
    key = int(input("🔐 Enter encryption key (1–255): "))

    # Hide GUI window
    root = Tk()
    root.withdraw()

    print("📂 Select image to encrypt...")
    input_path = askopenfilename(title="Select image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not input_path:
        print("❌ No file selected.")
        return

    print("💾 Choose save location for encrypted image...")
    encrypted_output_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not encrypted_output_path:
        print("❌ No save path selected.")
        return

    encrypt_image(input_path, encrypted_output_path, key)

    print("💾 Choose save location for decrypted image...")
    decrypted_output_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not decrypted_output_path:
        print("❌ No save path selected.")
        return

    decrypt_image(encrypted_output_path, decrypted_output_path, key)

if __name__ == "__main__":
    main()
