from reactor.reactors import activate_reactor, deactivate_reactor, status_peregrev, check_reactors
from reactor.background import start_reactor_loop
import time


def console():
    print("⚛️ Добро пожаловать в систему управления реакторами")
    print("Введите 'Помощь'")

    start_reactor_loop()  # Запуск фоновой симуляции

    while True:
        command = input(">>> ").strip().lower()
        if command.startswith("активировать "):
            name = command.split(" ", 1)[1]
            activate_reactor(name)
        elif command.startswith("деактивировать "):
            name = command.split(" ", 1)[1]
            deactivate_reactor(name)
        elif command == "статус":
            check_reactors()
        elif command == "помощь":
            print("деактивировать <name> - дистанционное отключения реактора.\ncтатус - проверить все реакторы.\nактивировать <name> - дистанционное включения реактора ")
        elif command == "выход":
            print("Выходим...")
            time.sleep(3)
            return 

        else:
            print("❓ Неизвестная команда")