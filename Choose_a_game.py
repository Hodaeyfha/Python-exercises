class Choose_a_game:

    def __init__ (self):

        print("Welcome to our game")
        print('''
              Press the gsme number
              
              
              1 : Even and ood number
              2 : Letter word
              3 : Multiplication table
              4 : The number is divisble
              5 : The program takes a set of numbers
              
              ''')
        user_game = int(input("Please choose one of the numbers to enter the game: "))

        if user_game == 1:
            self.Even_and_ood_number()

        elif user_game == 2:
            self.Letter_word()

        elif user_game == 3:
            self.Multiplication_table()

        elif user_game == 4:
            self.The_number_is_divisble()

        elif user_game == 5:
            self.The_program_takes_a_set_of_numbers()

        else:
            print("Please don't deviate from the game nd choose the correct number ")
            

    def Even_and_ood_number(self):
        number = int(input('Enter a number: '))


        if number %2 == 0:
            print('even')
   
        else:
            print('odd')


    def Letter_word(self):
       word = input('Choose a word: ')
       letters = []
       for letter in word:
           
           if letter in letters:
               
               continue
           else:
               letters.append(letter)
               
       print(letters)


    def Multiplication_table(self):
        inputs = int(input('enter number: '))

        for number in range(2, inputs+1):

            for value in range(2, inputs+1):
                result = number * value
                print(f'{number} X {value} = {result}')

            print('--------------')
        
    def The_number_is_divisble(self):
        lower = int(input('Enter lower range limit: '))
        upper = int(input('Enter upper range limit: '))
        divisible = int(input('Enter the number to be divided by: '))

        for i in range(lower, upper +1):
            if i %divisible ==0:
                print(i)


    def The_program_takes_a_set_of_numbers(self):
        printask = input("Choose either 'even' or 'ood': ")
        choose = int(input("Enter number: "))

        if printask == 'even':
            for i in range(0, choose +1):
                if i %2 == 0:
            
                    print('even: ',i)

        elif printask == 'ood':
            for y in range(0, choose +1):
                if y %2 != 0:
            
                    print('ood: ',y)


    
 


g = Choose_a_game()
    
