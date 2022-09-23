from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
    return list(reader)
