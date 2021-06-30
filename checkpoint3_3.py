from collections import Counter
dict1={'a':200,'b':150,'c':300}
dict2={'a':250,'b':100,'c':200}
d = Counter(dict1) + Counter(dict2)
print(d)

