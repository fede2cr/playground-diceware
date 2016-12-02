# Example taken from https://stackoverflow.com/questions/19697846/python-csv-to-json

import csvmapper

fields = ('ArrayIndex', 'Word')
parser = csvmapper.CSVParser('diceware.wordlist.csv', csvmapper.FieldMapper(fields))

converter = csvmapper.JSONConverter(parser)

print converter.doConvert(pretty=True)
