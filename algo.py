##5.5.	Задача консенсуса DNA ридов

def make_consensus(input: list[str]):
    out = ""
    if len(input) == 0:
        return out
    stringsLen = len(input[0])
    for i in range(0, stringsLen):
        consensusChar = first_top_letter(i, input)
        out += consensusChar
    return out
def first_top_letter(index: int, input: list[str]):
    charCountMap = {}
    for val in input:
        charValue = val[index]
        charCountMap[charValue] = charCountMap.get(charValue, 0) + 1

    return max(charCountMap, key=charCountMap.get)

# Проверяем
stringsInput = ["Tot", "Sem", "Beb", "Sat"]
consensusStr = make_consensus(stringsInput)
print(consensusStr)
