fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

fibList :: [Int]
fibList = map fib [1..] --Woo! Super inefficiency!

result = sum $ filter even $ takeWhile (<4000000) fibList
