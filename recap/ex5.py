# Scan all possible ordered subcombinations of an order array

def scan(word):
    combos = set()
    
    def _scan(word=""):
        # Base case
        print(word)
        if len(word) <= 0:
            return
        if word not in combos:
            combos.add(word)
        # Adjavent nodes
        if len(word) > 1:
            if word[1:] not in combos:
                _scan(word=word[1:])
            if word[:-1] not in combos:
                _scan(word=word[:-1])
        
    _scan(word)
    return combos

if __name__ == '__main__':
    word = "holacomoestas"
    combos = scan(word)
    print(combos)