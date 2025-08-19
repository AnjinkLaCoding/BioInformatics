def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes.extend([2*block - 1, 2*block])
        else:
            nodes.extend([2*(-block), 2*(-block) - 1])
    return nodes

def colored_edges(genome):
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(0, n, 2):
            edge = (nodes[i+1], nodes[(i+2) % n])
            edges.append(edge)
    return edges

def two_break_distance(P, Q):
    P_edges = colored_edges(P)
    Q_edges = colored_edges(Q)

    adj = {}
    for u,v in P_edges + Q_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)

    # Count cycles
    visited = set()
    cycles = 0
    for node in adj:
        if node not in visited:
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for neigh in adj[curr]:
                        if neigh not in visited:
                            stack.append(neigh)
            cycles += 1

    blocks = sum(len(chrom) for chrom in P)
    return blocks - cycles

def parse_genome_line(line):
    chromosomes = []
    
    # Find all sequences within parentheses
    i = 0
    while i < len(line):
        if line[i] == '(':
            # Find the matching closing parenthesis
            j = i + 1
            while j < len(line) and line[j] != ')':
                j += 1
            
            # Extract the sequence between parentheses
            sequence = line[i+1:j]
            
            # Split by whitespace and convert to integers
            genes = []
            for gene in sequence.split():
                if gene.startswith('+'):
                    genes.append(int(gene[1:]))
                elif gene.startswith('-'):
                    genes.append(-int(gene[1:]))
                else:
                    # Handle case where + might be implicit
                    genes.append(int(gene))
            
            chromosomes.append(genes)
            i = j + 1
        else:
            i += 1
    
    return chromosomes

with open('C:/Users/Matthew/Downloads/dataset_30163_4 (1).txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines if line.strip()]
P = parse_genome_line(lines[0])
Q = parse_genome_line(lines[1])
res = two_break_distance(P, Q)

print(res)
