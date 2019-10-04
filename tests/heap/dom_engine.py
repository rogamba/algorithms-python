import json
import random

with open('data.json') as file:
    data = json.load(file)
print(data)


class DOM(object):
    """ Class representing the entire
        DOM tree
    """

    class Node:
        """ Node Element of the DOM
        """
        def __init__(self, elem):
            self.tag = None if "tag" not in elem else elem['tag']
            self.id = None if "id" not in elem else elem['id']
            self.classes = [] if 'classes' not in elem else elem['classes']
            self.adj = []
            self.parent = None

        def is_selected(self, selector):
            # Selector method for the instance node
            tag, _id, classes = None, None, []
            s_classes = selector.split(".")
            if len(s_classes) > 1:
                classes = s_classes[1:]
            s_id = s_classes[0].split("#")
            if len(s_id) > 1:
                _id = s_id[1] 
            tag = s_id[0]
            # Compare
            req = 0
            obs = 0
            if tag: req+=1
            if _id: req+=1
            if len(classes) > 0: req +=1
            # Compare
            if tag and self.tag == tag: obs+=1
            if _id and self.id == _id: obs+=1
            if len(classes) > 0 and set(classes).issubset(self.classes): obs+=1
            return req == obs
              
    def __init__(self, hierarchy=None):
        self.nodes = {}
        self.count = 0
        self.root = None
        if hierarchy:
            self.add(hierarchy)
            
    def __str__(self):
        s = ""
        for k in self.nodes:
            s+="{} => {}".format(
                k,
                [ a.key for a in self.nodes[k].adj ]
            )
            s+="\n"
        return s

    def add_node(self, key, elem):
        new_node = self.Node(elem)
        self.nodes[key] = new_node
        new_node.parent = self.nodes[key]
        self.nodes[key].key = key
        if not self.root:
            self.root = self.nodes[key]

    def add(self, elem, parent_key=""):
        # Unique node key
        if not parent_key:
            node_key = self.gen_key(elem, parent_key)
        else:
            node_key=parent_key
        if node_key not in self.nodes:
            self.add_node(node_key, elem)
        # Check children to recurse
        if 'children' in elem:
            for child in elem['children']:
                child_key = self.gen_key(child, self.nodes[node_key].key)
                self.add_node(child_key, child)
                self.nodes[node_key].adj.append(self.nodes[child_key])
                self.add(child, parent_key=child_key)
        
    def gen_key(self, elem, path):
        key="({})".format(random.randint(0,1000))
        if "tag" in elem:
            key+=elem["tag"]
        if "id" in elem:
            key+="#{}".format(elem["id"])
        if "classes" in elem:
            key+="".join( [".{}".format(c) for c in elem['classes']] ) 
        return "{}>{}".format(path,key)

    def find(self, selector):
        # Count the times the conditions are fullfilled
        count = 0
        selector = selector.split(" ")
        # Traverse tree to find node
        def find_compare(node=None, selector_path=None):
            nonlocal count
            if len(selector_path) <= 0:
                return 
            # If length of the condition == 1 and node fulfill the condition, increment
            if node.is_selected(selector_path[0]):
                if len(selector_path) == 1:
                    count+=1
                selector_path = selector_path[1:]

            # Traverse the children
            for adj in node.adj:
                find_compare(adj, selector_path=selector_path[:])

        find_compare(self.root, selector_path=selector[:])
        return count
    

def find_selectors(dom, tests):
    results = []
    for selector in tests:
        results.append(dom.find(selector))
    return results
    

if __name__=='__main__':
    dom = DOM(data['hierarchy'])
    print("DOM tree:")
    print(dom)
    res = find_selectors(dom, data['tests'])
    print("Count: {}".format(res))





