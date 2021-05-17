class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return f"Мой номер счета {self._name}"

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return f"Аккаунт пользователя: {self._balance} Квро"

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Ошибка системы!")
        self._balance = balance

account = BankAccount(1, 90)
#имя аккаунта
account.name = "Адилет"
print(account.name)
#баланс аккаунта
account.balance = 100500
print(account.balance)


    # #@customer_name.setter
    # #def customer_name(self, customer_name):
    #     self._customer_name = customer_name
