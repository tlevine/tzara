import qualified Data.Map as M
import qualified Data.Char as C

type Array = undefined

data Cell = Cell {
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

tableDist :: Distance Table

columnDist :: Distance Column

fromCSVCell :: String -> Cell
fromCSVCell raw = { nchar = length raw,
                    nnewline = count (== '\n') raw,
                    nspace = count (== ' )' raw,
                    nuppercase = count C.isAsciiUpper raw
                    nuppercase = count C.isAsciiLower raw,
                    ndigit = count C.isNumber raw,
                    nmark = count C.isMark raw,
                    nsymbol = count C.isSymbol raw }
  where
    count func = foldr (\x sum -> if (func x) then sum + 1 else sum) 0
