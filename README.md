#  Caesar Cipher Tool

A fun and interactive Python program that lets you encrypt and decrypt secret messages using the ancient Caesar Cipher method! Perfect for creating secret codes, solving puzzles, or just having fun with cryptography.

##  What is Caesar Cipher?

The Caesar Cipher is one of the oldest and most famous encryption techniques in history! Named after Julius Caesar (who used it to protect his military messages), it works by shifting each letter in your message by a certain number of positions in the alphabet. It's like a secret code that only people with the "key" can understand!

##  Cool Features

-  **Super Encryption**: Encrypts EVERYTHING - letters, numbers, symbols, and even spaces!
-  **Easy Decryption**: Just use the same shift number to get your original message back
-  **Interactive & Fun**: Friendly interface with helpful tips
-  **Smart Validation**: Won't let you enter invalid numbers
-  **Perfect for Everyone**: Whether you're a beginner or cryptography expert
-  **No Dependencies**: Just run it with Python - no extra installations needed!

## Files

- `caesar_cipher.py` - Main program with Caesar Cipher implementation
- `test_caesar_cipher.py` - Test script to verify functionality
- `README.md` - This documentation file

## How to Run

### Run the main program:
```bash
python caesar_cipher.py
```

### Run the test script:
```bash
python test_caesar_cipher.py
```

## How it Works

1. **Encryption**: Each letter is replaced by a letter some fixed number of positions down the alphabet
2. **Decryption**: The reverse process - letters are shifted back by the same amount
3. **Modular arithmetic**: Uses modulo 26 to wrap around the alphabet (Z + 1 = A)

## Example

- **Original text**: "sharky01 is a h@cker"
- **Shift value**: 11
- **Encrypted**: "~sl}v%;<+t~+l+sKnvp}"
- **Decrypted**: "sharky01 is a h@cker" (using shift 11 in reverse)

**Note**: encrypts ALL printable characters including numbers and symbols


##  How to Get Started

1. **Run the program**: `python caesar_cipher.py`
2. **Choose**: Pick encrypt (1) or decrypt (2)
3. **Type your secret message**: Enter whatever you want to encrypt/decrypt
4. **Pick your shift number**: Choose between 1-25 (higher = more secure!)
5. **Get your result**: See your encrypted/decrypted message
6. **Keep going**: The program will ask if you want to do more!

##  Perfect For:

-  **Secret messages** between friends
-  **Puzzle solving** and brain teasers  
-  **Learning cryptography** concepts
-  **Fun coding projects**
-  **Understanding encryption** basics