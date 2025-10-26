import os
from cryptography.fernet import Fernet

# --- 1. Key Management ---
def generate_key():
    """Generates a new Fernet key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'secret.key'")

def load_key():
    """Loads the previously generated key from the current directory."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Error: 'secret.key' not found. Please run the tool with 'generate' command first.")
        return None

# --- 2. Encryption/Decryption Functions ---
def encrypt_file(filename, key):
    """Encrypts a file using the provided Fernet key."""
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        with open(filename + ".enc", "wb") as file:
            file.write(encrypted_data)
        
        os.remove(filename)
        print(f"File '{filename}' successfully ENCRYPTED to '{filename}.enc'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_file(filename, key):
    """Decrypts a file using the provided Fernet key."""
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        # Determine the original filename
        if filename.endswith(".enc"):
            original_filename = filename[:-4]
        else:
            original_filename = "decrypted_" + filename
            
        with open(original_filename, "wb") as file:
            file.write(decrypted_data)
            
        os.remove(filename)
        print(f"File '{filename}' successfully DECRYPTED to '{original_filename}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}. Check if the key is correct.")

# --- 3. Main Execution Logic ---
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 encryptor.py <command> [filename]")
        print("Commands: generate, encrypt <filename>, decrypt <filename>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        generate_key()
    elif command == "encrypt" and len(sys.argv) == 3:
        key = load_key()
        if key:
            encrypt_file(sys.argv[2], key)
    elif command == "decrypt" and len(sys.argv) == 3:
        key = load_key()
        if key:
            decrypt_file(sys.argv[2], key)
    else:
        print("Invalid command or missing filename.")
        print("Commands: generate, encrypt <filename>, decrypt <filename>")

