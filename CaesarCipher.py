def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Shift character within alphabet
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                shifted_char = chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                shifted_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

def main():
    while True:
        mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
        if mode in ['e', 'encrypt', 'd', 'decrypt']:
            break
        else:
            print("Invalid choice, please enter 'E' for encryption or 'D' for decryption.")
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if mode in ['e', 'encrypt']:
        encrypted_text = caesar_cipher(text, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted_text}")
    elif mode in ['d', 'decrypt']:
        decrypted_text = caesar_cipher(text, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
