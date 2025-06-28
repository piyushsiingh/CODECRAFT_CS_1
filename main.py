import time
import sys

def animate_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main loop
while True:
    animate_text("\n=== Caesar Cipher Tool ===", 0.03)
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))

    if choice == 'e':
        animate_text("\nEncrypting your message...", 0.04)
        time.sleep(0.5)
        encrypted = encrypt(message, shift)
        animate_text("Encrypted message: " + encrypted, 0.06)
    elif choice == 'd':
        animate_text("\nDecrypting your message...", 0.04)
        time.sleep(0.5)
        decrypted = decrypt(message, shift)
        animate_text("Decrypted message: " + decrypted, 0.06)
    else:
        animate_text("Invalid choice. Please enter 'e' or 'd'.", 0.05)

    # Ask user if they want to continue
    again = input("\nDo you want to try another message? (yes/y/no/n): ").strip().lower()
    if again not in ['yes', 'y']:
        animate_text("Thank you for using Caesar Cipher Tool. Goodbye! 🛡️", 0.05)
        break
