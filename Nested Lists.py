L=[[input(),float(input())] for i in range(int(input()))]
s = sorted(set([i[1] for i in L]))
for name in sorted(i[0] for i in L if i[1] == s[1]):
    print(name)
