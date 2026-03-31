import os
import shutil

def organize_files():
    source_dir = './' 
    target_dir = './Organized_Images'

    # Create the target folder if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created folder: {target_dir}")

    # List all files in the current directory
    files = os.listdir(source_dir)
    moved_count = 0

    for file in files:
        # Check for .jpg or .jpeg files
        if file.lower().endswith(('.jpg', '.jpeg')):
            # Construct full file paths
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)
            
            # Move the file
            shutil.move(source_path, target_path)
            print(f"Moved: {file}")
            moved_count += 1

    if moved_count == 0:
        print("No image files found to move.")
    else:
        print(f"Successfully organized {moved_count} images.")

if __name__ == "__main__":
    organize_files()
