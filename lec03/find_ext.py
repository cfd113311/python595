import sys
import os

def search_filesystem(file_ext):
    for filename in os.listdir():
        if file_ext == os.path.splitext(filename)[-1]:
            print("found:", filename)
            break
    else:
        print("none found.")


if __name__ == "__main__":
    search_filesystem(sys.argv[-1])
