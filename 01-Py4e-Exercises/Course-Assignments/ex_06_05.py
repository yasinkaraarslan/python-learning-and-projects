str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(":")
# print("0") 18
piece = str[ipos+2: ]
# print(num)
value = float(piece)
print(value)


