#!/bin/sh env python

import sys
from arango import ArangoClient


def main(argv):
    # Check for price parameter
    if len(argv) >= 2:
        price = argv[1]
    else:
        print("Usage: aefilter.py <item price>")
        exit()

    # Connect to ArangoDB.
    client = ArangoClient(hosts='http://localhost:8529')
    aep_db = client.db(
        'ae_product', username='admin@ae_product', password='password')

    # Get a cursor to the document collection and print it
    cursor = aep_db.aql.execute(
        'FOR doc IN item_list FILTER doc.Price == ' + price + ' RETURN doc')
    items = [doc for doc in cursor]
    print(items)


if __name__ == "__main__":
    main(sys.argv)
