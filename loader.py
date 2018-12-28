'''
Author: Christos Plexidas
Email: plexae@gmail.com

CSV2SQLite

This is CSV to SQLite using a Json Input file as parameters including mapping.
This will create a local database quickly for you to run queries at
'''

import sqlite3
import json
import csv

param_file = 'params.json'

with open(param_file) as f:
    data = json.load(f)

conn = sqlite3.connect('step0_' + data["db"] + '.db')
c = conn.cursor()

def lenopenreadlines(filename,encoding):
    with open(filename, encoding=encoding, mode='r', errors='ignore') as f:
        return len(f.readlines())


def data_entry(loadtype,file_loc,columns,encoding_of_files,delimiter_set,active):

    if active:
        counter = 0
        query_create = 'CREATE TABLE IF NOT EXISTS ' + loadtype + ' (' + ','.join(columns) + ')'
        print(query_create)
        c.execute(query_create)

        f = open(file_loc,encoding=encoding_of_files, errors='ignore')

        counter = lenopenreadlines(file_loc,encoding_of_files)

        with f:
            reader = csv.reader(f, delimiter=delimiter_set)

            for row in reader:
                Ncounter = counter
                counter = counter - 1
                print(str(counter) + '/' + str(Ncounter))
                column_insert = "','".join(columns)
                row_insert = "','".join(row)
                row_insert.replace("''","'")
                row_to_insert = "INSERT INTO " + loadtype + "('" + column_insert + "') VALUES('" + row_insert +  "')"
                #print(row_to_insert)
                try:
                    c.execute(row_to_insert)
                    conn.commit()
                except sqlite3.Error as err:
                    print(err)
                    #logger.error(err.message) -- uncomment to log error


#run the query

data_entry(data['table_1']['type'],data['table_1']['filepath'],data['table_1']['columns'],data['table_1']['encoding_of_file'],data['table_1']['delimiter_set'],data['table_1']['active'])

c.close()
conn.close()


