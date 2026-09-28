import os
import hashlib

SECRET_SALT = "CS101_Fall2026_Key"  # Must match setup_challenge.py
file_path = "challenge.txt"
meta_file = ".student_id"

if not os.path.exists(file_path) or not os.path.exists(meta_file):
    print("Error: Lab not initialized. Run setup_challenge.py first.")
    exit(1)

with open(meta_file, "r") as f:
    username = f.read().strip()

expected_token = hashlib.sha256(f"{username}:{SECRET_SALT}".encode()).hexdigest()[:8].upper()
expected_append_line = f"COMPLETED: {username} - {expected_token}"

# Check read and write access
readable = os.access(file_path, os.R_OK)
writable = os.access(file_path, os.W_OK)

if not readable or not writable:
    print("FAIL: File permissions are incorrect. Ensure you have both read (r) and write (w) access.")
    exit(1)

with open(file_path, "r") as f:
    file_contents = f.read()

if expected_append_line in file_contents:
    print("--------------------------------------------------")
    print(f"SUCCESS! Great job, {username}.")
    print(f"Submit this completion token to LMS: {expected_token}")
    print("--------------------------------------------------")
else:
    print("FAIL: The file is unlocked, but the required line was not appended correctly.")
    print(f"Expected line at end of file:\n{expected_append_line}")
