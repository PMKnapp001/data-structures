# line added to test git command line execution
"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)
    species_list = []
    for line in file:
        line = line.rstrip()
        data = line.split("|")
        species_list.append(data[1])

    return set(species_list)
    

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    file = open(filename)
    villagers = []
    for line in file:
        line = line.rstrip()
        entry = line.split("|")
        if search_string == entry[1]:
            villagers.append(entry[0])
        elif search_string == "All":
            villagers.append(entry[0])

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.
    
    Fitness = 1, Nature = 2, Education = 3, Music = 4, Fashion = 5, Play = 6

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    file = open(filename)
    villagers_by_hobby = [[],[],[],[],[],[]] 
    hobby_dictionary = {"Fitness":0, "Nature":1, "Education":2, "Music":3, "Fashion":4, "Play":5}
    for line in file:
        line = line.rstrip()
        entry = line.split("|")
        i = hobby_dictionary[entry[3]]
        villagers_by_hobby[i].append(entry[0])

    return villagers_by_hobby
        
    

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    file = open(filename)

    for line in file:
        line = line.rstrip()
        data = line.split("|")
        villager = tuple(data) 
        all_data.append(villager)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    file = open(filename)
    villager_motto_dictionary = {}

    for line in file:
        line = line.rstrip()
        data = line.split("|")
        villager_motto_dictionary[data[0]] = data[4]
    
    if villager_name in villager_motto_dictionary:
        return villager_motto_dictionary[villager_name]


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    file = open(filename)
    list_file = open(filename)
    villager_personality_dictionary = {}
    villagers_by_personality = []

    for line in file:
        line = line.rstrip()
        data = line.split("|")
        villager_personality_dictionary[data[0]] = data[2]
    
    for line in list_file:
        line = line.rstrip()
        data = line.split("|")
        if data[2] == villager_personality_dictionary[villager_name]:
            villagers_by_personality.append(data[0])
    
    return set(villagers_by_personality)

# print("--------------All Species----------------")
# print(all_species("villagers.csv"))
# print()
# print("--------------All Villagers--------------")
# print(get_villagers_by_species("villagers.csv"))
# print()
# species = "Dog"
# print(f"---------All {species} Villagers--------")
# print(get_villagers_by_species("villagers.csv",species))
# print()
# print("-------------Villagers By Hobby----------")
# for hobby_list in all_names_by_hobby("villagers.csv"):
#     print(hobby_list)
#     print()
# print("-----------------All Data-------------------")
# # print(all_data("villagers.csv"))
# print()
# print("-----------------Villager Motto-------------------")
# name = "Agent S"
# print(find_motto("villagers.csv", name))
print()
print("-----------------Villagers by personality-------------------")
name = "Willow"
print()
for villager in find_likeminded_villagers("villagers.csv", name):
    print(villager)
