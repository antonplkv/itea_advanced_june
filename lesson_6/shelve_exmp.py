import shelve

SHELVE_FILE = 'SHELVE_DB'

with shelve.open(SHELVE_FILE) as countries:
    print(countries.clear())