a = [ 1, 2, 3 , 3, 4, 4, 5, 6]
n = len(a)
l, r = 0, n-1
t =3
while l < r:
    m = (l+r)//2
    if a[m] < t:
        l = m +1
    else:
        r = m
print(l)
