"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""  
import arcade
import pyglet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
SPRITE_SCALING=0.4
Game_Matrix=[[0,0,0],[0,0,0],[0,0,0]]

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        # Set up the player list
        self.player_list = None
        self.Turn=1
        # Set up the player info
        self.player_sprite = None

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()


        
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """
##        self.player_sprite = arcade.Sprite("cross-arcade.png", 0.5)
##        self.player_sprite.center_x = 200
##        self.player_sprite.center_y = 150
##        self.player_list.append(self.player_sprite) 
##        self.player_list.draw()


        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        for x in range(0,801,266):
            arcade.draw_line(x,0,x,600,arcade.color.BLACK,5)
        for y in range(0,601,200):
            arcade.draw_line(0,y,800,y,arcade.color.BLACK,5)
        self.player_list.draw()
        
        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.Check_in_Game_Matrix(x,y)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
    def Check_in_Game_Matrix(self,x,y):
        col=x//266
        y=600-y
        row=y//200
        print("%s %s" % (row, col))
        if Game_Matrix[row][col]==0 and self.Turn==1:
            self.Make_Cross(row,col)
        elif Game_Matrix[row][col]==0 and self.Turn==2:
            self.Make_O(row,col)
        pass
    def Make_Cross(self,row,col):
       self.player_sprite = arcade.Sprite("1.jpg", SPRITE_SCALING)
       print("%s %s %s %s" % ((row*266)+100,(col*200)+60,(row*266)+200,(col*200)+140))
       self.player_sprite.center_x = (col * 266) +120
       self.player_sprite.center_y = (SCREEN_HEIGHT-(row * 200)) - 90
       self.player_list.append(self.player_sprite)
       self.player_list.draw()
       Game_Matrix[row][col] = self.Turn
       self.Check_Win()
       self.Turn = (self.Turn % 2) + 1

    def Make_O(self,row,col):
       self.player_sprite = arcade.Sprite("2.jpg", SPRITE_SCALING)
       print("%s %s %s %s" % ((row*266)+100,(col*200)+60,(row*266)+200,(col*200)+140))
       self.player_sprite.center_x = (col*266)+120
       self.player_sprite.center_y = (SCREEN_HEIGHT-(row*200))-90
       self.player_list.append(self.player_sprite)
       self.player_list.draw()
       Game_Matrix[row][col] = self.Turn

       self.Check_Win()
       self.Check_Draw()
       self.Turn = (self.Turn % 2) + 1

    def Check_Win(self):
        self.check_diagnols()
        self.check_hr_vr();
        print(self.Turn)
        pass
    def check_diagnols(self):
        count_lr=0
        count_rl=0
        for i in range(len(Game_Matrix)):
##            print(i)
            if Game_Matrix[i][i]==self.Turn:
                count_lr=count_lr+1
                
            if Game_Matrix[len(Game_Matrix)-i-1][len(Game_Matrix)-i-1]==self.Turn:
                count_rl=count_rl+1
        if count_lr==3 or count_rl==3:
            print("%s Win!!" % self.Turn)
            arcade.close_window()
        pass
    def check_hr_vr(self):
        for i in range(len(Game_Matrix)):
            count_vr=0
            count_hr=0
            for j in range(len(Game_Matrix)):
                if Game_Matrix[i][j]==self.Turn:
                    count_vr=count_vr+1
                if Game_Matrix[j][i]==self.Turn:
                    count_hr=count_hr+1
            if count_vr==3 or count_hr==3:
                print("%s Win!!" % self.Turn)
                arcade.close_window()
        pass
    def Check_Draw(self):
        draw=True
        for i in range(len(Game_Matrix)):
            for j in range(len(Game_Matrix)):
                if Game_Matrix[i][j]==0:
                    draw=False
        if draw==True:
            print("Draw!!!! Well played")
            arcade.close_window()
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()