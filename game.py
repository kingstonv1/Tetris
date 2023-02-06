import pygame
import random
import time


class Board:
    def __init__(self):
        self.bag = default_bag()
        self.active_piece = self.pull_piece()
        self.grid = [["" for x in range(10)] for y in range(20)]
        self.held_piece = None
        self.score = 0
        self.default_location = (5, 0)
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

    def move_piece(self, direction):
        temp = self.piece_location

        if direction == "Right":
            if self.piece_location[0] + self.active_piece.offset_right < 9:
                self.piece_location = (temp[0] + 1, temp[1])
        elif direction == "Left":
            if self.piece_location[0] + self.active_piece.offset_left > 0:
                self.piece_location = (temp[0] - 1, temp[1])
        else:
            return

    def hard_drop(self):
        pass


class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0

        match self.shape:
            case "I":
                self.offset_right = 0
                self.offset_left = 0
                self.offset_down = 3
            case "J":
                self.offset_right = 0
                self.offset_left = -1
                self.offset_down = 2
            case "L":
                self.offset_right = 1
                self.offset_left = 0
                self.offset_down = 2
            case "O":
                self.offset_right = 1
                self.offset_left = 0
                self.offset_down = 1
            case "S":
                self.offset_right = 1
                self.offset_left = -1
                self.offset_down = 1
            case "Z":
                self.offset_right = 1
                self.offset_left = -1
                self.offset_down = 1
            case "T":
                self.offset_right = 1
                self.offset_left = -1
                self.offset_down = 1

    def draw(self, location):
        global screen

        if self.shape == "I":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(300 + (location[0] * 40), 180 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(300 + (location[0] * 40), 220 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (0, 150, 175), rect)
            pygame.draw.rect(screen, (0, 150, 175), rect2)
            pygame.draw.rect(screen, (0, 150, 175), rect3)
            pygame.draw.rect(screen, (0, 150, 175), rect4)
        elif self.shape == "J":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(300 + (location[0] * 40), 180 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(300 + (location[0] * 40 - 40), 180 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (0, 0, 255), rect)
            pygame.draw.rect(screen, (0, 0, 255), rect2)
            pygame.draw.rect(screen, (0, 0, 255), rect3)
            pygame.draw.rect(screen, (0, 0, 255), rect4)
        elif self.shape == "L":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(300 + (location[0] * 40), 180 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(300 + (location[0] * 40 + 40), 180 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (236, 88, 0), rect)
            pygame.draw.rect(screen, (236, 88, 0), rect2)
            pygame.draw.rect(screen, (236, 88, 0), rect3)
            pygame.draw.rect(screen, (236, 88, 0), rect4)
        elif self.shape == "O":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(300 + (location[0] * 40), 180 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(300 + (location[0] * 40 + 40), 180 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (236, 88, 0), rect)
            pygame.draw.rect(screen, (236, 88, 0), rect2)
            pygame.draw.rect(screen, (236, 88, 0), rect3)
            pygame.draw.rect(screen, (236, 88, 0), rect4)
        elif self.shape == "S":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(340 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(260 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (0, 255, 0), rect)
            pygame.draw.rect(screen, (0, 255, 0), rect2)
            pygame.draw.rect(screen, (0, 255, 0), rect3)
            pygame.draw.rect(screen, (0, 255, 0), rect4)
        elif self.shape == "T":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(260 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(340 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (255, 0, 0), rect)
            pygame.draw.rect(screen, (255, 0, 0), rect2)
            pygame.draw.rect(screen, (255, 0, 0), rect3)
            pygame.draw.rect(screen, (255, 0, 0), rect4)
        elif self.shape == "Z":
            rect = pygame.Rect(300 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect2 = pygame.Rect(340 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect3 = pygame.Rect(260 + (location[0] * 40), 100 + (location[1] * 40), 40, 41)
            rect4 = pygame.Rect(300 + (location[0] * 40), 140 + (location[1] * 40), 40, 41)
            pygame.draw.rect(screen, (138, 43, 226), rect)
            pygame.draw.rect(screen, (138, 43, 226), rect2)
            pygame.draw.rect(screen, (138, 43, 226), rect3)
            pygame.draw.rect(screen, (138, 43, 226), rect4)


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

size = (1000, 1000)
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
            elif event.key == pygame.K_C:
                board.hard_drop()

    screen.fill((128, 128, 128))
    board.active_piece.draw(board.piece_location)
    draw_grid(screen)

    pygame.display.flip()
