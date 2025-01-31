import subprocess
import os
import re

# Define paths
source = r"E:\System Folders\Documents\Informatik Studium\Informatik Studium\Lernzettel"
destination = r"C:\Users\Lukas\quartz\content"

# Run xcopy command
subprocess.run(f'xcopy "{source}" "{destination}" /E /C /H /Y', shell=True)

# Function to clean markdown files
def remove_h1_lines(directory):
    h1_pattern = re.compile(r"^#\s+.*")  # Matches lines starting with "#" followed by a space and text

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Only process markdown files
                file_path = os.path.join(root, file)

                # Read file and filter lines
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # Remove H1 lines
                new_lines = [line for line in lines if not h1_pattern.match(line)]

                # Write the cleaned content back
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)

# Run cleanup
remove_h1_lines(destination)

print("all H1 headers removed.")

# Run npx quartz sync
subprocess.run("npx quartz sync", shell=True)
