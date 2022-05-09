
import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, strings):
        current_node = self.head

        for string in strings:
            
            if string not in current_node.children:
                current_node.children[string] = Node(string)

            current_node = current_node.children[string]
       
        return True

    def dfs(self, current_node, depth):
        for k, v in sorted(current_node.children.items()):
            
            for _ in range(depth):
                print("--", end="")
            print(k)

            self.dfs(v, depth + 1)
        
        return True


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    trie = Trie()
    for _ in range(N):
        current_input = list(map(str, sys.stdin.readline().split()))
        trie.insert(current_input[1:])

    trie.dfs(trie.head, 0)