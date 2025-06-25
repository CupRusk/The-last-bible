import threading
import time
from reactor.settings import reactors
from reactor.reactors import status_peregrev


def reactor_loop():
    while True:
        for name, data in reactors.items():
            if data['активен']:
                data['температура'] += 1
                data['уровень радиации'] += 0.5
                status_peregrev(name)
            else:
                data['температура'] = max(0, data['температура'] - 0.5)
                data['уровень радиации'] = max(0, data['уровень радиации'] - 0.2)
        time.sleep(1)

def start_reactor_loop():
    thread = threading.Thread(target=reactor_loop, daemon=True)
    thread.start()
