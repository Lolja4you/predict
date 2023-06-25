import random
import json

from collections import Counter


class Dice:
    def __init__(self) -> None:
        self.pk                     = 0

        self.num_simulations        = 20
        self.max_num_rolls          = 1000
        self.bet                    = 5
        self.balance                = 10
        

        self.big_counter            = 0
        self.small_counter          = 0

        self.odd_counter            = 0
        self.even_counter           = 0

        self.two_same_num_counter   = 0
        self.three_same_num_counter = 0

        self.straight_counter       = 0
        
        self.win_counter            = 0

        self.average_big_rate       = 0
        self.average_small_rate     = 0
        
        self.average_odd_rate       = 0      
        self.average_even_rate      = 0

        self.average_two_same_rate  = 0
        self.average_three_same_rate= 0

        self.average_straight_rate  = 0
        self.average_balance        = 0
        
        self.average_win_rate       = 0


        self.list_n                 = []
        self.list_roll_sum          = []

        self.list_rolls             = []
        self.roll_header            = []



    def json_packer(self, data, n, series):
        roll_header = {
            "series" : series+1,
            "roll"  : self.roll_header,
        }

        roll_content = {
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
        
        self.roll_header.append(roll_content)
        if n == 0:
            self.list_rolls.append(roll_header)
            
        if n+1 == self.max_num_rolls:
            self.roll_header  = []

        return self.list_rolls[series]
             

    def to_null_counter(self, series):
        self.big_counter            = 0
        self.small_counter          = 0

        self.odd_counter            = 0
        self.even_counter           = 0

        self.two_same_num_counter   = 0
        self.three_same_num_counter = 0

        self.straight_counter       = 0
    

    def play(self, data, n):
        bet = 5
        data['roll'][n]['bet'] = bet
        data['roll'][n]['before_balance'] = self.balance
        '''
        if 'S' == data['roll'][n]['small']:
            self.balance += bet*2
            status_1 = 1
        elif "3SN" == data['roll'][n]['3SN']:
            self.balance -= bet
            status_1 = 0
        else:
            self.balance -= bet
            status_1 = 0

        if 'O' == data['roll'][n]['odd']:
            status_2 = 1
            self.balance += bet*2
        elif "3SN" == data['roll'][n]['3SN']:
            self.balance -= bet
            status_2 = 0
        else:
            status_2 = 0
            self.balance -= bet
        
        if 10 == data['roll'][n]['roll_sum']:
            self.balance += bet*6
            status_3 = 1
        elif "3SN" == data['roll'][n]['3SN']:
            self.balance -= bet
            status_3 = 0
        else:
            self.balance -= bet
            status_3 = 0
        

        if "2SN" == data['roll'][n]['2SN']:
            status_4 = 1
            self.balance += bet*2.1
        elif "3SN" == data['roll'][n]['3SN']:
            self.balance -= bet
            status_4 = 0
        else:
            status_4 = 0
            self.balance -= bet


        average_status  = (status_1 + status_2 + status_4)/3
        #average_status = status_1 
        #average_status = (status_1 + status_2) / 2
        #average_status  = (status_1 + status_2 + status_3)/3
        '''
        try:
            if self.list_rolls[-1]['roll'][-1]['odd_rate'] <= self.list_rolls[-1]['roll'][-1]['even_rate']:
                eo = "E"
            else:
                eo = "O"

            if self.list_rolls[-1]['roll'][-1]['big_rate'] <= self.list_rolls[-1]['roll'][-1]['small_rate']:
                bs = "S"
            else:
                bs = "B"
            bet_predict = bs + eo

            if bet_predict ==  bet_predict == data['roll'][n]['odd'] + data['roll'][n]['small'] or bet_predict == data['roll'][n]['even'] + data['roll'][n]['big']:
                self.balance += bet*4.6
                status_1 = 1
            elif bet_predict == data['roll'][n]['odd'] + data['roll'][n]['big'] or data['roll'][n]['even'] + data['roll'][n]['small']:
                self.balance += bet*3.45
                status_1 = 1
            elif "3SN" == data['roll'][n]['3SN']:
                self.balance -= bet
                status_1 = 0
            else:
                self.balance -= bet
                status_1 = 0

            
        except:
            if 'S' == data['roll'][n]['small']:
                self.balance += bet*2
                status_1 = 1
            elif "3SN" == data['roll'][n]['3SN']:
                status_1 = 0
            else:
                self.balance -= bet
                status_1 = 0
            average_status = status_1 

        
        data['roll'][n]['after_balance'] = self.balance
        data['roll'][n]['status'] = average_status
        if n+1 == self.max_num_rolls:
            data["balance"] = self.balance
            self.balance = 10
        return data
    
    def analystic_data(self, data, n):
            #data = json.loads(data)
             
            big_rate        = self.big_counter/data['roll'][n]['id']
            small_rate      = self.small_counter/data['roll'][n]['id']
            
            odd_rate        = self.odd_counter/data['roll'][n]['id']
            even_rate       = self.even_counter/data['roll'][n]['id']

            two_same_rate   = self.two_same_num_counter/data['roll'][n]['id']
            three_same_rate = self.three_same_num_counter/data['roll'][n]['id']

            straight_rate   = self.straight_counter/data['roll'][n]['id']


            self.average_big_rate           += big_rate
            self.average_small_rate         += small_rate 

            self.average_odd_rate           += odd_rate 
            self.average_even_rate          += even_rate       

            self.average_two_same_rate      += two_same_rate 
            self.average_three_same_rate    += three_same_rate 

            self.average_straight_rate      += straight_rate 

            self.average_win_rate           += data['roll'][n]['status']

            data['roll'][n]['big_rate'] = big_rate
            data['roll'][n]['small_rate'] = small_rate

            data['roll'][n]['odd_rate'] = odd_rate
            data['roll'][n]['even_rate'] = even_rate

            if n+1 == self.max_num_rolls:
                self.average_balance         += data['balance']
                        
            if data["series"] == self.num_simulations and data['roll'][n]['id'] == self.max_num_rolls:
                self.average_big_rate        /= self.num_simulations * self.max_num_rolls
                self.average_small_rate      /= self.num_simulations * self.max_num_rolls

                self.average_odd_rate        /= self.num_simulations * self.max_num_rolls
                self.average_even_rate       /= self.num_simulations * self.max_num_rolls

                self.average_two_same_rate   /= self.num_simulations * self.max_num_rolls
                self.average_three_same_rate /= self.num_simulations * self.max_num_rolls

                self.average_straight_rate   /= self.num_simulations * self.max_num_rolls
                self.average_balance         /= self.num_simulations
                
                
                self.average_win_rate        /= self.num_simulations * self.max_num_rolls


                txt_1 = f"""
                    average. series: {self.num_simulations} - roll: {self.max_num_rolls} 
                    average Balnce : {self.average_balance}; average win rate: {self.average_win_rate}
                    big: {self.average_big_rate}; small: {self.average_small_rate};
                    odd: {self.average_odd_rate}; even: {self.average_even_rate};                
                    2SN: {self.average_two_same_rate}
                    3SN: {self.average_three_same_rate}
                    ST:  {self.average_straight_rate}

                    """
                j = Counter(self.list_roll_sum)
                output = open("simulations.js", 'w')
                output.write(json.dumps(self.list_rolls, indent=3))
                output.close()
                for i in range(0, len(j.most_common())):
                    sum_number_rate = f"\t\t    {j.most_common()[i][0]}N : {j.most_common()[i][1]/self.max_num_rolls/self.num_simulations}\n"
            
                    txt_1+=sum_number_rate
                print(txt_1)
                #print(self.list_rolls)

    def dice_roll(self, n, series):
        roll = []

        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)

        roll_sum = dice_1 + dice_2 + dice_3

        a = dice_1 == dice_2 - 1 == dice_3 - 2
        b = dice_1 == dice_2 + 1 == dice_3 + 2
        c = dice_1 + 1 == dice_2  == dice_3 - 1
        
        big        = None
        small      = None
        even       = None
        odd        = None

        two_same   = None
        three_same = None

        straight   = None

        if roll_sum % 2 == 0:
            self.even_counter += 1
            even = "E"
        else:
            self.odd_counter += 1
            odd  = "O"
        
        if roll_sum > 10:
            self.big_counter += 1
            big = "B"
        else:
            self.small_counter += 1
            small = "S"

        if dice_1 == dice_2 or dice_2 == dice_3 or dice_1 == dice_3:
            self.two_same_num_counter += 1
            two_same = "2SN"
        
        if dice_1 == dice_2 == dice_3:
            self.three_same_num_counter += 1
            three_same = "3SN"
        
        if a or b or c:
            self.straight_counter +=1
            straight = "ST"

        roll = [
                (dice_1, dice_2, dice_3),
                roll_sum,
                big, small,
                odd, even, 
                two_same, three_same, 
                straight
                ]
        self.list_n.append(roll)
        self.list_roll_sum.append(roll_sum)

        data = self.json_packer(roll, n, series)
        #self.play(data, n)
        self.analystic_data(self.play(data, n), n)

        
        #print(self.list_rolls)



object = Dice()
def game_while():
    cycle = 0
    while cycle != object.num_simulations:
        second_cycle = 0

        while second_cycle != object.max_num_rolls:
            object.dice_roll(second_cycle, cycle)
            second_cycle += 1
        cycle += 1
        object.to_null_counter(cycle)
game_while()