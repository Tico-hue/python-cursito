commonChild1 = ''
commonChilds = []
charMatch = ""
indexMatch = 0
palabra1 = "anita"
palabra2 = "nieta"
while len(palabra1) > 0:

    for index1 in range(len(palabra1)):
        for index2 in range(indexMatch, len(palabra2)):
            if palabra1[index1] == palabra2[index2]:
                charMatch = palabra1[index1]
                indexMatch = index2+1
                commonChild1 += charMatch
                commonChilds.append(commonChild1)
                break

    palabra1 = palabra1[1:]
    indexMatch = 0
    commonChild1 = ""
hijomayor = ""
for hijo in commonChilds:
    if len(hijo) > len(hijomayor):
        hijomayor = hijo
print(hijomayor)
