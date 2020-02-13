import sys
import math

def get_default(default):
    n_new_lst = []
    for i in range(len(default)):
        n_new_lst.append(Node())
    for i in range(len(default)):
        n_new_lst[i].index = i
        n_new_lst[i].neightboor = default[i].neightboor
        n_new_lst[i].gateway = default[i].gateway
        for j in range(len(default[i].linked)):
            n_new_lst[i].linked.append(n_new_lst[default[i].linked[j].index])
    return n_new_lst

class Node:
    def __init__(self):
        self.index = None
        self.gateway = False
        self.neightboor = 0
        self.action = 0
        self.linked = []
        self.heat = -1
    
    def add_link(self, target):
        self.linked.append(target)

n, l, e = [int(i) for i in input().split()]

node_lst = []
for i in range(n):
    node_lst.append(Node())
    node_lst[i].index = i

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    node_lst[n1].add_link(node_lst[n2])
    node_lst[n2].add_link(node_lst[n1])
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    node_lst[ei].gateway = True
    for j in range(len(node_lst[ei].linked)):
        node_lst[ei].linked[j].neightboor += 1
    
def get_action(node):
    lowest = None
    for i in range(len(node.linked)):
        if node.linked[i].heat != -1 and (node.linked[i].heat == node.heat - 1) and (lowest == None or node.linked[i].action < lowest):
            lowest = node.linked[i].action
    lowest = 0 if lowest == None else lowest
    return lowest - node.neightboor + 1

def backtrack(node, etage):
    if node.heat == etage:
        return False
    if node.heat == -1:
        node.heat = etage
        node.action = get_action(node)
        return True
    else:
        save = False
        for i in range(len(node.linked)):
            if node.linked[i].gateway == False and (node.heat + 1 == node.linked[i].heat or node.linked[i].heat == -1):
                if backtrack(node.linked[i], etage):
                    save = True
        return save

def destruct_link(node, index):
    for i in range(len(node.linked)):
        if node.linked[i].index == index:
            del node.linked[i]
            return

def get_more_near(tmp_lst):
    save_coord = None
    save_score = None
    for i in range(len(tmp_lst)):
        if tmp_lst[i].neightboor > 0 and (save_score == None or save_score < tmp_lst[i].heat):
            save_score = tmp_lst[i].heat
            save_coord = [i, None]
            for j in range(len(tmp_lst[i].linked)):
                if tmp_lst[i].linked[j].gateway == True:
                    save_coord[1] = tmp_lst[i].linked[j].index
                    break
    return save_coord

def get_with_action(tmp_lst):
    save_coord = None
    save_score = None
    for i in range(len(tmp_lst)):
        if tmp_lst[i].neightboor > 1 and (save_score == None or save_score > tmp_lst[i].heat) and tmp_lst[i].action <= 0:
            save_score =  tmp_lst[i].heat
            save_coord = [i, None]
            for j in range(len(tmp_lst[i].linked)):
                if tmp_lst[i].linked[j].gateway == True:
                    save_coord[1] = tmp_lst[i].linked[j].index
                    break
    return save_coord

while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    res = None
    for i in range(len(node_lst[si].linked)):
        if node_lst[si].linked[i].gateway:
            res = [si, node_lst[si].linked[i].index]
    if res == None:
        tmp_lst = get_default(node_lst)
        res = backtrack(tmp_lst[si], 0)
        etage = 1
        while res == True:
            res = backtrack(tmp_lst[si], etage)
            etage+=1
        res = get_with_action(tmp_lst)
        if res == None:
            res = get_more_near(tmp_lst)            
    node_lst[res[0]].neightboor -= 1
    destruct_link(node_lst[res[0]], res[1])
    destruct_link(node_lst[res[1]], res[0])
    print(str(res[0]) + " " + str(res[1]))