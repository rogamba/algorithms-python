import json
import random
from collections import deque

data = {
    "hierarchy": {
      "tag": "html",
      "children": [
        {
          "tag": "div",
          "children": [
            {
              "tag": "li",
              "id": "content",
              "children": [
                {
                  "tag": "span",
                  "children": [
                    {"tag": "p"}
                  ]
                },
                {
                  "tag": "div",
                  "children": [
                    {"tag": "div"}
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "tests": [
      "div p",
      "div#id.class1.class2"
    ]
  }

def match(selector, node):
    """ Match selector 
        required attr must be equal to
        observed attributes
    """
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
    if tag: req+=1
    if _id: req+=1
    if len(classes) > 0: req +=1
    # Compare
    obs = 0
    if tag and 'tag' in node and node['tag'] == tag: 
        obs+=1
    if _id and 'id' in node and node['id'] == _id: 
        obs+=1
    if len(classes) > 0 and 'classes' in node and set(classes).issubset(node['classes']): 
        obs+=1
    return req == obs

def count_nodes(root, selector):
    count=0
    def _count_nodes(node, selector=""):
        nonlocal count
        selector_path = deque(selector.split(" "))
        # Found the selector
        if len(selector_path) > 1 and match(selector_path[0],node):
            selector_path.popleft()
        if len(selector_path) == 1 and match(selector_path[0],node):
            count+=1
        # Fing adjacent nodes
        if 'children' in node:
            for child in node['children']:
                # Only if matches the top most selector, continue there...
                _count_nodes(child, selector=" ".join(selector_path) )

    _count_nodes(root, selector=selector)
    return count

def find_selectors(dom, tests):
    """ Loop the selectors and nodes
    """
    results = []
    for selector in tests:
        results.append(count_nodes(dom, selector))
    return results
  

if __name__=='__main__':
    res = find_selectors(data['hierarchy'], data['tests'])
    print("Count: {}".format(res))
