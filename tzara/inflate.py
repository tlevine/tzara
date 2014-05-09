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

def inflate(dataset:iter) -> dict:
    '''
    Dataset is an iterable of dicts, with keys as string
    column names and values as string cell values.

    This returns a dictionary with keys as column names.
    Each of its values is another dictionary, with keys
    as string feature names (nchar, nnewline, &c.) and
    values as counter feature distributions.


        dataset :: [dict str str]
        distributions :: dict str collections.Counter
        deconstruct_dataset :: dataset -> dict str distributions
     
    For example,

        deconstruct_dataset([{'Petal.Length'}])

    returns something like this.

        {'Petal.Length':{'nchar':Counter({12:1}),'nnewline':Counter({0:1}})}

    It actually returns more, but this is a small example just
    to convey the type.
    '''
    distributions = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.Counter()))
    for row in dataset:
        for column_name, cell in row.items():
            for feature_name, feature_value in _features(cell).items():
                distributions[column_name][feature_name][feature_value] += 1
