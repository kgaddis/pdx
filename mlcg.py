# Kainoa Gaddis (c) 2014
# This is a Multiplicative Linear Congruential Generator
# aka a Pseudo-Random number generator



# The given seed value for s
s = 12


# New custom randrange function
def randrange(p1, p2 = None):
    global s

    a = 55
    m = 251

    if p2 == None:
        low = 0
        high = p1
    else:
        low = p1
        high = p2
    
    # Compute result
    r = s % (high - low) + low
    
    # Update the seed
    s = (s * a) % m

    return r




if __name__ == "__main__":
    for _ in range(12):
        print(randrange(15))
