from reactor.console import console
from ui.window import init_window
from encrypt.console import console_encrypt
import os
os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        print(" Механики, которые я сделал:")
        print("1.  Консоль управления реакторами")
        print("2.  Окно")
        print("3.  Консоль шифрования")
        print("Введите 'выход' для завершения.\n")
        x = input("Введите цифру механики: ").strip().lower()

        if x == "1":
            console()
        elif x == "2":
            init_window()
        elif x == "3":
            console_encrypt()
        elif x == "выход":
            print("Выход из программы.")
            break
        else:
            print(" Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
