class BetLog:
    def __init__(self) -> None:
        self.bet_list = []

    def add_event_in_log(self, ser_data):
        self.bet_list.append(ser_data)

    def return_data(self):
        return self.bet_list

    def __str__(self) -> str:
        return f"{self.bet_list}"

class EventData:
    def __init__(self, *args) -> None:
        self.args = args

    def __number(self):
        return self.args[1]
    
    def __black_or_red(self):
        if "black" in self.args:
            return "black"
        else:
            return "red"
        
    def __odd_or_even(self):
        if self.args[1] % 2 == 0:
            return "even"
        else:
            return "odd"
        
    def __big_or_small(self):
        if self.args[1] > 18:
            return "big"
        else:
            return "small"

    def serializer(self):
        serializer_event_data = {
            "number"    :   self.__number(),
            "black/red" :   self.__black_or_red(),
            "odd/even"  :   self.__odd_or_even(),
            "big/small" :   self.__big_or_small()
        }
        return serializer_event_data
    
    def __str__(self) -> str:
        return self.args

class Analysis:
    def __init__(self, ) -> None:
        self.num_simulations        = 1
        self.big_counter            = 0
        self.small_counter          = 0

        self.odd_counter            = 0
        self.even_counter           = 0

        self.red_counter             = 0
        self.black_counter          = 0
        
        self.average_big_rate       = 0
        self.average_small_rate     = 0
        
        self.average_odd_rate       = 0      
        self.average_even_rate      = 0
        
        self.average_red_rate       = 0
        self.average_black_rate     = 0


    def counter(self, serializer):
        data = serializer
        if data['black/red'] == 'red':
            self.red_counter+=1
        else:
            self.black_counter+=1
        
        if data['odd/even'] == 'odd':
            self.odd_counter+=1
        else:
            self.even_counter+=1
        
        if data['big/small'] == 'small':
            self.small_counter+=1
        else:
            self.big_counter+=1

    def analysis(self):
        big_rate        = self.big_counter/self.num_simulations 
        small_rate      = self.small_counter/self.num_simulations 
        
        odd_rate        = self.odd_counter/self.num_simulations 
        even_rate       = self.even_counter/self.num_simulations 

        red_rate        = self.red_counter/self.num_simulations
        black_rate      = self.black_counter/self.num_simulations
        
        """
        self.average_big_rate           += big_rate
        self.average_small_rate         += small_rate 

        self.average_odd_rate           += odd_rate 
        self.average_even_rate          += even_rate   
        
        self.average_red_rate           += red_rate
        self.average_black_rate         += black_rate

        self.average_big_rate        /= self.num_simulations
        self.average_small_rate      /= self.num_simulations

        self.average_odd_rate        /= self.num_simulations
        self.average_even_rate       /= self.num_simulations

        self.average_red_rate        /= self.num_simulations
        self.average_black_rate      /= self.num_simulations
        """
        self.num_simulations+=1

        return {
                'num_simulations'   :   self.num_simulations,
                'average_big_rate'  :   round(big_rate, 3),
                'average_small_rate':   round(small_rate, 3),
                'average_odd_rate'  :   round(odd_rate, 3),
                'average_even_rate' :   round(even_rate, 3),
                'average_red_rate'  :   round(red_rate, 3),
                'average_black_rate':   round(black_rate, 3),
                }



class Me:
    def __init__(self) -> None:
        pass

class MyBet:...

class WriteInTerminal:
    def output(self, **kwarg):
        n = 0
        
        for i in kwarg["BetLog"].return_data():
            print(
                f"{n} >>>", i["number"], i["black/red"], i["odd/even"], i["big/small"])
            n+=1
        txt_1 = f"""
            average. cycle --- {n}
            odd: {kwarg['Analysis']['average_odd_rate']}; even: {kwarg['Analysis']['average_even_rate']};                
            big: {kwarg['Analysis']['average_big_rate']}; small: {kwarg['Analysis']['average_small_rate']};
            red: {kwarg['Analysis']['average_red_rate']}; black: {kwarg['Analysis']['average_black_rate']}
        """
        print(txt_1)

class WriteInFille:...



"""
odd/even
black/red/green
small/big

number 


"""
b = BetLog()
c = WriteInTerminal()
analysis = Analysis()

while True:
    a = EventData(input("color: "), int(input("number: ")))
    b.add_event_in_log(a.serializer())
    analysis.counter(a.serializer())

    c.output(BetLog = b, Analysis=analysis.analysis())



