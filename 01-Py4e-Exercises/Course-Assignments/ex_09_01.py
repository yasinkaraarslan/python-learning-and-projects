counts = dict()

names = ['yasin', 'ahmet', 'yasin', 'mehmet', 'yasin', 'ahmet']

for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)