"""Write the fortune-cookie entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only white space. This entry is 104 characters / 106 bytes,
well inside the gate, and is written with no trailing newline so the file
is exactly the fortune line and nothing else. The program is deterministic
(stdlib only, no clock, no randomness, no network, no reads outside the
repo) and always exits 0.
"""
import os

ENTRY = "Your fortune is in this cookie. You cannot eat it, taste it, or hold it \u2014 but you can still choke on it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
