data Sym = L | R deriving (Eq, Ord, Show)
tog L = R
tog R = L

data Tree a = Nil | Node { left  :: Tree a
                         , value :: a
                         , right :: Tree a
                         } deriving (Eq, Show)

chain :: [Sym] -> Sym -> Tree Sym
chain [] sym = Node Nil sym Nil
chain (x:xs) sym =
    case x of
      L -> Node (chain xs sym) sym Nil
      R -> Node Nil sym (chain xs sym)

insert :: [Sym] -> Tree Sym -> (Sym, Tree Sym)
insert [] t = (undefined, t)
insert (x:xs) Nil = undefined
insert (x:xs) (Node left value right) =
    case (x, left, right) of
      (L, Nil, r)   -> (value, Node (chain xs (tog value)) (tog value) r)
      (L, left, _)  -> let (sym, left') = insert xs left
                       in (sym, Node left' (tog sym) right)
      (R, l, Nil)   -> (value, Node l (tog value) (chain xs (tog value)))
      (R, _, right) -> let (sym, right') = insert xs right
                       in (sym, Node left (tog sym) right')

emSeed = [R, L]
treeSeed = Node (Node Nil L Nil) L Nil

step :: ([Sym], Tree Sym) -> ([Sym], Tree Sym)
step (!xs, t) = let (sym, t') = insert xs t
                in (sym:xs, t')

iterate' f x = x `seq` x : iterate' f (f x)

main =
    putStrLn $ concatMap (\x -> case x of
                                  L -> "0\n"
                                  R -> "1\n") $
                 (L:) $ map (head . fst) $ (iterate' step (emSeed, treeSeed))
