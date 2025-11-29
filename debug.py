# save as write_example.py
from pathlib import Path

def write_score(file_path, text):
    with open(file_path, "a") as f:
        f.write(text + "\n")   # <-- set a breakpoint on this line or the next
    # break here to inspect file contents
    return Path(file_path).stat().st_size

if __name__ == "__main__":
    out = "TeamA 120/4 in 20.0 overs"
    size = write_score("score.txt", out)
    print("Wrote bytes:", size)
