import arcade
import math
import sys

class Snails(arcade.Window):
    path1 = 11
    path2 = 22
    head1 = 1
    head2 = 2
    width = 600
    height = 600
    size = 8
    turn = 1
    grid = []
    score_player_1 = 1
    score_player_2 = 1

    MOVEMENT_SPEED = 5
    SPRITE_SCALING_PLAYER = 0.25


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_sprite = None
        self.sprite_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.initialize_grid()

    def initialize_grid(self):
        for row in range(self.size):
            self.grid.append([])
            for column in range(self.size):
                self.grid[row].append(0)
        self.grid[0][0] = self.head1
        self.grid[self.size-1][self.size-1] = self.head2


    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()


    def mapping(self, x, y, turn):
        bw = self.width / self.size
        bh = self.height / self.size
        gr = math.floor(x / bw)
        gc = math.floor(y / bh)
        if self.grid[gr][gc] == 0:
            self.grid[gr][gc] = turn
        return gr, gc

    def get_current_pos(self, turn):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] is turn:
                    return i, j

    # def on_mouse_press(self, x, y, button, modifiers):
    #     gx, gy = self.mapping(x, y, self.turn)
    #     print(gx, gy)
    #     print(self.turn)
    #     print(self.grid)

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
                    self.player_sprite = arcade.Sprite("1.jpg", self.SPRITE_SCALING_PLAYER)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)

                    # arcade.draw_rectangle_filled(i * bw + ri, j * bh + ci, bw / 2, bh / 2, arcade.color.BLUE)
                elif self.grid[i][j] == 2:
                    self.player_sprite = arcade.Sprite("2.jpg", self.SPRITE_SCALING_PLAYER)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)
                    # arcade.draw_circle_filled(i * bw + ri, j * bh + ci, bw / 4, arcade.color.AMAZON)
                elif self.grid[i][j] is 11:
                    self.player_sprite = arcade.Sprite("11.jpg", 0.1)
                    self.player_sprite.center_x = i * bw + ri
                    self.player_sprite.center_y = j * bh + ci
                    self.player_list.append(self.player_sprite)
                elif self.grid[i][j] is 22:
                    self.player_sprite = arcade.Sprite("22.jpg", 0.1)
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

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        i, j = self.get_current_pos(self.turn)
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
                elif (self.grid[i][j+1] is (self.turn_change(self.turn)) or
                      (self.grid[i][j+1] is self.turn_change(self.turn)*11)):
                    self.turn = self.turn_change(self.turn)
                elif self.grid[i][j+1] is self.turn*11:
                    self.grid[i][j] = self.turn*11
                    while (j+1 < self.size) and (self.grid[i][j+1] is self.turn*11):
                        j += 1
                    self.grid[i][j] = self.turn
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
                elif (self.grid[i][j-1] is (self.turn_change(self.turn)) or
                      (self.grid[i][j-1] is self.turn_change(self.turn)*11)):
                    self.turn = self.turn_change(self.turn)
                elif self.grid[i][j-1] is self.turn*11:
                    self.grid[i][j] = self.turn*11
                    while (j-1 >= 0) and (self.grid[i][j-1] is self.turn*11):
                        j -= 1
                    self.grid[i][j] = self.turn
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
                elif (self.grid[i+1][j] is (self.turn_change(self.turn)) or
                      (self.grid[i+1][j] is self.turn_change(self.turn)*11)):
                    self.turn = self.turn_change(self.turn)
                elif self.grid[i+1][j] is self.turn*11:
                    self.grid[i][j] = self.turn*11
                    while (i+1 < self.size) and (self.grid[i+1][j] is self.turn*11):
                        i += 1
                    self.grid[i][j] = self.turn
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
                elif (self.grid[i-1][j] is (self.turn_change(self.turn)) or
                      (self.grid[i-1][j] is self.turn_change(self.turn)*11)):
                    self.turn = self.turn_change(self.turn)
                elif self.grid[i-1][j] is self.turn*11:
                    self.grid[i][j] = self.turn*11
                    while (i-1 >= 0) and (self.grid[i-1][j] is self.turn*11):
                        i -= 1
                    self.grid[i][j] = self.turn
                    self.turn = self.turn_change(self.turn)
        self.is_win()
        # print("Player 1 : " + str(self.score_player_1))
        # print("Player 2 : " + str(self.score_player_2))
        # # elif key == arcade.key.DOWN:/
        #     self.player_sprite.change_y = -MOVEMENT_SPEED
        # elif key == arcade.key.LEFT:
        #     self.player_sprite.change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.RIGHT:
        #     self.player_sprite.change_x = MOVEMENT_SPEED


    def turn_change(self, turn):
        if turn is 1:
            turn = 2
        else:
            turn = 1
        return turn

    def is_stop(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] is 0:
                    return False
        return True

    def is_win(self):
        if self.is_stop():
            if self.score_player_1 > self.score_player_2:
                print("Player 1 win by " + str(self.score_player_1 - self.score_player_2))
                sys.exit()
            elif self.score_player_1 < self.score_player_2:
                print("Player 2 win by " + str(self.score_player_2 - self.score_player_1))
                sys.exit()
            else:
                print("Game Draw!!!")
                sys.exit()

def main():
    """ Main method """
    game = Snails(600, 600, "Snails")
    game.setup()
    arcade.run()

main()