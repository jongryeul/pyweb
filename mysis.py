import os

def clear():
    if os.name == 'nt':  # 윈도우이면
        os.system('CLS')
    else:  # posix
        os.system('clear')

    # os.system('cls' if os.name == 'nt' else 'clear')