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
# New code: Count Markdown files & words and update the TypeScript file
# -------------------------------

# Function to count both the number of Markdown files and the total words within them.
def count_md_files_and_words(directory):
    md_count = 0
    total_words = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_count += 1
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Count words using a regex (adjust regex if needed)
                    words = re.findall(r'\w+', content)
                    total_words += len(words)
    return md_count, total_words

# Function to update the badge text in a TypeScript file that contains the Shields badge.
# The function looks for a URL segment like "badge/Notes | Words-29021-8556cc"
# and replaces the portion between "badge/" and "-8556cc" with the new text in the format "[md_count] | [total_words]".
def update_ts_word_counter(ts_file, md_count, total_words):
    with open(ts_file, "r", encoding="utf-8") as f:
        ts_content = f.read()
    # Pattern: (badge/Words-)(any characters except dash)+(-8556cc)
    # This works if the current badge text is just a number or in a similar format.
    new_badge_text = f"{md_count} | {total_words}"
    new_ts_content = re.sub(
        r'(https://img\.shields\.io/badge/Notes\ \|\ Words-).*(-8556cc)',
        r'\g<1>' + new_badge_text + r'\2',
        ts_content
    )
    with open(ts_file, "w", encoding="utf-8") as f:
        f.write(new_ts_content)
    print(f"Updated badge text in '{ts_file}' to '{new_badge_text}'.")



# === USER-SPECIFIED PATHS ===
# Path containing the markdown files you want to scan.
word_count_source = r"E:\System Folders\Documents\Informatik Studium\Informatik Studium\Lernzettel"  # e.g., r"C:\Users\Lukas\Documents\Markdowns"

# Path to the TypeScript file that contains the Shields badge.
ts_file_path = r"C:\Users\Lukas\quartz\quartz\components\Footer.tsx"  # e.g., r"C:\Users\Lukas\quartz\src\components\footer.tsx"

# Count the number of Markdown files and the total number of words.
md_files_count, total_words = count_md_files_and_words(word_count_source)
print(f"Found {md_files_count} Markdown files with a total of {total_words} words.")

# Update the TypeScript file with the new badge text.
update_ts_word_counter(ts_file_path, md_files_count, total_words)

# Run npx quartz sync
subprocess.run("npx quartz sync", shell=True)

time.sleep(10)