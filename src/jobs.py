from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        reader = list(csv.DictReader(file))
    return reader
