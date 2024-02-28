import pygame
from pygame.locals import *
from random import shuffle, randrange
import time

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = self.generate_maze()

    def generate_maze(self):
        """
        Generating maze using depth-first search algorithm.
        Returns:
            A tuple containing vertical & horizontal walls of the maze.
        """
        def walk(x, y):
            """
            Recursive function to create the maze.
            Args: x, y: Current position in   //.
            """
            visited[y][x] = True
            directions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(directions)
            for xx, yy in directions:
                if 0 <= xx < self.width and 0 <= yy < self.height and not visited[yy][xx]:
                    if xx == x:
                        hor[max(y, yy)][x] = "+  "
                    if yy == y:
                        ver[y][max(x, xx)] = "   "
                    walk(xx, yy)

     #Initialize variables
        visited = [[False] * self.width for _ in range(self.height)]
        ver = [["|  "] * self.width + ['|'] for _ in range(self.height)] + [[]]
        hor = [["+--"] * self.width + ['+'] for _ in range(self.height + 1)]

        # Start generating maze
        walk(randrange(self.width), randrange(self.height))
        return ver, hor

class MovingRectangleGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.window_width = 1500
        self.window_height = 800
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.maze_generator = MazeGenerator(self.window_width // 30, 5 + self.window_height // 30)
        self.main_loop()

    def draw_maze(self):
        """
        Draw the maze walls on the screen.
        """
        ver, hor = self.maze_generator.maze
        borders = []
        for i in range(len(ver)):
            for j in range(len(ver[i])):
                if ver[i][j] != ' ':
                    borders.append(pygame.draw.rect(self.screen, (144, 234, 144), (j * 30, i * 30, 30, 30)))
        for i in range(len(hor)):
            for j in range(len(hor[i])):
                if hor[i][j] != ' ':
                    borders.append(pygame.draw.rect(self.screen, (144, 234, 144), (j * 30, i * 30, 30, 30)))

    def main_loop(self):
        """
        Main game loop.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            self.draw_maze()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    MovingRectangleGame()