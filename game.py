import pygame
import random

# The shapes of the pieces & rotations as coordinates on a 4x4 grid. Taken from:
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318
# because my initial approach was super inefficient.
shapes = {
    "I": [[0, 4, 8, 12], [0, 1, 2, 3]],
    "J": [[1, 5, 8, 9], [0, 4, 5, 6], [0, 1, 4, 8], [4, 5, 6, 10]],
    "L": [[0, 4, 8, 9], [4, 5, 6, 8], [0, 1, 5, 9], [4, 5, 6, 2]],
    "O": [[0, 1, 4, 5]],
    "S": [[4, 5, 1, 2], [0, 4, 5, 9]],
    "T": [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]],
    "Z": [[0, 1, 5, 6], [1, 4, 5, 8]]
}

# The colors of the pieces (R, G, B)
colors = {
    "I": (0, 175, 175),
    "J": (0, 0, 255),
    "L": (255, 80, 0),
    "O": (255, 255, 0),
    "S": (0, 255, 0),
    "T": (230, 230, 250),
    "Z": (255, 0, 0)
}

class Board:
    def __init__(self):
        self.bag = default_bag()
        self.active_piece = self.pull_piece()
        self.grid = [["" for _ in range(10)] for _ in range(20)]
        self.held_piece = None
        self.score = 0
        self.default_location = (0, 0)
        self.piece_location = self.default_location

    def pull_piece(self):
        if not self.bag:
            self.bag = default_bag()

        chosen = random.choice(self.bag)
        self.bag.remove(chosen)
        return chosen

    def hold(self):
        if self.held_piece:
            temp = self.active_piece
            self.active_piece = self.held_piece
            self.held_piece = temp
            self.piece_location = self.default_location
        else:
            self.held_piece = self.active_piece
            self.active_piece = self.pull_piece()
            self.piece_location = self.default_location

    # Pass a value of 'check' into this function in order to check a piece's position
    # against the walls (usually after rotating)
    def move_piece(self, direction):
        temp = self.piece_location

        offset_right = max(list(map(lambda x: x % 4, self.active_piece.rotation)))
        offset_left = min(list(map(lambda x: x % 4, self.active_piece.rotation)))
        piece_x = self.piece_location[0]

        start = 0
        end = 7

        if direction == "Right":
            if piece_x + offset_right <= end:
                self.piece_location = (temp[0] + 1, temp[1])

        elif direction == "Left":
            if piece_x + offset_left >= start:
                self.piece_location = (temp[0] - 1, temp[1])

        elif direction == "Check":
            # Hard-Coding an edgecase for the "I" piece becaue it was being difficult
            if piece_x + offset_right > end + 1:
                if self.active_piece.shape != "I":
                    self.piece_location = (temp[0] - offset_right + 1, temp[1])
                else:
                    self.piece_location = (temp[0] - offset_right, temp[1])

        else:
            return

    def rotate_piece(self, direction):
        if direction == "Right":
            self.active_piece.rotate(1)
        elif direction == "Left":
            self.active_piece.rotate(-1)

        self.move_piece("Check")



    def hard_drop(self):
        pass
        # for i1, x in enumerate(self.grid):
        #     for i2, y in enumerate(x):
        #         pass




class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.angle = 0
        self.rotation = shapes[self.shape][self.angle]

    def draw(self, location):
        global screen

        mat = self.rotation

        for i in range(4):
            x = 0
            y = 0
            offset = 40
            dims = (40, 40)
            temp = mat[i]

            # Get the X, Y to draw our rect at
            while temp >= 4:
                temp -= 4
                y += 1
            x = temp + 1
            y += 1

            r = pygame.Rect((location[0] * 40 + x * 40 + 300, location[1] * 40 + y * 40 + 100), dims)
            pygame.draw.rect(screen, colors[self.shape], r)

    def rotate(self, amnt):
        if self.shape != "O":
            self.angle += amnt
            self.rotation = shapes[self.shape][self.angle % len(shapes[self.shape])]


def default_bag():
    return [Piece("I"), Piece("J"), Piece("L"), Piece("O"), Piece("S"), Piece("T"), Piece("Z")]


def draw_grid(surface):
    # Grid Width = 10 boxes of 40 pixels each
    # Grid Height = 20 boxes of 40 pixels each
    OFFSET = 40

    white = (255, 255, 255)
    black = (0, 0, 0)
    points = ((300, 100), (300, 900), (700, 900), (700, 100))

    # Draw the grid outlines
    pygame.draw.lines(surface, white, closed=True, points=points, width=3)

    # Draw Vertical lines
    for i in range(1, 10):
        x = 300 + OFFSET * i
        pygame.draw.line(surface, black, start_pos=(x, 102), end_pos=(x, 898))

    # Draw Horizontal lines
    for i in range(1, 20):
        y = 100 + OFFSET * i
        pygame.draw.line(surface, black, start_pos=(300, y), end_pos=(700, y))


board = Board()

pygame.init()

size = (1000, 800)
icon = pygame.image.load('./Assets/icon.png')
last_input = 0

pygame.display.set_caption("Tetris")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.move_piece("Left")
            elif event.key == pygame.K_RIGHT:
                board.move_piece("Right")

            elif event.key == pygame.K_SPACE:
                board.hold()

            elif event.key == pygame.K_x:
                board.rotate_piece("Right")
            elif event.key == pygame.K_z:
                board.rotate_piece("Left")

            elif event.key == pygame.K_c:
                board.hard_drop()

    screen.fill((128, 128, 128))
    board.active_piece.draw(board.piece_location)
    draw_grid(screen)

    pygame.display.update()
