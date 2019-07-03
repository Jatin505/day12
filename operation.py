from collections import Counter
x={'b':10,'a':5,'c':90}
y={'b':78,'a':45}
z={'a':90,'c':10}
a=dict(Counter(x)+Counter(y)+Counter(z))
print(a)
