class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #creates the dictionary for the values
        adj = collections.defaultdict(list)

        #a for loop adding the values to the dictionary
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        #bfs to get the answer
        def bfs(src, target):
            #base condition, if not met return -1
            if src not in adj or target not in adj:
                return -1
            
            #initialise the queue and the visisted set
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            #start the bfs
            while q:
                #pops the element
                node, w = q.popleft()
                #if the node is equal to the target pops the w where w is the actual combined weight
                if node == target:
                    return w
                #gets the values stored in the dictionary
                for nei, weight in adj[node]:
                    #if the neightbour(a,b etc) is not in visited, append it to the queue with the newly calculated weight
                    #and then add it to visited
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
