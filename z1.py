# Владимир Штефан, [19.02.2023 17:02]
# [В ответ на Практика для 18.0]
# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями
# с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.
#
# Владимир Штефан, [19.02.2023 17:03]
# [В ответ на Практика для 18.0]
# print(all_eq(['крот', 'белка', 'выхухоль']))
# print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
#
# Владимир Штефан, [19.02.2023 17:03]
# [В ответ на Практика для 18.0]
# ['крот____', 'белка___', 'выхухоль']
# ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
# ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

def all_eq(lst):
    new_list = []
    for i in lst:
        lst_max = max(lst, key=len)
        len_lst = len(lst_max)
        str_lst =''.join(i.ljust(len_lst, '_'))
        new_list.append(str_lst)
    return new_list

def all_eq_1(lst: list) -> list:
    max_len = len(max(lst, key=len))
    return [item.ljust(max_len, '_') for item in lst]

print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
