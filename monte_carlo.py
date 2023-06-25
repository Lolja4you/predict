import random

import matplotlib.pyplot as plt

def roll_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    die_3 = random.randint(1, 6)

    # Определим является ли значение на костях одинаковым
    if (die_1+die_2+die_3)%2==0:
        same_num = True
    elif die_1 == die_2 and die_2 == die_3:
        same_num = False
    else:
        same_num = False
    return same_num

num_simulations = 10000
max_num_rolls = 100
bet = 5

# Отслеживаемые переменные
win_probability = []
end_balance = []
"""
fig = plt.figure()
plt.title("Monte Carlo Dice Game [" + str(num_simulations) + "simulations]")
plt.xlabel("Roll Number")
plt.ylabel("Balance [$]")
plt.xlim([0, max_num_rolls])
"""
for i in range(num_simulations):
    balance = [10]
    num_rolls = [0]
    num_wins = 0
    # Выполняется до тех пор пока игрок не выкинет 1000 раз
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()
        # Результат если кости одинаковые
        if same == True:
            balance.append(balance[-1] + 2 * bet)
            num_wins += 1
        # Результат если кости разные
        else:
            balance.append(balance[-1] - bet)

        num_rolls.append(num_rolls[-1] + 1)
    # Сохраняем отслеживаемую переменную и добавляем строку к рисунку

    win_probability.append(num_wins/num_rolls[-1])
    end_balance.append(balance[-1])
    """
    plt.plot(num_rolls, balance)"""
"""
plt.show()
"""
# Усредненная вероятность выигрыша и конечного баланса
overall_win_probability = sum(win_probability)/len(win_probability)
overall_end_balance = sum(end_balance)/len(end_balance)
# Вывод средних значений
print("Average win probability after " + str(num_simulations) + "runs: " + str(overall_win_probability))
print("Average ending balance after " + str(max_num_rolls) + "runs: $" + str(overall_end_balance))

"""
json_part_data = {
    data : {
        "id"        : second_pk,
        "roll"      : (dice_1, dice_2, dice_3),
        "roll_sum"  : roll_sum,
        "even"      : even,
        "odd"       : odd,
        "Big"       : big,
        "small"     : small,
        "2SN"       : two_same,
        "3SN"       : three_same,
        "ST"        : straight,
    },

}
"""

"""
bet = {
        "small" : ,
        "big"   : ,
        "odd"   : ,
        "edd"   : ,
        "Number": ,
        "2SN"   : ,
        "3SN"   : ,
        "ST"    : , 

    }



"""
"""
            rols_data = json.dumps({
                "series" : series+1,
                "data"   : {
                    "roll" : [{
                        "id"        : n+1,
                        "roll"      : data[0],
                        "roll_sum"  : data[1],
                        "big"       : data[2],
                        "small"     : data[3],
                        "odd"       : data[4],
                        "even"      : data[5],
                        "2SN"       : data[6],
                        "3SN"       : data[7],
                        "ST"        : data[8],
                        #"status"    : ...,
                        #"bet"       : ...,
                        #"before_balance" : ...,
                        #"afte_balance"   : ...,
                    }],
                }
            })
"""
"""
        roll_header = {
            "series" : series+1,
            "roll"  : [{
                        "id"        : n+1,
                        "roll"      : data[0],
                        "roll_sum"  : data[1],
                        "big"       : data[2],
                        "small"     : data[3],
                        "odd"       : data[4],
                        "even"      : data[5],
                        "2SN"       : data[6],
                        "3SN"       : data[7],
                        "ST"        : data[8],
                        #"status"    : ...,
                        #"bet"       : ...,
                        #"before_balance" : ...,
                        #"afte_balance"   : ...,
                    }
                }]
"""