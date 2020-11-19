import time
import threading


# Overiding Thread class in threading module 
class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, stick_left, stick_right):
        threading.Thread.__init__(self)
        self.index = index
        self.stick_left = stick_left
        self.stick_right = stick_right

    def run(self):
        while self.running:
            # Philosopher thinks for 20 seconds
            print(f'Philosopher {self.index} is thinking.\n')
            time.sleep(5)
            print(f'Philosopher {self.index} wants to eat!\n')
            self.eat()

    # Eat without deadlock - philosopher awaits for boths sticks to be free
    def eat(self):
        # Sticks corresponds to semaphores - if both are free philosopher will eat.
        stick_1, stick_2 = self.stick_left, self.stick_right
        while self.running:
            stick_1.acquire() # Philosopher takes a left stick
            taken = stick_2.acquire(False)
            if taken: break # If right stick not available, leave left stick
            stick_1.release()
            print(f'Philosopher {self.index} swaps sticks.\n')
            stick_1, stick_2 = stick_2, stick_1
        else:
            return

        self.eating()
        stick_2.release()
        stick_1.release()
            
        

    def eating(self):
        print(f'Philosopher {self.index} starts eating.\n')
        time.sleep(5) # Eats for 20 seconds
        print(f'Philosopher {self.index} stops eating and starts thinking.\n')


def main():
    # Initializing 5 semaphores/sticks
    sticks = [threading.Semaphore() for _ in range(5)]

    philosophers = [Philosopher(i, sticks[i%5], sticks[(i+1)%5]) for i in range(5)]
    Philosopher.running = True

    for p in philosophers: p.start()
    time.sleep(60)
    Philosopher.running = False
    print ("Done eating.\n")


if __name__ == '__main__':
    main()



