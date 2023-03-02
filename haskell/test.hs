-- create an error
type_error = putStrLn 'a' "Hello"

main = print . cat $ map pure [ 'a' .. 'z' ]
