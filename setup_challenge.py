import os
import socket
import hashlib

SECRET_SALT = "CS101_Fall2026_Key"
file_path = "challenge.txt"
meta_file = ".student_id"

def get_ip():
    """Detects the active network IP of the VM."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# 1. Prompt for student identifier
username = input("Enter your student username or ID: ").strip().lower()
if not username:
    print("Error: Username cannot be empty.")
    exit(1)

# 2. Get current VM IP address and calculate unique hash
student_ip = get_ip()
raw_data = f"{username}:{student_ip}:{SECRET_SALT}"
token = hashlib.sha256(raw_data.encode()).hexdigest()[:8].upper()

# 3. Write challenge content
with open(file_path, "w") as f:
    f.write(f"=== CHMOD LAB FOR USER: {username} ===\n")
    f.write("Task 1 (Read): You successfully unlocked this file!\n")
    f.write(f"Your unique completion token is: {token}\n\n")
    f.write("Task 2 (Write): Append the exact line below to the end of this file:\n")
    f.write(f"COMPLETED: {username} - {token}\n")

# 4. Save metadata for verification
with open(meta_file, "w") as f:
    f.write(f"{username}\n")

# 5. Lock permissions completely (000)
os.chmod(file_path, 0o000)

print(f"\nLab setup complete for '{username}' on IP {student_ip}.")
print(f"'{file_path}' created with 000 permissions. Use chmod to proceed.")
