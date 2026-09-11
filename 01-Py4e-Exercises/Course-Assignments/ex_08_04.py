uniq = open("romeo.txt")

unique_words = list()

for line in uniq :
    words = line.split()
    for w in words :
        if w not in unique_words :
            unique_words.append(w)
unique_words.sort()
print(unique_words)