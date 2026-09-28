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

# 1. Verify files exist
if not os.path.exists(file_path) or not os.path.exists(meta_file):
    print("Error: Lab files missing. Run setup_challenge first.")
    exit(1)

with open(meta_file, "r") as f:
    username = f.read().strip()

# 2. Check read access
readable = os.access(file_path, os.R_OK)

if not readable:
    print("FAIL: Permissions are incorrect. Ensure you have read (r) access to challenge.txt.")
    exit(1)

# 3. Calculate expected token using current VM IP address
student_ip = get_ip()
raw_data = f"{username}:{student_ip}:{SECRET_SALT}"
expected_token = hashlib.sha256(raw_data.encode()).hexdigest()[:8].upper()

# 4. Confirm file contains the valid token
with open(file_path, "r") as f:
    file_contents = f.read()

if expected_token in file_contents:
    print("--------------------------------------------------")
    print(f"SUCCESS! File is readable for user '{username}'.")
    print("Submit the following TWO items to your LMS portal:")
    print(f"  1. Completion Token: {expected_token}")
    print(f"  2. VM IP Address:    {student_ip}")
    print("--------------------------------------------------")
else:
    print("FAIL: Read permission set, but the file contents appear corrupted.")
