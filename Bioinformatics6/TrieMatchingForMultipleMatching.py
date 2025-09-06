from collections import defaultdict

def TrieConstruct(str):
    res = []
    Tree = defaultdict(lambda: defaultdict(list))
    for i in str:
        node = Tree
        for j in range(len(i)):
            if i[j] not in node:
                node[i[j]] = {}
            node = node[i[j]]
        node['$']=True
    return Tree

def PrefixTrieMatching(Text, Trie):
    SymbolID = 0
    Symbol = Text[SymbolID]
    Node = Trie
    res = ""
    while True:
        if '$' in Node:
            #res += Symbol
            return res
        elif Symbol in Node:
            Node = Node[Symbol]
            SymbolID += 1
            res += Symbol
            if SymbolID < len(Text):
                Symbol = Text[SymbolID]
            #else:
                #if '$' in Node:
                    #res += Symbol
                    #return res
                #else:
                    #return "Not found"
        else:
            return "Not found"

def TrieMatching(Text, Trie):
    PrefixList = defaultdict(list)
    i = 0
    LenText = len(Text)
    while Text:
        #print(Text)
        Prefix = PrefixTrieMatching(Text, Trie)
        #print(Prefix)
        if Prefix != 'Not found':
            PrefixList[Prefix].append(i)
        i += 1
        Text = Text[1:]
    return PrefixList

    


with open("C:/Users/Matthew/Downloads/dataset_30220_8.txt", 'r') as file:
    lines = file.read().strip().split('\n')
'''
Sample Input:
AATCGGGTTCAATCGGGGT
ATCG GGGT

Sample Output:
ATCG: 1 11
GGGT: 4 15
'''
Text = lines[0]
Patterns = lines[1].split()
tree = TrieConstruct(Patterns)
res = TrieMatching(Text, tree)
for a,b in res.items():
    print(f"{a}: {" ".join([str(i) for i in b])}")