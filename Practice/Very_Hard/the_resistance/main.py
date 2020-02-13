import sys
import math
import time
 
class TreeNode:
    def __init__(self, m_char, r_str = 0):
        self.m_char = m_char
        self.r_str = r_str
        self.childs = []
            
    def get_child(self, m_char):
        for c_node in self.childs:
            if c_node.m_char == m_char:
                return c_node
        return None
        
    def debug(self, idx):
        if self.m_char != None:
            debug(" " * (idx * 3) + self.m_char + ("[" + str(self.r_str) + "]" if self.r_str != 0 else ""))
        for child in self.childs:
            child.debug(idx + 1)
        

class Tree:
    def __init__(self, word_dic):
        self.begin_node = TreeNode("")
        for x in range(len(word_dic)):
            self.add_word_to_tree(word_dic[x])
        
    def add_word_to_tree(self, m_word):
        cur_node = self.begin_node
        m_word_len = len(m_word)
        i = 0
        for m_char in m_word:
            target_node = cur_node.get_child(m_char)
            if target_node == None: # If char not exist, add it
                    cur_node.childs.append(TreeNode(m_char))
                    target_node = cur_node.get_child(m_char)
            if i == m_word_len - 1: # If last char of word, res_nbr += 1
                target_node.r_str += 1
            cur_node = target_node
            i += 1
             
    def debug(self):
        self.begin_node.debug(0)
        
        
class Solver:
    def __init__(self, tree):
        self.tree = tree
    
    def solve(self, m_sentence):
        self.m_sentence = m_sentence
        self.m_sentence_len = len(m_sentence)
        self.h_sentence = [-1] * self.m_sentence_len
        total = self.start_solve(0)
        print(total)
        
    def start_solve(self, idx):
        if self.h_sentence[idx] == -1:
            self.h_sentence[idx] = 0
            for child in self.tree.begin_node.childs:
                self.h_sentence[idx] += self.recursive(child, idx)
        return self.h_sentence[idx]

    def recursive(self, cur_node, idx):
        # If bad char
        if cur_node.m_char != self.m_sentence[idx]:
            return 0
        # If word and sentence end:
        if idx == self.m_sentence_len - 1:
            return cur_node.r_str
        
        idx += 1
        if idx >= self.m_sentence_len:
            return 0
        ret = 0
        if cur_node.r_str != 0:
            ret += self.start_solve(idx) * cur_node.r_str
        
        for node in cur_node.childs:
            ret += self.recursive(node, idx)
        return ret

    def debug(self):
        debug(self.h_sentence)

def debug(message):
    print(message, file=sys.stderr)
  
def get_morse(word, mdict):
    m_str = ""
    for x in word:
        m_str += mdict[ord(x) - 65]
    return m_str

sys.setrecursionlimit(10000000)
m_dict = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']      
l = input()
total_len = len(l)
n = int(input())
w = []
for i in range(n):
    w.append(get_morse(input(), m_dict))

old_ts = time.time()
tree = Tree(w)
debug("tree build in " + '{0:.2f}'.format(time.time() - old_ts))

old_ts = time.time()
# tree.debug()
debug("tree print in " + '{0:.2f}'.format(time.time() - old_ts))

old_ts = time.time()
solver = Solver(tree)
solver.solve(l)
# solver.debug()
debug("sentence solve in " + '{0:.2f}'.format(time.time() - old_ts))