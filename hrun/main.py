"""
Examples:
    hrun use 3.1.12 3.2.2 -- python app.py
    hrun use 3.1.12 3.2.2 -- time python app.py
    hrun use 3.1.12 3.2.2 -- python -m timeit app.py
    # discover case apps and run against versions
    hrun use 3.1.12 3.2.2 --case-dirs cases --entrypoint app.py
"""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser("history-runner")
    print("Hello world!")
    return 0


if __name__ == "__main__":
    exit(main())
