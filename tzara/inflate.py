import re
import collections

def features(cell:str) -> dict:
    notupper = re.compile(r'[^A-Z]')
    notlower = re.compile(r'[^a-z]')
    notdigit = re.compile(r'[^0-9]')

    stripped = cell.strip()

    return {
        'nchar': len(stripped),
        'nnewline': stripped.count('\n'),
        'nspace': stripped.count(' '),
        'nuppercase': re.sub(notupper, '', stripped),
        'nlowercase': re.sub(notlower, '', stripped),
        'ndigit': re.sub(notdigit, '', stripped),
    }

def feature_distributions(cells:iter) -> dict:
    distributions = collections.defaultdict(lambda: collections.Counter())
    for cell in cells:
        for key, value in cells.items():
            distributions[k][value] += 1
    return distributions

def merge_distributions(a:dict, b:dict) -> dict:
    '''
    Combine two dicts of counters.
    '''
    c = dict(a)
    for key, b.keys():
        if key not in c:
            c[key] = collections.Counter()
        c[key].update(b[key])
    return c
