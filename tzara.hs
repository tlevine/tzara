import qualified Data.Map as M

type Array = undefined

data Cell = Column {
  nchar :: Array Int,
  nnewline :: Array Int,
  nuppercase :: Array Int,
  nlowercase :: Array Int,
  ndigit :: Array Int,
  nspace :: Array Int
}

type Column = [Cell]

type Table = [Column]

type Distance a :: a -> a -> Float

dist :: Distance 

        'nchar': len(stripped),
        'nnewline': stripped.count('\n'),
        'nspace': stripped.count(' '),
        'nuppercase': re.sub(notupper, '', stripped),
        'nlowercase': re.sub(notlower, '', stripped),
        'ndigit': re.sub(notdigit, '', stripped),
