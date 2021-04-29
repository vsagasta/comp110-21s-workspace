import os

def traverse(path: str) -> None:
    """Recursive function that prints out all of the files and directories in our workspace."""
    # Base Case
    if os.path.isfile(path):
        print(f"file: {path}")
    else:
        # Recursive Case
        # When path refers to directory name
        print(f"dir: {path}")
        for child_path in os.listdir(path):
            traverse(os.path.join(path, child_path))

traverse("exercises")
# traverse("comp110-21s-workspace")

# python -m lessons.ls27_files