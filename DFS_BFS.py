from queue import Queue,PriorityQueue

def dfs(graph,root):
    visited = []
    stack = [root]

    while stack:
        top = stack.pop()
        if top not in visited:
            for node in graph[top]:
                if node not in visited:
                    stack.append(node)
            visited.append(top)
    print(visited)

def dfs_search(graph,root,key):
    visited = []
    stack = [root]

    while stack:
        top = stack.pop()
        if top == key:
            visited.append(top)
            break

        if top not in visited:
            for node in graph[top]:
                if node not in visited:
                    stack.append(node)
            visited.append(top)
    print(visited)

def dfs_search_path(graph,root,key):
    visited = []
    stack = [(root,[root])]
    while stack:
        print("Stack:",stack)
        print(visited)
        print("-"*10)
        top,path = stack.pop()
        # print("Stack:",top,path)
        if top == key:
            visited.append(top)
            print(path)
            break

        if top not in visited:
            for node in graph[top]:
                if node not in visited:
                    stack.append((node,path+[node]))
            visited.append(top)
    # print(visited)

def bft(tree,root):
    q = Queue(maxsize=0)
    q.put(root)
    visited = []
    while not q.empty():
        front = q.get()
        if front not in visited:
            for node in tree[front]:
                if node not in visited:
                    q.put(node)
            visited.append(front)

    print(visited)

def level_order_traversal(tree,root):
    q = Queue(maxsize=0)
    q.put(root)
    visited = []
    while not q.empty():
        front = q.get()
        if front not in visited:
            i = len(tree[front])-1
            while i>=0:
                if tree[front][i] not in visited:
                    q.put(tree[front][i])
                i-=1
            visited.append(front)

    i=len(visited)
    while i>0:
        print(visited.pop())
        i-=1

def bfs(tree,root,key):
    q = Queue(maxsize=0)
    q.put((root,[root]))
    visited = []
    while not q.empty():
        front,path = q.get()
        print(front,path)
        if front == key:
            visited.append(front)
            print(path)
            break

        if front not in visited:
            for node in tree[front]:
                if node not in visited:
                    q.put((node, path+[node]))
            visited.append(front)

if __name__ == '__main__':
    graph1 = {
        'A': ['B', 'S'],
        'B': ['A'],
        'C': ['D', 'E', 'F', 'S'],
        'D': ['C'],
        'E': ['C', 'H'],
        'F': ['C', 'G'],
        'G': ['F', 'S'],
        'H': ['E', 'G'],
        'S': ['A', 'C', 'G']
    }

    tree = {
        0:[1,2],
        1:[0,3],
        2:[0,4,5],
        3:[1],
        4:[2,6],
        5:[2],
        6:[4]
    }
    # dfs(graph1, 'A')
    # dfs(tree,0)
    # dfs_search_path(graph1, 'A','B')
    # bft(tree,0)
    # bfs(tree,0,6)
    level_order_traversal(tree,0)