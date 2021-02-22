def euclidean_dist(x, y):
    check_rules(x, y)
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    check_rules(x, y)
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    check_rules(x, y)
    set_x = set(x)
    set_y = set(y)

    intersect_x_y = set_x & set_y
    union_x_y = set_x | set_y
    return 1 - len(intersect_x_y)/len(union_x_y)

def dot_product(x, y):
    return

def cosine_sim(x, y):
    check_rules(x, y)
    raise NotImplementedError()

# Feel free to add more
def check_rules(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")