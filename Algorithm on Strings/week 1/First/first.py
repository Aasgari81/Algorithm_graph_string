#Uses python3

def build_trie(patterns):
    tree = dict()
    lenletters = 0
    for m in patterns :
        lenletters += len(m)
    for j in range(lenletters + 3) :
        tree[j] = dict(dict())
    newnodenumber = 1
    for word in patterns :
        itno = 0
        prev_node = 0
        if word[0] in tree[0].keys() :
            for letter in word :  
                if letter in tree[prev_node].keys() :
                    itno += 1
                    prev_node = tree[prev_node][letter]
                else :
                    tree[prev_node][letter] = newnodenumber
                    prev_node = newnodenumber
                    newnodenumber += 1
                    itno += 1
                    
                    
        else : 
            for l in range(len(word)) :
                if l == 0 :
                    tree[l][word[l]] = newnodenumber
                    newnodenumber+=1
                else :
                    tree[newnodenumber - 1][word[l]] = newnodenumber
                    newnodenumber += 1
    return tree
        
if __name__ == "__main__":
    n = int(input())
    patterns = [input() for _ in range(n)]
    tree = build_trie(patterns)
   
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))