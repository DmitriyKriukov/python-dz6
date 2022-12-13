# # 5. Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать
# # это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# # Примеры:
# # [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# # [1,4,3,2] => "1-4"
# # [1,4] => "1,4"
#
# # Какие-то дикие костыли получились
#
# some_list = [1, 4, 5, 2, 3, 9, 8, 11, 0]
# some_list.sort()
# count = 1
# some_str = f'{some_list[0]}'
# for i in range(1, len(some_list)):
#     if some_list[i] - some_list[i - 1] == 1 and count == 1:
#         some_str = some_str + '-'
#         count += 1
#     elif some_list[i] - some_list[i - 1] == 1 and count != 1 and (len(some_list) - i) != 1:
#         count += 1
#     elif some_list[i] - some_list[i - 1] == 1 and count > 1 and (len(some_list) - i) == 1:
#         some_str = some_str + f'{some_list[i]}'
#     elif some_list[i] - some_list[i - 1] != 1 and count > 1:
#         some_str = some_str + f'{some_list[i - 1]},{some_list[i]}'
#         count = 1
#     else:
#         some_str = some_str + f',{some_list[i]}'
# print(some_str)

# # 6. Дана строка (возможно, пустая), состоящая из букв A-Z:
# # AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# # Нужно написать функцию RLE, которая на выходе даст строку вида:
# # A4B3C2XYZD4E3F3A6B28
# # И сгенерирует ошибку, если на вход пришла невалидная строка.
# # Пояснения:
# # Если символ встречается 1 раз, он остается без изменений;
# # Если символ повторяется более 1 раза, к нему добавляется количество повторений.
#
#
# import re
#
# inp_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
# pattern = r'[^A-Z]'
# if re.search(pattern, inp_str) or inp_str == '':
#     print('Неверный ввод')
# else:
#     res = ''
#     ind = 0
#     count = 1
#     while ind < len(inp_str) - 1:
#         if inp_str[ind] == inp_str[ind + 1]:
#             count += 1
#         else:
#             if count == 1:
#                 res = res + inp_str[ind]
#             else:
#                 res = res + inp_str[ind] + str(count)
#             count = 1
#         ind += 1
#     if count == 1:
#         res = res + inp_str[-1]
#     else:
#         res = res + inp_str[-1] + str(count)
#     print(res)
