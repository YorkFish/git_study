# coding:utf-8
# example 22: graph.py

from collections import deque

#       A
#      / \
# C - B   F
# |\ / \ / \
# | I   G   E
# |  \ / \ /|
#  -- D - H |
#     |_____|
GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D']
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def push(self, val):
        return self._deque.append(val)

    def pop(self):
        return self._deque.popleft()


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node, end=' ')
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)


def dfs(graph, start, searched):
    if start not in searched:
        print(start, end=' ')
        searched.add(start)
    for node in graph[start]:
        if node not in searched:
            dfs(graph, node, searched)


if __name__ == "__main__":
    print("bfs:", end=' ')
    bfs(GRAPH, 'A')
    print()

    print("dfs:", end=' ')
    dfs(GRAPH, 'A', set())
    print()
