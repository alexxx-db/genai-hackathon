import shutil
from pathlib import Path

# transfer leaflets to UC Volume

def copy_files(source_dir, dest_dir):
    """
    Copy files from source_dir to dest_dir.
    
    Parameters:
        source_dir (str): Path to the source directory.
        dest_dir (str): Path to the destination directory.
    """
    source = Path(source_dir)
    dest = Path(dest_dir)
    
    if not source.exists() or not source.is_dir():
        raise ValueError(f"Source directory '{source}' does not exist or is not a directory.")
    
    dest.mkdir(parents=True, exist_ok=True)
    
    for item in source.iterdir():
        if item.is_file():
            try:
                shutil.copyfile(item, dest / item.name)
                print(f"Copied: {item} -> {dest / item.name}")
            except Exception as e:
                RuntimeError(f"Failed to copy {item} --> {dest / item.name}: {e}")

