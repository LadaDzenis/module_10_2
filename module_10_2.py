from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        day = 0
        while warriors != 0:
            warriors = warriors - self.power
            sleep(1)
            day += 1
            print(f'{self.name} сражается {day} день(дня), осталось {warriors} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')