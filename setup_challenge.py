import os
import hashlib

# Update this secret key for your course/term
SECRET_SALT = "CS101_Fall2026_Key"
file_path = "challenge.txt"
meta_file = ".student_id"

username = input("Enter your student username or ID: ").strip().lower()
if not username:
    print("Error: Username cannot be empty.")
    exit(1)

# Generate an 8-character unique hash token
token = hashlib.sha256(f"{username}:{SECRET_SALT}".encode()).hexdigest()[:8].upper()

# Create the locked file content
with open(file_path, "w") as f:
    f.write(f"=== CHMOD LAB FOR USER: {username} ===\n")
    f.write("Task 1 (Read): You successfully unlocked this file!\n")
    f.write(f"Your unique completion token is: {token}\n\n")
    f.write("Task 2 (Write): Append the exact line below to the end of this file:\n")
    f.write(f"COMPLETED: {username} - {token}\n")

# Store username locally for check_solution.py
with open(meta_file, "w") as f:
    f.write(username)

# Strip all permissions (000)
os.chmod(file_path, 0o000)

print(f"\nLab setup complete for student '{username}'.")
print(f"'{file_path}' has been created with 000 permissions. Use chmod to proceed.")
