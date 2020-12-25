import random
import time

class Color:
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    RESET     = '\033[0m'

class Screen:
    @classmethod
    def clear(self):
        print('\033[2J', end='')

    @classmethod
    def move(self, x, y):
        print(f'\033[{x};{y}H', end='')
    
def show_tree(width):
    colors = [
        Color.RED,
        Color.YELLOW,
        Color.BLUE,
        Color.PURPLE,
        Color.CYAN,
        Color.WHITE,
    ]
    ornaments = ['o', '&', '$', '#', '?', '@', 'i', '+']
    ornament_base = 'x'
    leaf = 'A'
    star = '*'
    wood = '|'

    total = sum(range(3, width+1, 2))
    total_ornaments = int(total * 0.3)
    tree = list(ornament_base * total_ornaments + leaf * (total - total_ornaments))
    random.shuffle(tree)

    # show star
    print(star.center(width).replace(star, Color.YELLOW + star))

    # show leafs and ornaments
    for size in range(3, width+1, 2):
        line = ''
        for _ in range(size):
            line += tree.pop()
        line = line.center(width)
        line = line.replace(leaf, Color.GREEN + leaf)
        for _ in range(line.count(ornament_base)):
            line = line.replace(ornament_base, random.choice(colors) + random.choice(ornaments), 1)
        print(line)

    # show woods
    wood_size = -(-width//10)
    for size in range(wood_size):
        woods = Color.YELLOW + (wood * wood_size).center(width)
        print(woods)

    # show message and reset color
    print(random.choice(colors) + 'Merry Christmas!'.center(width))
    print(Color.RESET, end='')

def main():
    tree_width = 30
    speed = 1.0

    while True:
        try:
            Screen.move(0, 0)
            Screen.clear()
            show_tree(tree_width)
            print('Press Ctrl-C to exit this program.')
            time.sleep(speed)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
