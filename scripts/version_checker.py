import xml.etree.ElementTree as ET

def version_checker(filename):
    for _, elem in ET.iterparse(filename):
        if elem.tag == "node":
            try:
                int(elem.attrib["version"])
            except ValueError:
                print("There is a piece of data that cannot be converted to the integer")
                break
    print("Any errors have occurred")

if __name__ == "__main__":
    version_checker("wroclaw")