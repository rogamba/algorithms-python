""" Permutations of string with unique
    characters...
"""


def permutations(word):
    perms = []
    def _get_perms(txt,perm=""):
        # Base case
        if len(perm) == len(word):
            perms.append(perm)
        # Recursive cases
        for i in range(len(txt)):
            missing_txt = txt[:i]+txt[i+1:]
            _get_perms(missing_txt, perm="{}{}".format(perm,txt[i]))
    _get_perms(word)
    return perms
        
if __name__ == '__main__':
    # Get permutations
    wrd="hola"
    perms = permutations(wrd)
    print(perms)
    print(len(perms))

