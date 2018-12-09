from typing import *


class Colors:
    RESET = "\033[0m"

    BOLD = "\033[1m"
    ITALICS = "\033[3m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"

    BLACK_BOLD = "\033[1;30m"
    RED_BOLD = "\033[1;31m"
    GREEN_BOLD = "\033[1;32m"
    YELLOW_BOLD = "\033[1;33m"
    BLUE_BOLD = "\033[1;34m"
    PURPLE_BOLD = "\033[1;35m"
    CYAN_BOLD = "\033[1;36m"
    WHITE_BOLD = "\033[1;37m"

    BLACK_ITALICS = "\033[3;30m"
    RED_ITALICS = "\033[3;31m"
    GREEN_ITALICS = "\033[3;32m"
    YELLOW_ITALICS = "\033[3;33m"
    BLUE_ITALICS = "\033[3;34m"
    PURPLE_ITALICS = "\033[3;35m"
    CYAN_ITALICS = "\033[3;36m"
    WHITE_ITALICS = "\033[3;37m"

    BLACK_UNDERLINED = "\033[4;30m"
    RED_UNDERLINED = "\033[4;31m"
    GREEN_UNDERLINED = "\033[4;32m"
    YELLOW_UNDERLINED = "\033[4;33m"
    BLUE_UNDERLINED = "\033[4;34m"
    PURPLE_UNDERLINED = "\033[4;35m"
    CYAN_UNDERLINED = "\033[4;36m"

    WHITE_UNDERLINED = "\033[4;37m"
    BLACK_BACKGROUND = "\033[40m"
    RED_BACKGROUND = "\033[41m"
    GREEN_BACKGROUND = "\033[42m"
    YELLOW_BACKGROUND = "\033[43m"
    BLUE_BACKGROUND = "\033[44m"
    PURPLE_BACKGROUND = "\033[45m"
    CYAN_BACKGROUND = "\033[46m"
    WHITE_BACKGROUND = "\033[47m"

    BLACK_BRIGHT = "\033[0;90m"
    RED_BRIGHT = "\033[0;91m"
    GREEN_BRIGHT = "\033[0;92m"
    YELLOW_BRIGHT = "\033[0;93m"
    BLUE_BRIGHT = "\033[0;94m"
    PURPLE_BRIGHT = "\033[0;95m"
    CYAN_BRIGHT = "\033[0;96m"
    WHITE_BRIGHT = "\033[0;97m"

    BLACK_BOLD_BRIGHT = "\033[1;90m"
    RED_BOLD_BRIGHT = "\033[1;91m"
    GREEN_BOLD_BRIGHT = "\033[1;92m"
    YELLOW_BOLD_BRIGHT = "\033[1;93m"
    BLUE_BOLD_BRIGHT = "\033[1;94m"
    PURPLE_BOLD_BRIGHT = "\033[1;95m"
    CYAN_BOLD_BRIGHT = "\033[1;96m"
    WHITE_BOLD_BRIGHT = "\033[1;97m"

    BLACK_BACKGROUND_BRIGHT = "\033[0;100m"
    RED_BACKGROUND_BRIGHT = "\033[0;101m"
    GREEN_BACKGROUND_BRIGHT = "\033[0;102m"
    YELLOW_BACKGROUND_BRIGHT = "\033[0;103m"
    BLUE_BACKGROUND_BRIGHT = "\033[0;104m"
    PURPLE_BACKGROUND_BRIGHT = "\033[0;105m"
    CYAN_BACKGROUND_BRIGHT = "\033[0;106m"
    WHITE_BACKGROUND_BRIGHT = "\033[0;107m"


class Console:
    @staticmethod
    def clear():
        print('\033[H\033[2J')

    @staticmethod
    def color(string: str, col: str) -> str:
        return col + string + Colors.RESET

    @staticmethod
    def print(string: str, col: str = Colors.RESET):
        print(Console.color(string, col))




