import os
import csv
import sys
import requests
from tqdm import tqdm

def download_file(url, dest_path):
    """Downloads a file from a URL to a destination path with a progress bar."""
    dest_filename = os.path.basename(dest_path)
    if os.path.exists(dest_path):
        print(f"{dest_filename} ✔️")
        return

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    try:
        response = requests.get(url, stream=True, allow_redirects=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(dest_path, 'wb') as f, tqdm(
            desc=f"Downloading {dest_filename}",
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            file=sys.stdout,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        if os.path.exists(dest_path):
            os.remove(dest_path) # Clean up partial file

def main():
    """Reads the CSV and downloads the models."""
    models_csv_path = 'models.csv'
    models_base_dir = 'models'

    if not os.path.exists(models_csv_path):
        print(f"Models manifest not found at {models_csv_path}", file=sys.stderr)
        return

    with open(models_csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row.get('url')
            dest_rel_path = row.get('dest')
            if url and dest_rel_path:
                dest_abs_path = os.path.join(models_base_dir, dest_rel_path)
                download_file(url, dest_abs_path)

if __name__ == "__main__":
    main()