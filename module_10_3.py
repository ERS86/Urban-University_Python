import threading
from random import randint
from time import sleep


class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while 0 < counter <= 100:
            random_number = randint(50, 500)
            counter -= 1
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        counter = 100
        while 0 < counter <= 100:
            random_number = randint(50, 500)
            counter -= 1
            print(f'Запрос на {random_number}.')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                break


test = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(test,))
th2 = threading.Thread(target=Bank.take, args=(test,))

th1.start()
th1.join()
th2.start()
th2.join()

print(f'Итоговый баланс: {test.balance}')
