""" Get all permutations of a given word
"""

word = "hola"

def get_permutations(word):
    perms = []
    def get_perms(txt, perm_word=""):
        if len(perm_word) == len(word):
            perms.append(perm_word)
            return
        for i in range(len(txt)):
            new_txt = txt[:i]+txt[i+1:]
            get_perms(new_txt, perm_word=perm_word+txt[i])
    get_perms(word)
    return perms

        
if __name__ == '__main__':
    print("Permutations of the word: {}".format(word))
    permutations = get_permutations(word)
    print(permutations)
        
        