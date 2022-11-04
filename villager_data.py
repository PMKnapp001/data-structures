# line added to test git command line execution
"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    # TODO: replace this with your code
    file = open(filename)
    species_list = []
    for data in file:
        entry = data.split("|")
        species_name = entry[1]
        species_list.append(species_name)

    species = set(species_list) 

    return species
    

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    # TODO: replace this with your code
    file = open(filename)
    villagers = []
    for data in file:
        entry = data.split("|")
        if search_string == entry[1]:
            villagers.append(entry[0])
        elif search_string == "All":
            villagers.append(entry[0])

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    
    file = open(filename)
    #hobbies = [fitness[], education[], nature[], play[], fashion[], music[]]
    hobbies = [] 
    for data in file:
        entry = data.split("|")
        hobby = entry[3]
        hobbies.append(hobby)
    
    hobbies = list(set(hobbies))
    hobbies_list = []
    for hobby in hobbies:
        hobby = []
        hobbies_list.append(hobby)
    
    for data in file:
        entry = data.split("|")
        hobby = entry[3]
        if hobby == 
    

    
    print(hobbies_list)
    print(hobby)

        # hobby = entry[3]
        
        # hobbies.append(list(hobby))  

        # if entry[3] == "Fitness":
        #     hobbies[0].append(entry[0]) 

       
            
    

    


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

    # TODO: replace this with your code

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

    # TODO: replace this with your code


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

    # TODO: replace this with your code

#print(all_species("villagers.csv"))
#print(get_villagers_by_species("villagers.csv", 'Dog'))
print(all_names_by_hobby("villagers.csv"))