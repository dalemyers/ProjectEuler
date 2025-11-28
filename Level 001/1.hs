
isMultiple :: [Int] -> Int -> Bool
isMultiple mults num = or $ map (\x -> num `mod` x == 0) mults

result = sum $ filter (isMultiple [3,5]) (take 1000 [0..])
