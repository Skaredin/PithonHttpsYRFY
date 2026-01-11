
# Пример обычного кода

result = 0
for n in range(1, 11):
    result += n ** 2
# Пример обычного кода

# Секретная магия квайна (ТАК НАЗЫВАЕТСЯ ФУНКЦИЯ КОТОРАЯ ВЫВОДИТ САМ СЕБЯ :)
quine = '''
result = 0
for n in range(1, 11):
    result += n ** 2
quine = {0}{1}{0}
print(quine.format(chr(39), quine))
'''
# Секретная магия квайна (ТАК НАЗЫВАЕТСЯ ФУНКЦИЯ КОТОРАЯ ВЫВОДИТ САМ СЕБЯ :)


print(quine.format(chr(39), quine))
