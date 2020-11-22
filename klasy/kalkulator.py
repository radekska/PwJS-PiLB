"""
Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora, parsującego i wykonującego równanie podane przez użytkownika
"""
import sys
from liczby_zespolone import LiczbyZespolone


class Kalkulator:
        
    def __parse_input(self, complex_number):
        splited_input = complex_number.split(' ')
        
        real_part = int(splited_input[0])
        sign = splited_input[1]
        imaginary_part = int(sign + splited_input[2][:-1])
   
        return LiczbyZespolone(real_part, imaginary_part)

    def __output_printer(self, output):
        print('Twój wynik to: {wynik}'.format(wynik=output))

    def __input_function(self):
        print('=============================================================')
        print('Liczby wprowadź w formacie <x +/- yi>' , end='\n')
        first_complex_number = input('Wprowadź pierwszą liczbę zespoloną: ')
        second_complex_number = input('Wprowdź drugą liczbę zespoloną: ')

        first_complex_number = self.__parse_input(first_complex_number)
        second_complex_number = self.__parse_input(second_complex_number)

        return first_complex_number, second_complex_number

        
    def __menu(self):
        print('=============================================================')
        print('Wybierz działanie:')
        print('1 - Dodawanie')
        print('2 - Odejmowanie')
        print('3 - Mnozenie')
        print('4 - Dzielenie')
        print('5 - Wykonaj kolejne działanie')
        print('Q - Zakończ program', end='\n')
        print('=============================================================')

        choice = input('Wybór: ')
        return choice
            

    def command_line_interface(self):
        output = None

        first_complex_number , second_complex_number = self.__input_function()
        
        while True:
            print('Wprowadzone liczby: {first} , {second}'.format(first=first_complex_number, second=second_complex_number))
            choice = self.__menu()
            if choice == '1':
                output =  first_complex_number + second_complex_number
                self.__output_printer(output)

            elif choice == '2':
                output =  first_complex_number - second_complex_number
                self.__output_printer(output)

            elif choice == '3':
                output = first_complex_number * second_complex_number
                self.__output_printer(output)

            elif choice == '4':
                try:
                    output = first_complex_number / second_complex_number
                except ZeroDivisionError:
                    print('Nie mozna dzielić przez zero!')
                else:
                    self.__output_printer(output)

            elif choice == '5':
                first_complex_number , second_complex_number = self.__input_function()

            elif choice in 'Qq':
                print('Koniec programu...')
                break
            else:
                print('Błędny wybór!')
            




if __name__ == '__main__':
    moj_kalkulator = Kalkulator()
    moj_kalkulator.command_line_interface()
