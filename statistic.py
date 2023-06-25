from collections import Counter
#list_n = [1, 5, 3, 3, 1, 2, 2, 1, 4, 4, 1, 2, 5, 6, 2, 4, 2, 6, 4, 3, 3, 6, 5, 2, 3, 1, 2, 2, 3, 3, 6, 4, 3, 6, 3, 1]
"""
list_n = [
    2, 4, 3, 1, 6, 5, 1, 5,
    2, 3, 2, 5, 1, 2, 3, 6,
    4, 3, 5, 6, 6, 1, 2, 2,
    3, 4, 1, 6, 4, 1, 5, 3, 
    5, 4, 2, 5, 5, 4, 4, 2, 
    1, 5, 5, 3, 5, 4, 3, 5,
    3, 3, 1, 4, 6, 4, 6, 6,
    2,
          ]
"""

list_n = [
    5, 4, 2, 6, 2, 2,
    4, 2, 2, 6, 3, 3,
    6, 3, 6, 4, 1, 5,
    1, 2, 4, 1, 1, 4,
    4, 3, 3, 3, 2, 4,
    2, 2, 4, 5, 5, 3,
    6, 1, 3, 3, 1, 1,
    3, 2, 4, 1, 3, 6,
    3, 3, 6, 3, 4, 1,
    4, 6, 1, 5, 3, 1,
    2, 3, 2, 4, 3, 1,
    4, 3, 2, 5, 2, 3,
    3, 5, 2, 1, 6, 6,
    5, 2, 4, 4, 2, 1,
    3, 2, 5, 3, 3, 5,
    2, 2, 2, 4, 1, 4,
    4, 1, 6, 1, 6, 6,
    4, 3, 5,
    ]

big_counter = 0
small_counter = 0 

odd_counter = 0
edd_counter = 0

number = 0
list_number = []
counters = 0
for j in range(1, len(list_n)+3):
    try:
        number += list_n[j-1]
    except:
        pass
    if j % 3 == 0:
        if number > 10:
            big_counter += 1
        else:
            small_counter += 1

        if number % 2 == 0:
            edd_counter += 1

        elif number % 2 != 0:
            odd_counter += 1
        list_number.append(number)
        number = 0
        counters +=1

    
dicti = Counter(list_n)
dict_sorted = sorted(dicti.items())
list_n_len = len(list_n)
print(list_n_len)
rate_list = []
rate_counter = 0
for i in dict_sorted:
    element = i
    rate = element[1]/list_n_len
    rate_list.append((element[0], rate))
    print(element , rate)
    rate_counter += rate


sorted_rate_list = sorted(rate_list, key=lambda x: x[1])
summ = sum(list_n)/list_n_len
sorted_rate_list.reverse()
print(rate_counter)
print(sorted_rate_list, summ)

txt = f"big:{big_counter/counters} small: {small_counter/counters}\nodd {odd_counter/counters} edd {edd_counter/counters}"
print(txt)
print(Counter(list_number))