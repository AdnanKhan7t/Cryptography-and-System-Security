import math
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def calculate_frequencies(text):
    text = text.upper().replace(" ", "")
    counter = Counter(text)
    total_letters = sum(counter.values())
    frequencies = {char: (count / total_letters) * 100 for char, count in counter.items()}
    return frequencies

def plot_frequencies(plain_freq, rail_freq, columnar_freq):
    all_letters = sorted(set(plain_freq.keys()).union(rail_freq.keys()).union(columnar_freq.keys()))
    plain_values = [plain_freq.get(letter, 0) for letter in all_letters]
    rail_values = [rail_freq.get(letter, 0) for letter in all_letters]
    columnar_values = [columnar_freq.get(letter, 0) for letter in all_letters]
    
    bar_width = 0.25
    r1 = np.arange(len(all_letters))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    plt.figure(figsize=(14, 8))
    plt.bar(r1, plain_values, color='blue', width=bar_width, edgecolor='grey', label='Plaintext')
    plt.bar(r2, rail_values, color='green', width=bar_width, edgecolor='grey', label='Rail Fence Cipher')
    plt.bar(r3, columnar_values, color='red', width=bar_width, edgecolor='grey', label='Columnar Cipher')
    
    plt.xlabel('Letters', fontweight='bold')
    plt.ylabel('Relative Frequency (%)', fontweight='bold')
    plt.title('Letter Frequencies: Plaintext vs Rail Fence Cipher vs Columnar Cipher')
    plt.xticks([r + bar_width for r in range(len(all_letters))], all_letters)
    plt.legend()
    plt.grid(True, axis='y')
    plt.savefig("frequency_plot_relative.png")
    plt.show()

def encrypt_rail_fence(text, num_rails):
    rail_matrix = [['\n' for _ in range(len(text))] for _ in range(num_rails)]
    down_direction = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == num_rails - 1:
            down_direction = not down_direction
        
        rail_matrix[row][col] = char
        col += 1
        row += 1 if down_direction else -1

    encrypted_text = []
    for r in range(num_rails):
        encrypted_text.extend([rail_matrix[r][c] for c in range(len(text)) if rail_matrix[r][c] != '\n'])
    
    return "".join(encrypted_text)

def encrypt_columnar_transposition(msg, key):
    msg_len = len(msg)
    num_cols = len(key)
    num_rows = math.ceil(msg_len / num_cols)
    padded_msg = msg + '_' * (num_cols * num_rows - msg_len)
    matrix = [padded_msg[i:i + num_cols] for i in range(0, len(padded_msg), num_cols)]
    sorted_key = sorted(key)
    cipher = []
    
    for col_idx in range(num_cols):
        current_col = key.index(sorted_key[col_idx])
        cipher.extend([matrix[row][current_col] for row in range(num_rows)])
    
    return "".join(cipher)

if __name__ == "__main__":
    plaintext = "The quick brown fox jumps over the lazy dog"
    rail_fence_ciphertext = encrypt_rail_fence(plaintext, 5)
    columnar_ciphertext = encrypt_columnar_transposition(plaintext, "monarch of flames")
    
    plain_freq = calculate_frequencies(plaintext)
    rail_freq = calculate_frequencies(rail_fence_ciphertext)
    columnar_freq = calculate_frequencies(columnar_ciphertext)
    
    plot_frequencies(plain_freq, rail_freq, columnar_freq)
