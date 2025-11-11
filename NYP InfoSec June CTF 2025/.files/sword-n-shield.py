# Define the input text
cipher_text = """
SwordShieldSwordSwordShieldShieldShieldSword
SwordShieldSwordShieldShieldSwordSwordShield
SwordShieldSwordShieldSwordSwordSwordSword
SwordShieldShieldShieldShieldSwordShieldShield
SwordShieldShieldShieldSwordSwordSwordSword
SwordSwordShieldShieldSwordSwordSwordSword
SwordShieldShieldSwordShieldSwordShieldShield
SwordSwordShieldShieldSwordSwordShieldShield
SwordShieldShieldSwordShieldShieldSwordShield
SwordSwordShieldShieldSwordSwordSwordSword
SwordShieldShieldSwordShieldShieldShieldSword
SwordShieldSwordShieldShieldShieldShieldShield
SwordShieldShieldShieldSwordSwordShieldShield
SwordShieldShieldShieldSwordShieldShieldShield
SwordSwordShieldShieldSwordSwordSwordSword
SwordShieldShieldShieldSwordSwordShieldSword
SwordShieldShieldSwordSwordShieldSwordSword
SwordShieldSwordShieldShieldShieldShieldShield
SwordShieldShieldShieldSwordSwordShieldShield
SwordShieldShieldSwordShieldSwordSwordSword
SwordSwordShieldShieldSwordSwordSwordShield
SwordSwordShieldShieldSwordSwordShieldShield
SwordShieldShieldSwordShieldShieldSwordSword
SwordShieldShieldSwordSwordShieldSwordSword
SwordShieldShieldShieldShieldShieldSwordShield
"""

# Step 1: Convert each word to binary (Sword = 0, Shield = 1)
binary_string = cipher_text.replace("Sword", "0").replace("Shield", "1").replace("\n", "")

# Step 2: Split binary into 8-bit chunks
bytes_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

# Step 3: Convert binary to ASCII characters
decoded_chars = [chr(int(byte, 2)) for byte in bytes_list]

# Step 4: Join the characters into the decoded message
decoded_message = ''.join(decoded_chars)

# Print the result
print("Decoded message:", decoded_message)
