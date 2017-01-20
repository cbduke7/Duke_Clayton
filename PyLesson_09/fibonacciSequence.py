startNum = int(input("Please enter your starting number: "))
seqSize = int(input("Please enter your sequence size: "))
seq = []*seqSize

for i in range(0, seqSize):
    if i == 0 or 1:
        seq[i] == startNum
    else:
        seq[i] = seq[index - 2]

print(seq) 
