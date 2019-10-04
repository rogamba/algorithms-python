""" Given a sequence of numbers pushed into an
    old phone, get the possible words that can come 
    out of the combination

"""

keyboard = {
    1 : [],
    2 : ["a","b","c"],
    3 : ["d","e","f"],
    4 : ["g","h","i"],
    5 : ["j","k","l"],
    6 : ["m","n","o"],
    7 : ["p","q","r","s"],
    8 : ["t","u","v"],
    9 : ["w","x","y","z"],
}

#code = [2,6,2,2]
code = [4,6,5,2]

dictionary = set([
    "rodrigo",
    "tree",
    "house",
    "hola",
    "amor",
    "boca",
    "amac",
    "coca"
])

def get_possible_words(code):
    possible = []
    # Loop possibilities
    for num in code:
        possible.append(keyboard[num])
    # Buld word combinations
    words = []
    def find_word(level=0,word=""):
        # Base case
        if level >= len(possible):
            if word in dictionary:
                words.append(word)
            return
        # Loop letters in the level and recurse
        for letter in possible[level]:
            find_word(level=level+1,word=word+letter)
    
    find_word()
    return words
    
words = get_possible_words(code)
print(words)