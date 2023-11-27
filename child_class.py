from parent_class import Verification

#тут наследуем, переопределяем что необходимо
#использование super()
class Ver2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users.txt') as r:
            for item in r:
                if f'{self.login, self.password}' + '\n' == item:
                    raise ValueError('Такой пользователь уже существует')
        super().save()

    def show(self):
        return self.login, self.password

x = Ver2('Ivan4', 'abooooooooooooba', 22)

