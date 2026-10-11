class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        bankSet = set(bank)
        visited = set([startGene])

        q = deque([(startGene, 0)])

        while q:
            gene, moves = q.popleft()

            if gene == endGene:
                return moves
            
            for i in range(len(startGene)):
                for c in ["A", "C", "G", "T"]:
                    geneList = list(gene)
                    geneList[i] = c
                    mutatedGene = "".join(geneList)
                    if mutatedGene not in bankSet:
                        continue
                    else:
                        if mutatedGene not in visited:
                            visited.add(mutatedGene)
                            q.append([mutatedGene, moves + 1])
        return -1 

            # Generate possible single-character mutations

            # For each mutated gene:
                # If it exists in bankSet and isn't visited:
                    # Mark it visited
                    # Add (mutatedGene, moves + 1) to the queue
