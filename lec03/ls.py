import sys
import os

def search_filesystem(filename):
    return filename in os.listdir()


if __name__ == "__main__":
    search_filesystem(sys.argv[-1])
