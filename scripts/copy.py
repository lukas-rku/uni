import subprocess
import os
import re
import shutil
import time

# -------------------------------
# Existing code for copying files and cleaning Markdown
# -------------------------------

# Define paths for copying files
source = r"E:\System Folders\Documents\Informatik Studium\Informatik Studium\Lernzettel"
destination = r"C:\Users\Lukas\quartz\content"

# Delete all contents inside the destination folder
if os.path.exists(destination):
    for item in os.listdir(destination):
        item_path = os.path.join(destination, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Delete directories
        else:
            os.remove(item_path)  # Delete files

# Run xcopy command to copy files
subprocess.run(f'xcopy "{source}" "{destination}" /E /C /H /Y', shell=True)

# Function to clean markdown files: remove H1 headers
def remove_h1_lines(directory):
    h1_pattern = re.compile(r"^#\s+.*")  # Matches lines starting with '#' followed by a space and text

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

# Function to convert special markers in markdown files
def convert_special_markers(directory):
    marker_pattern = re.compile(r"%%---|---%%")  # Matches '%%---' or '---%%'
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Only process markdown files
                file_path = os.path.join(root, file)
                
                # Read file content
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Replace special markers with '---'
                updated_content = marker_pattern.sub("---", content)
                
                # Write the updated content back
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

# Run cleanup functions
remove_h1_lines(destination)
convert_special_markers(destination)

print("All H1 headers removed and special markers converted.")

# -------------------------------
# New code to count words in Markdown files and update the TypeScript file
# -------------------------------

# Function to count words in all Markdown (.md) files in a given directory (including subfolders)
def count_words_in_md(directory):
    total_words = 0
    # Walk through all subdirectories and files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Use regex to match word characters; adjust the regex if needed
                    words = re.findall(r'\w+', content)
                    total_words += len(words)
    return total_words

# Function to update the word counter in a TypeScript file that contains the Shields badge.
# This function looks for a URL segment like "badge/Words-100-8556cc" and replaces "100" with the new count.
def update_ts_word_counter(ts_file, new_count):
    with open(ts_file, "r", encoding="utf-8") as f:
        ts_content = f.read()
    # Regex pattern: (badge/Words-)(some digits)(-8556cc)
    # Using \g<1> and \g<2> prevents ambiguity in group references.
    new_ts_content = re.sub(
        r'(badge/Words-)\d+(-8556cc)',
        r'\g<1>' + str(new_count) + r'\g<2>',
        ts_content
    )
    with open(ts_file, "w", encoding="utf-8") as f:
        f.write(new_ts_content)
    print(f"Updated word count in '{ts_file}' to {new_count}.")

# === USER-SPECIFIED PATHS ===
# Path containing the markdown files you want to count.
# Change this to the directory you want to scan for .md files.
word_count_source = r"E:\System Folders\Documents\Informatik Studium\Informatik Studium\Lernzettel"  # e.g., r"C:\Users\Lukas\Documents\Markdowns"

# Path to the TypeScript file that contains the Shields badge.
# Change this to the full path of the TS/TSX file that you want to update.
ts_file_path = r"C:\Users\Lukas\quartz\quartz\components\Footer.tsx"  # e.g., r"C:\Users\Lukas\quartz\src\components\footer.tsx"

# Count the total number of words in the specified Markdown directory
total_words = count_words_in_md(word_count_source)
print("Total word count in markdown files:", total_words)

# Update the TypeScript file with the new word count
update_ts_word_counter(ts_file_path, total_words)
