def decrypt_rail_fence(cipher, num_rails):
    """
    Decrypt a message encrypted with the Rail Fence Cipher.

    Parameters:
    - cipher (str): The encrypted message to decrypt.
    - num_rails (int): The number of rails used during encryption.

    Returns:
    - str: The decrypted plaintext message.
    """
    # Create a matrix to determine the pattern of rails
    rail_matrix = [['\n' for _ in range(len(cipher))] for _ in range(num_rails)]
    
    # Set direction and position
    down_direction = None
    row, col = 0, 0
    
    # Mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            down_direction = True
        elif row == num_rails - 1:
            down_direction = False
            
        rail_matrix[row][col] = '*'
        col += 1
        row += 1 if down_direction else -1
    
    # Fill the matrix with the cipher text
    index = 0
    for r in range(num_rails):
        for c in range(len(cipher)):
            if rail_matrix[r][c] == '*' and index < len(cipher):
                rail_matrix[r][c] = cipher[index]
                index += 1
                
    # Read the matrix in a zigzag manner to decrypt the message
    decrypted_text = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            down_direction = True
        elif row == num_rails - 1:
            down_direction = False
        
        if rail_matrix[row][col] != '*':
            decrypted_text.append(rail_matrix[row][col])
            col += 1
            
        row += 1 if down_direction else -1
        
    return "".join(decrypted_text)

if __name__ == "__main__":
    encrypted_text = input("Enter the encrypted text to decrypt: ")
    key = int(input("Enter the number of rails for decryption: "))
    decrypted_text = decrypt_rail_fence(encrypted_text, key)
    print(f"Decrypted Message: {decrypted_text}")
