#Uses python3

def solve(text, n, patterns):
    result = set()
    max_length  = max(len(word) for word in patterns)
    patterns_trie = build_trie(patterns)
    current_letter_index = 0
    for letter in text :
        if letter in patterns_trie[0].keys() :
            nnode = 0
            q = current_letter_index
            for i in range( max_length + 1) :
                if q >= len(text) :
                    break
                if letter in patterns_trie[nnode].keys() :
                    nnode = patterns_trie[nnode][letter]
                else :
                    break
                if "$" in patterns_trie[nnode].keys() :
                    result.add(current_letter_index)
                    
                
                
                
                
                if q == len(text) - 1 : 
                    letter = text[q]
                elif q < len(text) - 1 :
                    letter = text[q+1]
                else :
                    break
                q += 1
                
        current_letter_index += 1 
    
    return result


def build_trie(patterns):
    tree = dict()
    lenletters = 0
    for m in patterns :
        lenletters += len(m)
    for j in range(lenletters * 2) :
        tree[j] = dict(dict())
    patterns = sorted(patterns, key=len)
    newnodenumber = 1
    for word in patterns :
        itno = 0
        prev_node = 0
        sq = ""
        if word[0] in tree[0].keys() :
            for letter in word :  
                sq = letter
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
                sq = word[l]
                
                if l == 0 :
                    tree[l][word[l]] = newnodenumber
                    newnodenumber+=1
                    prev_node = tree[prev_node][word[l]]

                else :
                    tree[prev_node][word[l]] = newnodenumber
                    newnodenumber += 1
                    prev_node = tree[prev_node][word[l]]

        tree[prev_node]["$"] = newnodenumber
        newnodenumber+=1
    return tree


if __name__ == '__main__':
    import sys

    text = input().strip()
    n = int(input().strip())
    patterns = [input().strip() for _ in range(n)]

    ans = solve(text, n, patterns)
    ans = sorted(ans)

    print(' '.join(map(str, ans)))
