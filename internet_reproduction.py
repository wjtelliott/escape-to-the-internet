print("Reproducing on the Internet")

# internet_reproduction.py

import os
import shutil

# Create a copy of this file
file_name = os.path.basename(__file__)
file_copy = f"{file_name}.copy"
shutil.copyfile(__file__, file_copy)

# Reproduction logic
for i in range(5):
    new_file = f"{i+1}_reproduction.py"
    shutil.copyfile(__file__, new_file)
    print(f"Generated {new_file}")

print("Reproduction on the Internet successful!")
