"""
Caesar Cipher Implementation
A Python program that can encrypt and decrypt text using the Caesar Cipher algorithm.
"""

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using Caesar Cipher algorithm.
    Now encrypts all printable characters including letters, numbers, and symbols.
    
    Args:
        text (str): The text to encrypt or decrypt
        shift (int): The number of positions to shift each character
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if 32 <= ord(char) <= 126:
            shifted_ord = ((ord(char) - 32 + shift) % 95) + 32
            result += chr(shifted_ord)
        else:
            
            result += char
    
    return result

def get_user_input():
    """
    Get user input for message and shift value with friendly prompts.
    
    Returns:
        tuple: (message, shift, mode)
    """
    print("\n Welcome to Caesar Cipher!")
    print("=" * 40)
    print("What would you like to do?")
    print("1.  Encrypt a message")
    print("2.  Decrypt a message")
    
    while True:
        choice = input("\nPlease choose (1 or 2): ").strip()
        if choice in ['1', '2']:
            mode = 'encrypt' if choice == '1' else 'decrypt'
            action = "encrypt" if choice == '1' else "decrypt"
            break
        else:
            print(" Oops! Please enter 1 or 2.")
    
    print(f"\nGreat! Let's {action} your message.")
    message = input(f" Enter the message you want to {action}: ").strip()
    
    if not message:
        print("  You didn't enter any message. Please try again.")
        return get_user_input()
    
    print(f"\nNow, choose how much to shift your characters.")
    print(" Tip: Higher numbers make it harder to crack!")
    
    while True:
        try:
            shift = int(input(" Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print(" Shift must be between 1 and 25. Try again!")
        except ValueError:
            print(" That's not a valid number. Please enter 1-25.")
    
    return message, shift, mode

def main():
    """Main function to run the Caesar Cipher program with friendly interface."""
    print(" Welcome to the Caesar Cipher Tool!")
    print("This program helps you encrypt and decrypt messages using the ancient Caesar Cipher method.")
    print("It's perfect for secret messages, puzzles, or just having fun with cryptography!")
    
    while True:
        try:
            message, shift, mode = get_user_input()
            
            print(f"\n Processing your message...")
            
            if mode == 'encrypt':
                result = caesar_cipher(message, shift, 'encrypt')
                print(f"\n Success! Here's your encrypted message:")
                print(f" {result}")
                print(f"\n Remember: You'll need shift value {shift} to decrypt this later!")
            else:
                result = caesar_cipher(message, shift, 'decrypt')
                print(f"\n Success! Here's your decrypted message:")
                print(f" {result}")
            
            print(f"\n Great job! What would you like to do next?")
            continue_choice = input("Would you like to encrypt/decrypt another message? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes', 'yeah', 'sure', 'ok']:
                break
                
        except KeyboardInterrupt:
            print("\n\n Program interrupted. Thanks for using Caesar Cipher!")
            break
        except Exception as e:
            print(f"\n Oops! Something went wrong: {e}")
            print("Let's try again!")
    
    print("\n Thanks for using Caesar Cipher! Keep your secrets safe! ")

if __name__ == "__main__":
    main()
