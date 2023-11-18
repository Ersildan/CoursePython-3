def foo():
    s = input()
    s_ = s
    total = 1
    while True:
        txt = '@beegeek.bzz'
        if s + txt in m_lst:
            s = s_ + str(total)
            total += 1
        else:
            m_lst.append(s+txt)
            e_lst.append(s+txt)
            break


n = int(input())
m_lst = [input() for _ in range(n)]

m = int(input())
e_lst = []

for i in range(m):
    foo()
    
for i in e_lst:
    print(i)
