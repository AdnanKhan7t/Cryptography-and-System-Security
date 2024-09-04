import math

def decrypt_columnar_transposition(cipher, key):
    """
    Decrypt a message encrypted with the Columnar Transposition Cipher.

    Parameters:
    - cipher (str): The encrypted message to decrypt.
    - key (str): The key used during the encryption.

    Returns:
    - str: The decrypted plaintext message.
    """
    msg_len = len(cipher)
    num_cols = len(key)
    num_rows = int(math.ceil(msg_len / num_cols))
    
    # Create a matrix to hold the decrypted text
    decrypted_matrix = [[''] * num_cols for _ in range(num_rows)]
    
    # Determine the column order based on the sorted key
    sorted_key = sorted(key)
    
    index = 0
    for col in sorted_key:
        col_index = key.index(col)
        for row in range(num_rows):
            if index < msg_len:
                decrypted_matrix[row][col_index] = cipher[index]
                index += 1
    
    # Flatten the matrix to retrieve the plaintext
    decrypted_message = ''.join(sum(decrypted_matrix, []))
    
    # Remove padding characters
    return decrypted_message.rstrip('_')

if __name__ == "__main__":
    encrypted_msg = input("Enter the encrypted message to decrypt: ")
    key = input("Enter the key for decryption: ")
    decrypted_msg = decrypt_columnar_transposition(encrypted_msg, key)
    print(f"Decrypted Message: {decrypted_msg}")
