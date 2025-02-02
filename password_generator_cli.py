import random


LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&',"( ", ")", "*", "+", "?", "/"]


def generate_password(n_letters, n_numbers, n_symbols):
    """
    Generate a random password of letters, numbers, and symbols
    """
    letter_choices = [random.choice(LETTERS) for i in range(n_letters)]
    
    number_choices = [random.choice(NUMBERS) for i in range(n_numbers)]
    
    symbols_choices = [random.choice(SYMBOLS) for i in range(n_symbols)]
    
    password_list = letter_choices + number_choices +  symbols_choices
        
    random.shuffle(password_list)
    
    password = "".join(password_list)
        
    return password
    
    