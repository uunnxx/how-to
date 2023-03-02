-- file: ch00/KMinima.hs
-- lines beginning with "--" are comments.

import Text.PrettyPrint.HughesPJ (brackets)
minima k xs = take k (sort xs)

-- Lists
-- A list is surrounded by square brackets; the elements are separated by commas:
-- ghci> [1, 2, 3] -- [1, 2, 3]

-- Commas are separators, not terminators
-- Some languages permit the last element in a list to be followed by an optional trailing
-- comma before a closing brackets, but Haskell doesn't allow this. If you leave in a trailing
-- comma (e.g., [1, 2,]), you'll get a parse error.
--
-- A list can be of any length. An empty list is written []:
-- ghci> [] -- []
-- ghci> ["foo", "bar", "baz", "quux", "fnord", "xyzzy"] -- ["foo", "bar", "baz"...]
--
-- An elements of a list must be of the same type. Here, we violate this rule.
-- Our list starts with two Bool values, but ends with a string:
-- ghci> [True, False, "testing"] -- error
--
