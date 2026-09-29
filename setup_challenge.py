import os
import socket

file_path = "challenge.txt"
meta_file = ".student_id"

# 1. Prompt for student identifier
username = input("Enter your GNPS Username: ").strip().lower()
if not username:
    print("Error: Username cannot be empty.")
    exit(1)

# 2. Save metadata for verification script
with open(meta_file, "w") as f:
    f.write(f"{username}\n")

# 3. Write target permission instructions inside challenge.txt
with open(file_path, "w") as f:
    f.write(f"=== CHMOD LAB FOR USER: {username} ===\n\n")
    f.write("STEP 1 COMPLETE: You successfully figured out how to read this file!\n\n")
    f.write("STEP 2 TASK:\n")
    f.write("Modify the permissions of 'challenge.txt' to match these exact settings:\n")
    f.write("  - Owner (User): Read, Write, Execute\n")
    f.write("  - Group:        Read, Write\n")
    f.write("  - Others:       Read Only\n\n")
    f.write("Once you set the correct permissions for 'challenge.txt', run:\n")
    f.write("  ./check_solution\n")

# 4. Lock file down completely (000 permissions)
os.chmod(file_path, 0o000)

print(f"\nLab initialized for '{username}'.")
print("------------------------------------------------------------------")
print("Challenge started: 'challenge.txt' has been created with NO permissions.")
print("Figure out how to grant yourself read access to view the file contents!")
print("------------------------------------------------------------------")
