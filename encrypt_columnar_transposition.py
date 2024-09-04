import math

def encrypt_columnar_transposition(plaintext, key):
    key = str(key)
    msg_len = len(plaintext)
    num_cols = len(key)
    num_rows = math.ceil(msg_len / num_cols)
    
    padded_msg = plaintext + '_' * (num_cols * num_rows - msg_len)
    
    matrix = [padded_msg[i:i + num_cols] for i in range(0, len(padded_msg), num_cols)]
    
    sorted_key = sorted(key)
    cipher = []
    
    for sorted_col_idx in range(num_cols):
        actual_col_idx = key.index(sorted_key[sorted_col_idx])
        cipher.extend([matrix[row][actual_col_idx] for row in range(num_rows)])
    
    return "".join(cipher)

if __name__ == "__main__":
    plaintext = input("Enter the message to encrypt: ")
    key = input("Enter the key for encryption: ")
    
    if not key:
        print("Error: Key cannot be empty.")
    elif len(key) < 2:
        print("Error: Key must contain at least two characters.")
    else:
        encrypted_message = encrypt_columnar_transposition(plaintext, key)
        print(f"Encrypted Message: {encrypted_message}")
