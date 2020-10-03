from binaryTree import Node
from letterFrequencies import english_alphabet_frequencies
import queue

class huffmanencode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return((self.left, self.right))

def create_tree(frequencies):

    our_priority_queue = queue.PriorityQueue();
    
    for value in frequencies:    
        our_priority_queue.put(value)

    while our_priority_queue.qsize() > 1:

        left  = our_priority_queue.get()
        right = our_priority_queue.get()
        root = huffmanencode(left, right)
        new_tuple = (left[0] + right[0], root)
        our_priority_queue.put((new_tuple))

    return our_priority_queue.get()

root = create_tree(english_alphabet_frequencies)

def walk_tree(root, prefix="", code={}):
    if isinstance(root[1].left[1], huffmanencode):
        walk_tree(root[1].left,prefix+"0", code)
    else:
        code[root[1].left[1]]=prefix+"0"
    if isinstance(root[1].right[1], huffmanencode):
        walk_tree(root[1].right,prefix+"1", code)
    else:
        code[root[1].right[1]]=prefix+"1"
    return(code)

code = walk_tree(root)
for i in sorted(english_alphabet_frequencies, reverse=True):
    print(i[1], (i[0]), code[i[1]])