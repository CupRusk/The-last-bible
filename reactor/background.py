import threading
import time
from reactor.settings import reactors
from reactor.reactors import status_peregrev


def reactor_loop():
    while True:
        for name, data in reactors.items():
            if data['активен']:
                heat_gain = 0.5 + (data['температура'] / 100)
                data['температура'] += heat_gain

                if data['температура'] > 80:
                    data['уровень радиации'] += 1
                else:
                    data['уровень радиации'] += 0.2

                if 'топливо' in data and data['топливо'] > 0:
                    data['топливо'] -= 0.1
                else:
                    data['активен'] = False
                    print(f"[!] Реактор '{name}' отключён — топливо закончилось.")
            else:
                if data['температура'] > 0:
                    data['температура'] -= min(0.3 + data['температура'] / 200, data['температура'])

                if data['температура'] < 40:
                    data['уровень радиации'] = max(0, data['уровень радиации'] - 0.5)

            # Перегрев
            if data['температура'] > 120:
                print(f"[АВАРИЯ] Реактор '{name}' перегрелся! Возможен взрыв.")
            
            data['температура'] = round(min(data['температура'], 999), 2)
            data['уровень радиации'] = round(min(data['уровень радиации'], 100), 2)
            if 'топливо' in data:
                data['топливо'] = round(max(data['топливо'], 0), 2)

        time.sleep(1)


def start_reactor_loop():
    thread = threading.Thread(target=reactor_loop, daemon=True)
    thread.start()
