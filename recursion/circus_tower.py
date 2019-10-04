""" Given an array of persons consisting of tuples
    that indicate (height, width). Get the arrangement
    that fulfills the condition that every person should
    carry a person shorter and lighter on it's shoulders.
"""

arr = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]

# Get adjacent
def get_adjacent(person):
    adj = []
    for a in arr:
        if a[0] < person[0] and a[1] < person[1]:
            adj.append(a)
    return adj

# Recursion
def get_towers(arr):
    max_path = []
    def get_path(person, path=[]):
        nonlocal max_path
        # Get adjacent (persons that can be above)
        adj = get_adjacent(person)
        # No more adjacent, end of tower
        path = path[:]+[person]
        if not adj:
            if len(path) > len(max_path):
                max_path = path
        # Recurse
        for a in adj:
            get_path(a, path=path)
    for a in arr:
        get_path(a)
    return max_path


if __name__ == '__main__':
    tower = get_towers(arr)
    print(tower)