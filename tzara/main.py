from smart_csv_dictreader import DictReader

from tzara.inflate import inflate

def inspect_csv(fp):
    dataset = DictReader(fp)
    inflate(dataset)
