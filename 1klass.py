#создаем первый класс, разбираемся с инкапсуляцией, методами, свойствами
class Purse:

    def __init__(self, valuta = '' , owner_name = 'Unknown'):
        if valuta not in ('USD', 'EUR', 'RUB'):
            raise ValueError
        self.__money = 0.00
        self._valuta = valuta
        self.owner_name = owner_name

    def top_up_balance(self, how_much_money):
        self.__money += how_much_money
        return how_much_money

    def top_down_balance(self, how_much_money):
        if (self.__money < how_much_money):
            print("Недостачно средств")
            raise ValueError
        self.__money -=how_much_money
        return how_much_money
    
    def info(self):
        print(self.__money, self.valuta, self.owner_name)
        return
    
    def __del__(self):
        print("Кошелек удален")
        return

x = Purse('RUB','Valera')

x.valuta = 'RUB'
x.info()
x.__money = 1000 # не сработает, тк поля с __ перед названием инкапсулированы
x._valuta = 'EUR' # тоже не получится
x.owner_name = 'Валера' # а это уже сработает
x.top_up_balance(1000)
x.top_down_balance(100)
x.info()
x.top_down_balance(1100) #выкинет ошибку
