import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        enemies = 100
        days_of_war = 0
        warning = []
        message = f'{self.name}, на нас напали!'
        for i in range(enemies):
            if enemies > 0:
                days_of_war += 1
                enemies -= self.power
                if message not in warning:
                    print(message)
                    warning.append(message)
                print(f'{self.name} сражается {days_of_war} день(дня)..., осталось {max(enemies, 0)} воинов.\n')
                time.sleep(1)
                if enemies <= 0:
                    print(f'{self.name} одержал победу спустя {days_of_war} дней!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
second_knight.join()
print('Все битвы закончились!')
