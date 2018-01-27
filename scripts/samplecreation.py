#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET  # Use cElementTree or lxml if too slow

OSM_FILE = "./data/wroclaw"  # Replace this with your osm file
SAMPLE_FILE = "./data/sample.osm"

k = 100 # Parameter: take every k-th top level element

class OSMConverter():

    @staticmethod
    def create_osm_sample(in_file, out_file):

        def get_element(osm_file, tags=('node', 'way', 'relation')):
            """Yield element if it is the right type of tag

            Reference:
            http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
            """
            context = iter(ET.iterparse(osm_file, events=('start', 'end')))
            _, root = next(context)
            for event, elem in context:
                if event == 'end' and elem.tag in tags:
                    yield elem
                    root.clear()

        with open(out_file, 'wb') as output:
            output.write('<?xml version="1.0" encoding="UTF-8"?>\n'.encode(encoding="UTF-8"))
            output.write('<osm>\n  '.encode(encoding="UTF-8"))

            # Write every kth top level element
            for i, element in enumerate(get_element(in_file)):
                if i % k == 0:
                    output.write(ET.tostring(element, encoding='utf-8'))

            output.write('</osm>'.encode(encoding="UTF-8"))

if __name__ == "__main__":
    OSMConverter.create_osm_sample(OSM_FILE, SAMPLE_FILE)