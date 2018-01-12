import sqlite3
import pandas as pd

import pyprind

def osm_importer(database=None):

    '''
    database must be a string
    '''

    data = pd.read_csv('{}.csv'.format(database))

    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    progress = pyprind.ProgBar(data.shape[0], monitor=True)

    for num, i in enumerate(range(data.shape[0])):
        progress.update()

        if database == "nodes":
            id_key, lat, lon, user, uid, version, changeset, timestamp = data.iloc[i]

            c.execute('''INSERT INTO nodes 
                        (id, lat, lon, user, uid, version, changeset, timestamp)
                        VALUES ({},{},{},'{}',{},{},{},'{}')'''.format(id_key,
                                                               lat,
                                                               lon,
                                                               user,
                                                               uid,
                                                               version,
                                                               changeset,
                                                               timestamp)
                      )
        elif database == "ways":
            id_key, user, uid, version, changeset, timestamp = data.iloc[i]
            c.execute('''INSERT INTO ways 
                        (id, user, uid, version, changeset, timestamp)
                        VALUES ({},'{}',{}, {},{},'{}')'''.format(id_key,
                                                          user,
                                                          uid,
                                                          version,
                                                          changeset,
                                                          timestamp)
                      )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    database = input("Name of database to be imported: ")
    osm_importer(database)
