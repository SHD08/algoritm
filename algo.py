##1. Оценить асимптотическую сложность приведенного ниже алгоритма

Рассмотрим асимтотическую сложность каждого блока кода, и после этого получим итоговую


a = len(arr) – 1   		# O(1)
out = list()			# O(1)

while a > 0:			#  сложность цикла приблизительно O(log1.7(n))
    out.append(arr[a])
    a = a // 1.7
out.merge_sort()		#  O(n log(n))

Общая сложность будет сумма O(1) + O(1) + O(log1.7(n)) + O(n log(n)) но в асимптотике выбирается наибольшее, при n стремящемся к бесконечности. Так как O(n log(n)) > O(log1.7(n)), то финально

Ответ - O(n log(n))



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


##7 Сорт
def radix_sort(arr, max_digits):

    # основание системы счисления
    base = 10

    # создаём промежуточный пустой массив из 10 элементов
    bins = [[] for _ in range(base)]

    # перебираем все разряды, начиная с нулевого
    for i in range(0, max_digits):
        # перебираем все элементы в массиве
        for x in arr:
            # получаем цифру, стоящую на текущем разряде в каждом числе массива
            digit = (x // base ** i) % base
            # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
            bins[digit].append(x)
        # собираем в исходный массив все ненулевые значения из промежуточного массива
        arr = [x for queue in bins for x in queue]

        # очищаем промежуточный массив
        bins = [[] for _ in range(base)]

    # возвращаем отсортированный массив
    return arr
# Проверяем
arr = [23, 24, 25, 12, 14, 15, 16, 17, 12, 14, 20, 12, 25, 13, 20, 21, 12]
print(radix_sort(arr, 2))

