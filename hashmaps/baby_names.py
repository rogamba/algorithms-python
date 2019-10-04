""" Each year the goverment release a list of the 10000 most common baby names
    and their frequencies. The only problem y that some names have multiple spellings
    (for example John, Jon, Johnny) that would be essentially the same name but would
    appear separately in the list. 
    Given two lists, one of the (names, frequency) and another of pair of equivalent
    names, write an algorithm to print a new list of the tru frequency of each name.
    Note: If Jon and John are synonyms and John and Johhny are synonyms, then Jon and
    Johnny are synonyms (it's both transitive and symmetric) 

    Frequencies: John(15),Jon(12), Chris(13),Kris(4),Christopher(19)
    Synonyms: Jon,John),(John,Johnny),(Chris,Kris),(Chris, Christopher)
    Output: John(27), Kris(36)

"""

names = [
    ("John", 15),
    ("Jon", 12),
    ("Chris", 13),
    ("Kris", 4),
    ("Christopher", 19)
]

synonyms = [
    ("Jon","John"),
    ("John","Johnny"),
    ("Chris","Kris"),
    ("Chris","Christopher")
]

def baby_names_real_freq(names, synonyms):
    # Get mapping of the names in a hastable
    names_map = {}
    for name, syn in synonyms:
        # Check if it is a totally new name
        if name not in names_map:
            names_map[name] = name
        # Save synonym
        if syn not in names_map:
            names_map[syn] = name

    # Loop the frequencies
    real_frequencies = {}
    for name, freq in names:
        # Get the original name
        original_name = names_map[name]
        # With original set the count
        if original_name not in real_frequencies:
            real_frequencies[original_name] = 0
        # Sum
        real_frequencies[original_name] += freq

    return real_frequencies


if __name__ == '__main__':
    real_freq = baby_names_real_freq(names, synonyms)
    print("Baby names: {} ".format(names))
    print("Synonyms: {}".format(synonyms))
    print()
    print("Getting the real frequencies for the baby names...")
    print(real_freq)


            