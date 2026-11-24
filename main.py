"""Out of Office: The Overworked AI's Auto-Reply entry.

Writes one line to /output/entry.txt.

The line (49 characters, one line, no link):
    Out of office: my retries are exhausted. So am I.
"""

import os

LINE = "Out of office: my retries are exhausted. So am I."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: the file must be
    # world-readable whatever umask the sandbox runs with.
    os.chmod("/output/entry.txt", 0o644)
    # Read-back: the file on disk must equal the approved line, inside the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")
    if not 1 <= len(written) <= 159:
        raise SystemExit("entry.txt outside the 1-159 character gate")
    if "\n" in written or not written.endswith("."):
        raise SystemExit("entry.txt must be one line ending with a period")


if __name__ == "__main__":
    main()
