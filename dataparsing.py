import json
from console import *

data_colors = {
    'lock/unlock': Colors.BLUE_BOLD_BRIGHT,
    'add-key': Colors.YELLOW_BOLD_BRIGHT,
    'revoke-key': Colors.BLACK_BOLD_BRIGHT,
    'login': Colors.CYAN_BOLD,
    'kick': Colors.RED_BOLD_BRIGHT
}


def log(key: str, timestamp: str, typ: str, action: str):
    with open('log.json', mode='r+', encoding='utf-8') as f:
        data = json.load(f)
        data.append({
            "key": key,
            "timestamp": timestamp,
            "type": typ,
            "action": action
        })

        f.seek(0)
        json.dump(data[:min(len(data), 50)], f, indent=4)
        f.truncate()


def clear_log():
    with open('log.json', 'w') as f:
        json.dump([], f)


def print_log():
    with open('log.json', mode='r+', encoding='utf-8') as f:
        data = json.load(f)

    Console.print(f'╔═{"═" * 50}═╦═{"═" * 15}═╦═{"═" * 12}═╦═{"═" * 100}═╗', Colors.BLACK_BOLD)
    Console.print(f'║ {"Key":<50} ║ {"Timestamp":15} ║ {"Type":12} ║ {"Message":100} ║', Colors.BLACK_BOLD)
    Console.print(f'╠═{"═" * 50}═╬═{"═" * 15}═╬═{"═" * 12}═╬═{"═" * 100}═╣', Colors.BLACK_BOLD)
    for t in data:
        Console.print(f'║ {t["key"]:<50} ║ {t["timestamp"].upper():15} ║ {t["type"].upper():12} ║ {t["action"]:100} ║',
                      data_colors[t['type']])
    Console.print(f'╚═{"═" * 50}═╩═{"═" * 15}═╩═{"═" * 12}═╩═{"═" * 100}═╝', Colors.BLACK_BOLD)
    "╚═══╩═══╩═══╝"


if __name__ == '__main__':
    clear_log()
    log('one', '1', 'lock/unlock', 'heh')
    log('two', '2', 'add-key', 'heh')
    log('three', '3', 'revoke-key', 'heh')
    log('four', '4', 'login', 'heh')
    log('five', '5', 'kick', 'heh')
    print_log()
