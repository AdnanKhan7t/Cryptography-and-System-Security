def encrypt_rail_fence(text, num_rails):
    """
    Encrypt a message using the Rail Fence Cipher.

    Parameters:
    - text (str): The plaintext message to encrypt.
    - num_rails (int): The number of rails for the Rail Fence Cipher.

    Returns:
    - str: The encrypted message.
    """
    # Create the rail matrix initialized with newlines
    rail_matrix = [['\n' for _ in range(len(text))] for _ in range(num_rails)]
    
    # Set the initial direction and position
    down_direction = False
    row, col = 0, 0
    
    # Fill the rail matrix with the characters from the text
    for char in text:
        if row == 0 or row == num_rails - 1:
            down_direction = not down_direction
        
        rail_matrix[row][col] = char
        col += 1
        row += 1 if down_direction else -1
    
    # Construct the cipher text by reading the rail matrix row by row
    encrypted_text = []
    for r in range(num_rails):
        for c in range(len(text)):
            if rail_matrix[r][c] != '\n':
                encrypted_text.append(rail_matrix[r][c])
    
    return "".join(encrypted_text)

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    
    # Validate the number of rails input
    while True:
        try:
            num_rails = int(input("Enter the number of rails for encryption: "))
            if num_rails < 2:
                print("Number of rails must be at least 2. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    encrypted_text = encrypt_rail_fence(text, num_rails)
    print(f"Encrypted Message: {encrypted_text}")
