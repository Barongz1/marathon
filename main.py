"""One-Liner Marathon — entry for make.fun.

Writes one line to /output/entry.txt. The line is one comedy joke up to 280 characters, on any subject.
"""
import os

LINE = "My smart home is so smart it filed a restraining order against me. Apparently opening the fridge at 3 AM counts as harassment."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
