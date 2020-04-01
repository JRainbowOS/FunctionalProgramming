module Main where

qshort :: Ord a => [a] -> [a]
qshort []     = [] 
qshort (p:xs) = qshort [x | x<-xs, x<p] ++ [p] ++ qshort [x | x<-xs, x>=p]

main = do
    print (qshort [1, 3, 2, 4, 0])