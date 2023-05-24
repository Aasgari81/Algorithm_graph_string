# python3
def BWT(text):
    result = ""
    letter_cycle = {}
    suffixes = []
    s = len(text)
    for i in range(s) :
        suffix = ""
        letter = text[i]
        m = i
        for j in range(s) :
            if letter == "$" :
                suffix += "$"
                m = 0
                letter = text[m]
            

            else :
                suffix += letter
                m += 1
                letter = text[m]
        suffixes.append(suffix)
    suffixes = sorted(suffixes)
    for sfx in suffixes :
        result += sfx[-1]
    return result





if __name__ == '__main__':
    text = input().strip()
    print(BWT(text))