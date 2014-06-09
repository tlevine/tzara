import qualified Data.Map as M
import qualified Data.Char as C

data Feature = Nchar | Nnewline | Nuppercase | Nlowercase | Ndigit | Nspace

data Cell = M.Map Feature Int

type Column = M.Map Feature [Int]

type Table = [Column]

type Distance a :: a -> a -> Float

tableDist :: Distance Table

columnDist :: Distance Column

toCell :: String -> Cell
toCell raw = M.fromList $ [("nchar", length raw),
                           ("nnewline", count (== '\n') raw),
                           ("nspace", count (== ' )' raw),
                           ("nuppercase", count C.isAsciiUpper raw
                           ("nuppercase", count C.isAsciiLower raw),
                           ("ndigit", count C.isNumber raw),
                           ("nmark", count C.isMark raw),
                           ("nsymbol", count C.isSymbol raw) ]
  where
    count func = foldr (\x sum -> if (func x) then sum + 1 else sum) 0

toColumn :: [Cell] -> Column
toColumn cell:cells
