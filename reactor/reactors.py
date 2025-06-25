from reactor.settings import reactors

def deactivate_reactor(name):
    if name not in reactors:
        print(f"[Ошибка] Реактор '{name}' не найден.")
        return

    if reactors[name]['уровень радиации'] > 10.5:
        print(f"[Внимание] Уровень радиации в реакторе '{name}' превышает норму! "
              f"Текущий уровень: {reactors[name]['уровень радиации']}%\n"
              "Невозможно удалённо деактивировать реактор.")
        return

    reactors[name]['активен'] = False
    print(f"[OK] '{name}' деактивирован.")


def activate_reactor(name):
    if name not in reactors:
        print(f"[Ошибка] Реактор '{name}' не найден.")
        return
    
    elif reactors[name]['активен']:
        print(f"[Внимание] Реактор '{name}' уже активен.")
        return
    
    reactors[name]['активен'] = True
    print(f"[OK] '{name}' активирован.")


def check_reactors():
    print("\n📊 Состояние реакторов:")
    for name, data in reactors.items():
        state = "🟢 Активен" if data['активен'] else "🔴 Отключен"
        print(f"- {name.title()}: {state} | "
              f"🌡 Темп: {data['температура']}°C | ☢ Радиация: {data['уровень радиации']}%")
        
def status_peregrev(name):
   if name not in reactors:
        print(f"[Ошибка] Реактор '{name}' не найден.")
        return
   elif reactors[name]['температура'] > 100:
        print(f"[Внимание] Реактор '{name}' перегревается! Текущая температура: {reactors[name]['температура']}°C")
        return