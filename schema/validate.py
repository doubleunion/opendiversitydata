#!/usr/bin/env python
# encoding: utf-8
#
# usage: validate.py [-h] [-s SCHEMA] [-d DATA]
#
# Validate a JSON data file against a specified JSON Schema.
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -s SCHEMA, --schema SCHEMA
#                         name of JSON Schema file
#   -d DATA, --data DATA  name of JSON data file
#
# NB: when validation fails, output is much easier to read if you're using Python 3.*
# but in general this works in Python 2 as well

from __future__ import print_function

import json
import jsonschema
import argparse

def main():
    parser = argparse.ArgumentParser(description='Validate a JSON data file against a specified JSON Schema.')
    parser.add_argument('-s', '--schema', action='store', dest='schema', help='name of JSON Schema file')
    parser.add_argument('-d', '--data', action='store', dest='data', help='name of JSON data file')
    args = parser.parse_args()

    if not args.data:
        print()
        print("You need to pass me a data file to validate, teapot. >:(")
        print()
        exit()
    if not args.schema:
        print()
        print("You need to pass me a schema to use for validation, teapot. >:(")
        print()
        exit()

    data = json.load(open(args.data, 'rU'))
    
    schema = json.load(open(args.schema, 'rU'))

    jsonschema.validate(data, schema)

if __name__ == '__main__':
    main()
