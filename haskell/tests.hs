import Text.PrettyPrint (Style(ribbonsPerLine))
import Data.Sequence.Internal.Sorting (QList(Nil))
inc :: Integer -> Integer
inc x = x + 1


euler1 = sumMods [1..999]
    where mod3or5 x = x `mod` 3 == 0 || x `mod` 5 == 0
          sumMods xx = sum (filter mod3or5 xx)


--tail recursion: tail position is a pure function call (allows for direct passing when popping recursive calls off the stack)
fact n = aux 1 n
    where aux a 0 = a
          aux a n = aux (a*n) (n-1)--tail position (because it's directly used as return value once computed)

--higher order function
twice f x = f (f x)

--bst implementation, sum types algebraic data types
data Tree a = Branch a (Tree a) (Tree a) 
              | Empty
    deriving Show

bstAdd x Empty = Branch x Empty Empty
bstAdd x (Branch a left right)
    | x <= a = Branch a (bstAdd x left) right
    | otherwise = Branch a left (bstAdd x right)


bstFind x Empty = False
bstFind x (Branch a left right)
    | x == a = True
    | x < a = bstFind x left
    | otherwise = bstFind x right

--data Maybe a = Just a | Nothing

bstLookup x Empty = Nothing
bstLookup x (Branch (k,v) left right)
    | x==k = Just v
    | x < k = bstLookup x left
    | otherwise = bstLookup x right


getIOP x Empty = x
getIOP x (Branch a left right) = getIOP a right

bstRemove x Empty = Empty
bstRemove x (Branch a Empty Empty)
    | x == a = Empty
    | otherwise = Branch a Empty Empty
bstRemove x (Branch a Empty right)
    | x == a = right
    | x > a = Branch a Empty (bstRemove x right)
    | otherwise = Branch a Empty right --not in the tree case
bstRemove x (Branch a left Empty)
    | x == a = left
    | x < a = Branch a (bstRemove x left) Empty
    | otherwise = Branch a left Empty
bstRemove x (Branch a left right) 
    | x < a = Branch a (bstRemove x left) right
    | x > a = Branch a left (bstRemove x right)
    | otherwise = Branch (getIOP a left) (bstRemove (getIOP a left) left) right


--list implementation
data List a = Cons a (List a) | Null
    deriving Show

insertSorted x Null = Cons x Null
insertSorted x (Cons a b)
    | x <= a = Cons x (Cons a b)
    | otherwise = Cons a (insertSorted x b) 


data Complex = Complex {re :: Float, im :: Float}
               deriving (Show, Eq)
compadd a b = Complex {re = re a + re b, im = im a + im b}

compmult a b = Complex (re a * re b - im a * im b) (re a * im b + im a * re b)