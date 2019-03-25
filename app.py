import arcade
import math
from copy import deepcopy
import sys
import random


class Snails(arcade.Window):

    head1 = 1
    head2 = 2
    size = 8
    turn = 1
    grid = []
    score_player_1 = 1
    score_player_2 = 1
    depth = 0

    SPRITE_SCALING_PLAYER = 0.25

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_sprite = None
        self.sprite_list = None

        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.initialize_grid()

    def initialize_grid(self):
        for row in range(self.size):
            self.grid.append([])
            for column in range(self.size):
                self.grid[row].append(0)
        self.grid[0][0] = self.head1
        self.grid[self.size-1][self.size-1] = self.head2

    def generate_childern(self, board, turn):

        list = []
        copy1 = deepcopy(board)
        copy2 = deepcopy(board)
        copy3 = deepcopy(board)
        copy4 = deepcopy(board)

        i, j = self.get_current_pos(board, turn)
        if j+1 < self.size:
            if copy1[i][j+1] is 0:
                copy1[i][j] = turn*11
                copy1[i][j+1] = turn
                list.append(copy1)
            elif copy1[i][j + 1] is turn * 11:
                copy1[i][j] = turn * 11
                while (j + 1 < self.size) and (copy1[i][j + 1] is turn * 11):
                    j += 1
                copy1[i][j] = turn
                list.append(copy1)

        i, j = self.get_current_pos(board, turn)
        if j-1 >=0:
            if copy2[i][j-1] is 0:
                copy2[i][j] = turn*11
                copy2[i][j-1] = turn
                list.append(copy2)
            elif copy2[i][j - 1] is turn * 11:
                copy2[i][j] = turn * 11
                while j - 1 >= 0 and copy2[i][j - 1] is turn * 11:
                    j -= 1
                copy2[i][j] = turn
                list.append(copy2)

        i, j = self.get_current_pos(board, turn)
        if i+1 < self.size:
            if copy3[i+1][j] is 0:
                copy3[i][j] = turn * 11
                copy3[i+1][j] = turn
                list.append(copy3)
            elif copy3[i + 1][j] is turn * 11:
                copy3[i][j] = turn * 11
                while (i + 1 < self.size) and (copy3[i + 1][j] is turn * 11):
                    i += 1
                copy3[i][j] = turn
                list.append(copy3)

        i, j = self.get_current_pos(board, turn)
        if i-1 >= 0:
            if copy4[i-1][j] is turn*11:
                copy4[i][j] = turn*11
                while (i-1 >= 0) and (copy4[i-1][j] is turn*11):
                    i -= 1
                copy4[i][j] = turn
                list.append(copy4)
            elif i-1 >=0 and copy4[i-1][j] is 0:
                copy4[i][j] = turn*11
                copy4[i-1][j] = turn
                list.append(copy4)

        return list

    def setup(self):
        self.player_list = arcade.SpriteList()

    def mapping(self, x, y, turn):
        bw = self.width / self.size
        bh = self.height / self.size
        gr = math.floor(x / bw)
        gc = math.floor(y / bh)
        if self.grid[gr][gc] == 0:
            self.grid[gr][gc] = turn
        return gr, gc

    def get_current_pos(self, board, turn):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] is turn:
                    return i, j

    def draw_screen(self):

        ri = self.width / self.size
        ci = self.height / self.size
        ri1 = self.width / self.size
        ci1 = self.height / self.size
        for i in range(self.size - 1):
            arcade.draw_line(0, ci, self.width, ci, arcade.color.BLACK)
            arcade.draw_line(ri, 0, ri, self.height, arcade.color.BLACK)
            ri += ri1
            ci += ci1

        for i in range(self.size):
            for j in range(self.size):
                bw = self.width / self.size
                bh = self.height / self.size
                ri = int(bw / 2)
                ci = int(bh / 2)
                if self.grid[i][j] == 1:
                    self.player_sprite = arcade.Sprite("1.jpg", 0.1)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)

                elif self.grid[i][j] == 2:
                    self.player_sprite = arcade.Sprite("2.jpg", 0.08)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)
                elif self.grid[i][j] is 11:
                    self.player_sprite = arcade.Sprite("11.jpg", 0.09)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)
                elif self.grid[i][j] is 22:
                    self.player_sprite = arcade.Sprite("22.jpg", 0.075)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)
        self.player_list.draw()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.draw_screen()
        if self.is_win(self.grid, self.turn):
            print("Player "+str(self.turn)+" has won")
            sys.exit()
        elif self.is_draw(self.grid, self.turn):
            "Game Drawn"
            sys.exit()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        i, j = self.get_current_pos(self.grid, self.turn)
        if self.turn is 1:
            if key == arcade.key.UP:
                if (j+1) < self.size:
                    if self.grid[i][j+1] is 0:
                        self.grid[i][j+1] = self.turn
                        self.grid[i][j] = self.turn*11
                        if self.turn is 1:
                            self.score_player_1 += 1
                        elif self.turn is 2:
                            self.score_player_2 += 1
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif (self.grid[i][j+1] is (self.turn_change(self.turn)) or
                          (self.grid[i][j+1] is self.turn_change(self.turn)*11)):
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif self.grid[i][j+1] is self.turn*11:
                        self.grid[i][j] = self.turn*11
                        while (j+1 < self.size) and (self.grid[i][j+1] is self.turn*11):
                            j += 1
                        self.grid[i][j] = self.turn
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)

            elif key == arcade.key.DOWN:
                if (j-1) >= 0:
                    if self.grid[i][j - 1] is 0:
                        self.grid[i][j-1] = self.turn
                        self.grid[i][j] = self.turn*11
                        if self.turn is 1:
                            self.score_player_1 += 1
                        elif self.turn is 2:
                            self.score_player_2 += 1
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif (self.grid[i][j-1] is (self.turn_change(self.turn)) or
                          (self.grid[i][j-1] is self.turn_change(self.turn)*11)):
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif self.grid[i][j-1] is self.turn*11:
                        self.grid[i][j] = self.turn*11
                        while (j-1 >= 0) and (self.grid[i][j-1] is self.turn*11):
                            j -= 1
                        self.grid[i][j] = self.turn
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)

            elif key == arcade.key.RIGHT:
                if (i+1) < self.size:
                    if self.grid[i+1][j] is 0:
                        self.grid[i+1][j] = self.turn
                        self.grid[i][j] = self.turn*11
                        if self.turn is 1:
                            self.score_player_1 += 1
                        elif self.turn is 2:
                            self.score_player_2 += 1
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif (self.grid[i+1][j] is (self.turn_change(self.turn)) or
                          (self.grid[i+1][j] is self.turn_change(self.turn)*11)):
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif self.grid[i+1][j] is self.turn*11:
                        self.grid[i][j] = self.turn*11
                        while (i+1 < self.size) and (self.grid[i+1][j] is self.turn*11):
                            i += 1
                        self.grid[i][j] = self.turn
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)

            elif key == arcade.key.LEFT:
                if (i-1) >= 0:
                    if self.grid[i-1][j] is 0:
                        self.grid[i-1][j] = self.turn
                        self.grid[i][j] = self.turn*11
                        if self.turn is 1:
                            self.score_player_1 += 1
                        elif self.turn is 2:
                            self.score_player_2 += 1
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif (self.grid[i-1][j] is (self.turn_change(self.turn)) or
                          (self.grid[i-1][j] is self.turn_change(self.turn)*11)):
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)
                    elif self.grid[i-1][j] is self.turn*11:
                        self.grid[i][j] = self.turn*11
                        while (i-1 >= 0) and (self.grid[i-1][j] is self.turn*11):
                            i -= 1
                        self.grid[i][j] = self.turn
                        self.turn = self.turn_change(self.turn)
                        a, b = self.search_tree(self.grid, self.turn, 0)
                        self.grid = b
                        self.turn = self.turn_change(self.turn)

    def turn_change(self, turn):
        if turn is 1:
            turn = 2
        else:
            turn = 1
        return turn

    def count_score(self, board, turn):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] is turn or board[i][j] is turn*11:
                    score += 1
        return score

    def is_board_full(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] is 0:
                    return False
        return True

    def is_win(self, board, turn):
        if self.is_board_full(board):
            if self.count_score(board, turn) > self.count_score(board, self.turn_change(turn)):
                return True
        else:
            return False

    def is_lose(self, board, turn):
        if self.is_board_full(board):
            if self.count_score(board, turn) < self.count_score(board, self.turn_change(turn)):
                return True
        else:
            return False

    def is_draw(self, board, turn):
        if self.is_board_full(board):
            if self.count_score(board, turn) is self.count_score(board, self.turn_change(turn)):
                return True
            else:
                return False

    def is_continue(self, board):
        if self.is_board_full(board) is False:
            return True
        else:
            return False

    def evaluate_board(self, board, turn):
        if self.is_win(board, turn):
            return 10
        elif self.is_lose(board, turn):
            return -10
        elif self.is_draw(board, turn):
            return 5
        else:
            return 0

    def get_max(self, score_list):
        max = 0
        max_ind = 0
        for index, i in enumerate(score_list):
            if i >= max:
                max = i
                max_ind = index
        return max_ind, max

    def get_min(self, score_list):
        min = 0
        min_ind = 0
        for index, i in enumerate(score_list):
            if i <= min:
                min = i
                min_ind = index
        return min_ind, min

    def search_tree(self, board, turn, depth):
        childern_score = []
        list = self.generate_childern(board, turn)
        random.shuffle(list)
        for i in list:
            if self.evaluate_board(i, turn) is 10:
                childern_score.append(20)
            elif self.evaluate_board(i, turn) is 5:
                childern_score.append(5)
            elif self.evaluate_board(i, turn) is -10:
                childern_score.append(-10)
            elif self.evaluate_board(i, turn) is 0 and depth < 4:
                if depth >= 3:
                    childern_score.append(14-self.find_distance(i, turn))
                else:
                    p, q = self.search_tree(i, self.turn_change(turn), depth+1)
        if turn is 1:
            p, q = self.get_min(childern_score)
            return q, list[p]
        else:
            p, q = self.get_max(childern_score)
            return q, list[p]

    def find_distance(self, board, turn):
        i, j = self.get_current_pos(board, turn)
        i1, j1 = self.get_current_pos(board, self.turn_change(turn))
        return abs(i1-i)+abs(j1-j)

def main():
    game = Snails(600, 600, "Snails")
    game.setup()
    arcade.run()


main()
