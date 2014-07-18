#!/usr/bin/env python
# encoding: utf-8
#
# usage: check_totals.py [-h] json
#
# Print the aggregates from an Open Diversity Data JSON file to check the totals
# against the PDF.
#
# positional arguments:
#   json        Open Diversity Data JSON file to check totals on
#
# optional arguments:
#   -h, --help  show this help message and exit

from __future__ import print_function

import json
import argparse

def main():
    parser = argparse.ArgumentParser(description='Print the aggregates from an Open Diversity Data JSON file to check the totals against the PDF.')
    parser.add_argument('json', action='store', help='Open Diversity Data JSON file to check totals on')
    args = parser.parse_args()

    if not args.json:
        print()
        print("Sorry, you need to provide some data for me to aggregate :(")
        print()
        exit()
    
    jsondata = json.load(open(args.json, 'rU'))['section_d']

    job_categories = [
        "Executive/Senior Level Officials and Managers",
        "First/Mid Level Officials and Managers",
        "Professionals",
        "Technicians",
        "Sales Workers",
        "Administrative Support Workers",
        "Craft Workers",
        "Operatives",
        "Laborers and Helpers",
        "Service Workers"
    ]

    races = [
        "Hispanic or Latino",
        "White",
        "Black or African American",
        "Native Hawaiian or Other Pacific Islander",
        "Asian",
        "American Indian or Alaska Native",
        "Two or More Races"
    ]

    overall_totals = {}
    race_totals = {}

    for cat in job_categories:
        data = None
        for obj in jsondata:
            if obj['job_category'] == cat:
                data = obj['data']
        if data:
            total = 0
            for datum in data:
                total += datum['men'] + datum['women']
            overall_totals[cat] = total

        for race in races:
            race_data = None
            for inner_obj in data:
                if inner_obj['race'] == race:
                    race_data = inner_obj
            try:
                current = race_totals[race]
                current['men'] += race_data['men']
                current['women'] += race_data['women']
            except KeyError:
                race_totals[race] = {'men': race_data['men'], 'women': race_data['women']}


    print()
    print("### Overall Totals ###")
    for cat in job_categories:
        print("%s: %d" %(cat, overall_totals[cat]))
    print("Absolute total: %d" %sum([overall_totals[cat] for cat in job_categories]))
    print()
    print("### Totals by Race and Gender ###")
    hispanic = races.pop(0)
    print(hispanic, ': Men %d, Women %d' %(race_totals[hispanic]['men'], race_totals[hispanic]['women']))
    print("Non-Hispanic or Latino, Men:")
    for race in races:
        print("\t%s: %d" %(race, race_totals[race]['men']))
    print("Non-Hispanic or Latino, Women:")
    for race in races:
        print("\t%s: %d" %(race, race_totals[race]['women']))
    print()
    
if __name__ == '__main__':
    main()