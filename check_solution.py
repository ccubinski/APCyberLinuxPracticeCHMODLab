import os
import stat
import socket
import hashlib

SECRET_SALT = "CS101_Fall2026_Key"
file_path = "challenge.txt"
meta_file = ".student_id"
EXPECTED_OCTAL = 0o764  # User: rwx (7), Group: rw- (6), Others: r-- (4)

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

# 1. Verify required lab files exist
if not os.path.exists(file_path) or not os.path.exists(meta_file):
    print("Error: Lab files missing. Run setup_challenge first.")
    exit(1)

with open(meta_file, "r") as f:
    username = f.read().strip()

# 2. Inspect current permissions of challenge.txt
file_stat = os.stat(file_path)
current_permissions = stat.S_IMODE(file_stat.st_mode)

if current_permissions != EXPECTED_OCTAL:
    actual_octal = oct(current_permissions)[2:].zfill(3)
    print(f"FAIL: Current permissions are not correct. Please review the instructions and/or Linux Commands.")
    exit(1)

# 3. Generate unique verification token upon passing permission test
student_ip = get_ip()
raw_data = f"{username}:{student_ip}:{SECRET_SALT}"
expected_token = hashlib.sha256(raw_data.encode()).hexdigest()[:8].upper()

print("--------------------------------------------------")
print(f"SUCCESS! Target permissions verified for '{username}'.")
print("Submit the following TWO items to your LMS portal:")
print(f"  1. Completion Token: {expected_token}")
print(f"  2. VM IP Address:    {student_ip}")
print("--------------------------------------------------")
