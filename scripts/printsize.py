import os
import re

def print_size():
    print("{:>18} {:>18}".format("File", "Size(MB)"))
    for i in os.walk("."):
        for j in i:
            if isinstance(j, list) and j:
                for file in j:
                    if ".csv" in file or ".db" in file:
                        print("{:>18} {:>18}".format(file, (os.path.getsize(os.path.join(directory, file)) / 1000000)))
            if isinstance(j, str):
                directory = j


def script_information():
    py = re.compile(".py$")
    print("{:>18}".format("File"))
    for i in os.walk("."):
        for j in i:
            if isinstance(j, list) and j:
                for file in j:
                    if py.search(file):
                        print("{:>18}".format(file))


if __name__ == "__main__":
    print_size()
    script_information()
