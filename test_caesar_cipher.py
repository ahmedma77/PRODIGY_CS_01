"""
Test script for Caesar Cipher implementation
"""

from caesar_cipher import caesar_cipher

def test_caesar_cipher():
    """Test the Caesar Cipher functions with various inputs."""
    
    print("Testing Caesar Cipher Implementation...")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        ("Hello World", 3, "encrypt"),
        ("Khoor#Zruog", 3, "decrypt"),
        ("Python Programming", 5, "encrypt"),
        ("Udymts$Uwtlwfrrnsl", 5, "decrypt"),
        ("Caesar Cipher", 13, "encrypt"),
        ("Pnrfne$Pvcure", 13, "decrypt"),
        ("Test with numbers 123 and symbols !@#", 7, "encrypt"),
        ("sharky01 is a h@cker", 11, "encrypt"),
        ("Password123!@#", 5, "encrypt"),
        ("Special chars: !@#$%^&*()", 10, "encrypt"),
    ]
    
    for i, (message, shift, mode) in enumerate(test_cases, 1):
        result = caesar_cipher(message, shift, mode)
        print(f"Test {i}:")
        print(f"  Original: {message}")
        print(f"  Mode: {mode}, Shift: {shift}")
        print(f"  Result: {result}")
        print()
    
    # Test round-trip encryption/decryption
    print("Round-trip test (encrypt then decrypt):")
    original = "This is a test message!"
    shift = 10
    encrypted = caesar_cipher(original, shift, "encrypt")
    decrypted = caesar_cipher(encrypted, shift, "decrypt")
    
    print(f"  Original: {original}")
    print(f"  Encrypted: {encrypted}")
    print(f"  Decrypted: {decrypted}")
    print(f"  Round-trip successful: {original == decrypted}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_caesar_cipher()
