#!/usr/bin/env python
# Command line script to convert a single given number to and from several units

import argparse
from src.convert import kilometers_to_miles, miles_to_kilometers, \
years_to__minutes, minutes_to_years

#parse args
parse = argparse.ArgumentParser()
parse.add_argument('value', type=float, help="Provide the number to be converted")
args.parse.parse_args()

#perform conversions 
#km -> miles
to_miles = kilometers_to_miles(args.value)
print("{0} kilometer is {1} miles".format(args.value, to_miles))

#miles -> km
to_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilometers".format(args.value, to_km))

#years -> minutes
to_minutes = years_to_minutes(args.value)
print("{0} years is {1} minutes".format(args.value, to_minutes))

#minutes -> years
to_years = minutes_to_years(ags.value)
print("{0} minutes is {1} years".format(args.value, to_years))

#fin
