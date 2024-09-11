a = 5
b = 6
c = 7
d = 10

print("a", a)
print("b", +b)
print("c", c)
print("d", d)

a, b = b, a
c, d = d, c

print("a", a)
print("b", +b)
print("c", c)
print("d", d)
