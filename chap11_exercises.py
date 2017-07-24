# # 2 CHAPTER 11 EXERCISE
def mating_pairs():
    """ (set, set) -> set of tuple

    Return a set of tuples where each tuple contains a male from males and a 
    female from females.
    """
    males = {'Chase', 'Mikey', 'Edgar'} 
    females = {'Britney', 'Maegan', 'Allie'}
    pairs = set()
    gerbils = males

    for i in range(len(gerbils)):
        male = males.pop()
        female = females.pop()  
        pairs.add((male, female),)
    return pairs
# # print(mating_pairs())



# #  4 CHAPTER 11 EXERCISE
def count_values(dictionary):
    """ (dict) -> int
    Return the number of distinct values it contains.
    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    """ 
    return len(set(dictionary.values()))
# # print(count_values({'red': 1, 'green': 1, 'blue': 2}))



# # 5 CHAPTER 11 EXERCISE
def least_likely(particle_to_prob):
    """ (dict of {str: float}) -> str

    Return the particle from particle_to_prob with the lowest probability.

    >>> least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07})
    {'meson'}
    """
    smallest = min(particle_to_prob.values())
    result = set()
    for key in particle_to_prob:
        if particle_to_prob[key] == smallest:
            result.add(key)
    return result
# # print(least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07}))


# # 1 CHAPTER 11 EXERCISE 
def find_dups(integer):
    """ list(int) -> set(int)
    Returns a set of ints that occur two or more times in the list.

    >>> find_dups([1, 3, 1, 4, 4, 1])
    {1, 4}
    >>> find_dups([2, 4, 6, 8, 2, 2, 8, 9, 4])
    {8, 2, 4}
    """
    dups = set()
    for item in integer:
        if integer.count(item) > 1:
            dups.add(item)
    return dups
# # print(find_dups([1, 3, 1, 4, 4, 1]))


# # 6 CHAPTER 11 EXERCISE
def count_dups(integer):
    """ dict -> int
    Returns the number of values that appear two or more times.

    >>> count_dups({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
    2
    """
    # theres two values that have two duplicates
    l = []
    for values in integer.values():
        l.append(values)
    return len(find_dups(l))
# # print(count_dups({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3}))

# # 7 CHAPTER 11 EXERCISE
def is_balanced(colors):
    """ (dict of {str: float}) -> bool
    Returns True if colors is a balanced color. 
    
    >>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
    False
    >>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
    True
    """
    values = list(colors.values())
    total = sum(values)
    return total == 1.0
# # print(is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})

# 8 CHAPTER 11 EXERCISE
def dict_intersect(dict1, dict2):
    """ (dict, dict) -> dict
    Return a dictionary that contains only the key/value pairs found in both 
    of the original dictionaries. 
    
    >>> dict_intersect({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
    {'a': 1, 'b': 2}
    """

    new_dict = {}
    value_1 = set(dict1.items())
    value_2 = set(dict2.items())
    if value_1.intersection(value_2):
        item = value_1.intersection(value_2)
        new_dict.update(item)
    return new_dict


# 9 CHAPTER 11 EXERCISE
def 
    
    