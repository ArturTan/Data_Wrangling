#/usr/bin/python3

import pandas as pd
import csv

nodes_tags = pd.read_csv("nodes_tags.csv")
ways_tags = pd.read_csv("ways_tags.csv")

def streetmapping(file,
                  street_code={},
                  weirds=[]):
    dataset = pd.read_csv(file)
    streets = pd.DataFrame(dataset[dataset.key == "street"])
    sym_ul = pd.DataFrame(dataset[dataset.key == "street:sym_ul"])

    for num, i in zip(streets.index, streets.id):
        checker = 0
        for num_sec, j in zip(sym_ul.index, sym_ul.id):
            if i == j:
                street_code[streets.get_value(num, "value")] = sym_ul.get_value(num_sec, "value")
                checker = 1
                break
        if checker:
            continue
        weirds.append(streets.get_value(num, "value"))

    return weirds

if __name__ == "__main__":
    street_code = {}
    weirds = []
    for i in ["nodes_tags.csv", "ways_tags.csv"]:
        streetmapping(i, street_code, weirds)
    print("Streets without sym_ul: ")
    for i in weirds:
        try:
            street_code[i]
        except KeyError:
            print("\t", i)
    # Adama Mickiewicza - 12740
    # Na Niskich Łąkach - 13632
    # Grabarska - 06006
    street_code["Adama Mickiewicza"] = "12740"
    street_code["Na Niskich Łąkach"] = "13632"
    street_code["Grabarska"] = "06006"

    print("Saving to csv")
    with open("street_mapping.csv", 'w') as f:
        fieldnames = ["Street", "Sym_ul"]
        writer = csv.DictWriter(f,
                                fieldnames=fieldnames)
        writer.writeheader()
        data = [dict(zip(fieldnames, [k, v])) for k, v in street_code.items()]
        writer.writerows(data)


