#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def imhigher(h1, h2):
    "floor h1 is above of h2 if h1-h2 == 1."
    return h1-h2 > 0

def adjto(h1, h2):
    "Two floors are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def floor_puzzle():
    floors = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors)) # 1
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if not Hopper == 5 # Hopper does not live on the top floor. 
                if not Kay == 1 # Kay does not live on the bottom floor. 
                if not Liskov == 5 and not Liskov == 1 # Liskov does not live on either the top or the bottom floor. 
                if imhigher(Perlis, Kay)# Perlis lives on a higher floor than does Kay. 
                if not adjto(Ritchie, Liskov)# Ritchie does not live on a floor adjacent to Liskov's. 
                if not adjto(Kay, Liskov) # Liskov does not live on a floor adjacent to Kay's.
                )
print floor_puzzle()