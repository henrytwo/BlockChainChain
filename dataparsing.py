import json
import time
import datetime
from console import *

data_colors = {
    'lock/unlock': Colors.BLUE_BOLD_BRIGHT,
    'add-key': Colors.YELLOW_BOLD_BRIGHT,
    'revoke-key': Colors.BLACK_BOLD_BRIGHT,
    'login': Colors.CYAN_BOLD_BRIGHT,
    'kick': Colors.RED_BOLD_BRIGHT
}


def log(key: str, typ: str):
    with open('log.json', mode='r+', encoding='utf-8') as f:
        data = json.load(f)
        data.append({
            "key": key,
            "timestamp": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            "type": typ
        })

        f.seek(0)
        json.dump(data[:min(len(data), 50)], f, indent=4)
        f.truncate()


def clear_log():
    with open('log.json', 'w') as f:
        json.dump([], f)


def print_log():
    Console.clear()

    with open('log.json', mode='r+', encoding='utf-8') as f:
        data = json.load(f)

    Console.print('BLOCKCHAINCHAIN SYSTEM LOG')
    Console.print(f'╔═{"═" * 50}═╦═{"═" * 19}═╦═{"═" * 12}═╗', Colors.BLACK_BOLD)
    Console.print(f'║ {"Key":<50} ║ {"Timestamp":19} ║ {"Type":12} ║', Colors.BLACK_BOLD)
    Console.print(f'╠═{"═" * 50}═╬═{"═" * 19}═╬═{"═" * 12}═╣', Colors.BLACK_BOLD)
    for t in data:
        Console.print(f'║ {t["key"]:<50} ║ {t["timestamp"].upper():19} ║ {t["type"].upper():12} ║',
                      data_colors[t['type'].lower()])
    Console.print(f'╚═{"═" * 50}═╩═{"═" * 19}═╩═{"═" * 12}═╝', Colors.BLACK_BOLD)
    "╚═══╩═══╩═══╝"


if __name__ == '__main__':
    clear_log()

    """
    log('one', 'lock/unlock')
    log('two', 'add-key')
    log('three', 'revoke-key')
    log('four', 'login')
    log('five', 'kick')
    print_log()
    """