class Prompts:
    # my_stuff =
    # "╔═══╦═══╦═══╗" +
    # "║   ║   ║   ║" +
    # "╠═══╬═══╬═══╣" +
    # "║   ║   ║   ║" +
    # "╚═══╩═══╩═══╝"

    @staticmethod
    def cn_prompt():
        Console.print('Press ENTER to continue...', Colors.RED)
        input()

    @staticmethod
    def yn_prompt(string: str, op: str):
        y = 'Y' if op == 'y' else 'y'
        n = 'N' if op == 'n' else 'n'

        Console.clear()

        Console.print(
            Console.color(string + ' [%s/%s]' % (y, n), Colors.RED)
        )

        while True:
            inp = input('> ')
            if not inp:
                inp = op
            if inp.lower() in {'y', 'n'}:
                return inp
            else:
                Console.print('Invalid input.', Colors.RED)

    @staticmethod
    def num_input(u_bound: int) -> int:
        Console.print(f'SELECT AN OPTION [1-{u_bound}]', Colors.CYAN_BOLD)

        while True:
            try:
                x = int(input())
            except ValueError:
                Console.print('Invalid input.', Colors.RED)
                continue

            if x in range(1, u_bound + 1):
                return x
            else:
                Console.print('Invalid input.', Colors.RED)

    @staticmethod
    def q_prompt(prompt: str, op: str):
        while True:
            inp = input(Console.color(prompt, Colors.BLUE_BOLD))
            if inp and Prompts.yn_prompt(inp, op):
                return inp


class MenuFormatter:
    @staticmethod
    def splash():
        Console.print(
            "        _____  _            _     _____ _           _        _____ _           _\n" +
            "        |  _ \| |          | |   / ____| |         (_)      / ____| |         (_)\n" +
            "        | |_) | | ___   ___| | _| |    | |__   __ _ _ _ __ | |    | |__   __ _ _ _ __\n" +
            "        |  _ <| |/ _ \ / __| |/ / |    | '_ \ / _` | | '_ \| |    | '_ \ / _` | | '_ \\\n" +
            "        | |_) | | (_) | (__|   <| |____| | | | (_| | | | | | |____| | | | (_| | | | | |\n" +
            "        |____/|_|\___/ \___|_|\_\\\_____|_| |_|\__,_|_|_| |_|\_____|_| |_|\__,_|_|_| |_|\n",
            Colors.BLACK_BOLD)

        Console.print(
            "               _,aaaaaaaaaaaaaaaaaaa,_                _,aaaaaaaaaaaaaaaaaaa,_\n" +
            "              ,P'                     'Y,            ,P'                     'Y,\n" +
            "             d'    ,aaaaaaaaaaaaaaa,    `b          d'    ,aaaaaaaaaaaaaaa,    `b\n" +
            "            d'   ,d'            ,aaabaaaa8aaaaaaaaaa8aaaadaaa,            'b,   `b\n" +
            "            I    I              I                            I              I    I\n" +
            "            Y,   `Y,            `aaaaaaaaaaaaaaaaaaaaaaaaaaaa'            ,P'   ,P\n" +
            "             Y,   `baaaaaaaaaaaaaaad'   ,P          Y,   `baaaaaaaaaaaaaad'   ,P\n" +
            "              `b,                     ,d'            `b,                     ,d'\n" +
            "                `baaaaaaaaaaaaaaaaaaad'                `baaaaaaaaaaaaaaaaaaad'\n",
            Colors.BLACK_BOLD_BRIGHT)

        Console.print(
            'Super secret block chain based chain with chains and blocks and crypto and blocks. Also chains.',
            Colors.RED_BOLD_BRIGHT)
        Console.print('     Developed by: Henry Tu, Yuan Song (Ryan) Zhang, Syed Safwaan, and Andrew Gao     ',
                      Colors.RED_BOLD)

    @staticmethod
    def option_list(options: Union[List[str], Dict[str, str]]) -> int:
        if type(options) is list:
            options = {x: Colors.BLACK_BOLD for x in options}

        Console.print(f'╔═══╦{"═" * 15}╗', Colors.BLACK_BOLD)
        for i, (option, col) in enumerate(options.items(), 1):
            Console.print(f'║ {i} ║ {option:<13} ║', col)
        Console.print(f'╚═══╩{"═" * 15}╝', Colors.BLACK_BOLD)

        return Prompts.num_input(len(options))
