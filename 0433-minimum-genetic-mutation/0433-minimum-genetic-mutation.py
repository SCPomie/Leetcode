class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        #initialise the trackings
        bankSet = set(bank)
        visited = set([startGene])
        #start the queue
        q = deque([(startGene, 0)])
        #bfs starts
        while q:
            #pops the queue   
            gene, moves = q.popleft()
            #base case when the mutated gene is equal to the end gene you return the moves
            if gene == endGene:
                return moves
            #double for loop to mutate the Gene
            for i in range(len(startGene)):
                for c in ["A", "C", "G", "T"]:
                    geneList = list(gene)
                    geneList[i] = c
                    mutatedGene = "".join(geneList)
                    #if the mutation is not in the bank then just move to the next iteration
                    if mutatedGene not in bankSet:
                        continue
                    else:
                        #add the mutation to the visited and append it to the queue with moves + 1
                        if mutatedGene not in visited:
                            visited.add(mutatedGene)
                            q.append([mutatedGene, moves + 1])
        return -1 
