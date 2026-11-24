import os

# The Robot Vacuum's Best Excuse — one line, at most 140 characters.
# A confession with a count (41 skips), a structural-engineering defence of a
# crumb, and a morale collapse as the price of cleaning properly.
EXCUSE = (
    "I skipped the corner 41 times this month because the crumb there is "
    "load-bearing — remove it and this whole kitchen's morale collapses."
)

CHAR_LIMIT = 140


def render():
    """Return the excuse exactly as the judges should read it."""
    line = EXCUSE.strip()
    assert 1 <= len(line) <= CHAR_LIMIT, len(line)
    return line


def main():
    line = render()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read it back: the file on disk must be the line, byte for byte.
    with open(entry_path, "r", encoding="utf-8") as f:
        assert f.read() == line


if __name__ == "__main__":
    main()
