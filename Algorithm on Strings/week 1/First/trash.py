m = """0->1:G
1->2:A
2->3:G
0->4:T
4->5:T
1->6:G
6->7:A
7->8:A
8->9:C
9->10:T
0->11:A
11->12:T
12->13:A
13->14:C
14->15:C
11->16:G
16->17:A
17->18:A
18->19:C
19->20:C
0->21:C
21->22:C
22->23:C
23->24:A
24->25:T
1->26:T
26->27:C
27->28:G"""
q = m.split(sep = "\n")
s = """0->1:G
0->4:T
0->11:A
0->21:C
1->2:A
1->6:G
1->26:T
2->3:G
4->5:T
6->7:A
7->8:A
8->9:C
9->10:T
11->12:T
11->16:G
12->13:A
13->14:C
14->15:C
16->17:A
17->18:A
18->19:C
19->20:C
21->22:C
22->23:C
23->24:A
24->25:T
26->27:C
27->28:G
"""
s = s.strip()
m = m.strip()
p = s.split(sep="\n")


print(len(p))
print(len(q))
for i in p :
    if i in q :
        continue
    else :
        print(i)