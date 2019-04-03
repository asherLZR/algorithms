a1, a2 = map(int, input().split(":"))
b1, b2 = map(int, input().split(":"))
d = ((b1*60+b2)-(a1*60+a2))//2
f = a1*60+a2+d
h = f//60
m = f % 60
if h <= 9:
    h = "0"+str(h)
else:
    h = str(h)
if m <= 9:
    m = "0"+str(m)
else:
    m = str(m)
print(h+":"+m)
