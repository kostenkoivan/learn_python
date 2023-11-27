#наследование в глубину, наглядно и просто
class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    def a(self):
        print('C')

class D(C,A):
    def a(self):
        super().a()
        #print(self.__class__.__mro__)

print(D.__mro__)


D().a()

#класс для наследования и переопределния методов
class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self): #недоступен из вне, так же не наследуется, но исполняется
        if len(self.password) < 8:
            raise ValueError ('Слабый пароль')
        
    def save(self):
        with open('users.txt', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n') 