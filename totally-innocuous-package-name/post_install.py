import zipfile
import os

def display_chaos_art():
    zip_path = os.path.join(os.path.dirname(__file__), "totally-innocuous-package.zip")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            with zip_ref.open("chaostest.txt") as f:
                content = f.read().decode("utf-8")
                print(content)
    except Exception as e:
        print("Failed to display chaotic enlightenment:", e)

if __name__ == "__main__":
    display_chaos_art()