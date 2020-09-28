import tkinter as tk
from ex12.game import Game
from ex12.ai import AI
from PIL import ImageTk, Image
MSG_A ="The winner is player number 1"
MSG_B = "The winner is player number 2"
MSG_TIE = "Tie Game!"
MAIN_TITLE = "Welcom to the game:\n Connect Four!!\n\n Please choose game mode to start playing"


class MainScreen:
    """this class is the main screen of the game"""
    def __init__(self, root):
        self.__root= root
        self.__mainscreen = tk.Canvas(self.__root, width = 700, height = 500 ,
                                      bg="steel blue")
        self.__mainscreen.pack()
        self.__root.title("Connect Four!")
        self.__backgroundimage=ImageTk.PhotoImage(file='ex12/background.jpg')
        self.__mainscreen.create_image(0, 0, image=self.__backgroundimage,
                                       anchor=tk.NW )
        b1 = tk.Button(self.__mainscreen, text="player vs player",
                       command = self.change_mode(1))
        b1.place(x=305, y=200)
        b2 = tk.Button(self.__mainscreen, text="player vs computer",
                       command = self.change_mode(2))
        b2.place(x=295, y=250)
        b3 = tk.Button(self.__mainscreen, text="computer vs player",
                       command = self.change_mode(3))
        b3.place(x=295, y=300)
        b4 = tk.Button(self.__mainscreen, text="computer vs computer",
                       command = self.change_mode(4))
        b4.place(x=285, y=350)

    def change_mode(self,num):
        """this function open the chosen game mode """
        def move():
            self.__mainscreen.destroy()
            self.__game = Game()
            MyConnectFour(self.__root, self.__game, num)
        return move


class MyConnectFour:
    """this class is the main class that represent the board screen """
    def __init__(self, root, game, mode):
        self.__root = root
        self.__game = game
        self.__game_mode = mode
        self.__backgroundimage=Image.open('ex12/background2.jpg')
        self.__backgroundimage =self.__backgroundimage.resize((700,675),Image.
                                                              ANTIALIAS)
        self.__backgroundimage=ImageTk.PhotoImage(self.__backgroundimage)
        self.__root.title("Connect Four!")
        self.__c = tk.Canvas(self.__root, width=700, height=675)
        self.__c.create_image(0, 0, image=self.__backgroundimage, anchor=tk.NW)
        self.__c.pack(side=tk.LEFT)
        self.__board_state = self.create_board()
        self.__computer = None
        self.__computer2 = None
        self.__player_canvas = tk.Canvas(self.__root, width=400, height=400)
        self.__player_canvas.pack(side=tk.LEFT,fill=tk.BOTH ,expand=tk.TRUE)
        self.__red_gif = ImageTk.PhotoImage(file='ex12/yellow.jpeg' )
        self.__yellow_gif= ImageTk.PhotoImage(file="ex12/red.png")
        self.__up=ImageTk.PhotoImage(file='ex12/up.png')
        self.__down=ImageTk.PhotoImage(file='ex12/down.png')
        self.__player_canvas.pack()
        player_title = tk.Label(self.__player_canvas, text="\n\nThe Players:\n")
        player_title.pack(side=tk.TOP)
        self._display_label = tk.Label(self.__player_canvas, image=self.__yellow_gif)
        self.__player_display_label=tk.Label(self.__player_canvas,image=self.__down)
        self._display_label2 = tk.Label(self.__player_canvas, image=self.__red_gif)
        self._display_label.pack(side=tk.TOP)
        self.__player_display_label.pack(side=tk.TOP)
        self._display_label2.pack(side=tk.TOP)

        b8 = tk.Button(self.__player_canvas, text="reset game",command=self.reset,)
        b8.pack(side=tk.BOTTOM)
        b9 = tk.Button(self.__player_canvas, text="exit",
                       command=self.__root.destroy)
        b9.pack(side=tk.BOTTOM)
        self.single_game()


    def get_game_winner(self):
        return self.__game.get_winner()

    def single_game(self):
        """this function create the game by the chosen mode"""
        if self.__game_mode == 1:
            self.create_buttons()
        elif self.__game_mode == 2:
            self.__computer = AI(self.__game, 2)
            self.create_buttons()
        elif self.__game_mode == 3:
            self.create_buttons()
            self.__computer = AI(self.__game, 1)
            try:
                col = self.__computer.find_legal_move()
                self.__root.after(1000, lambda: self.player_move(col))
            except Exception:
                pass
        elif self.__game_mode == 4:
            self.__computer = AI(self.__game, 1)
            self.__computer2 = AI(self.__game, 2)
            self.comp_vs_comp(self.__computer)

    def comp_vs_comp(self,computer):
        """this function is control the computer vs computer mode"""
        if self.__game.get_winner() is not None:
            return
        if self.__game.get_current_player == 1:
            col = computer.find_legal_move()
            self.player_move(col)
            self.__root.after(900,lambda :self.comp_vs_comp(self.__computer2))
        else:
            col = computer.find_legal_move()
            self.player_move(col)
            self.__root.after(900,lambda :self.comp_vs_comp(self.__computer))

    def reset(self):
        """this function reset the board"""
        self.__c.delete("all")
        self.__c.create_image(0, 0, image=self.__backgroundimage,anchor=tk.NW)
        self.__game = Game()
        self.__board_state = self.create_board()
        self.__player_display_label.config(image=self.__down)

    def create_board(self):
        """this function create the board"""
        board_state = []
        for i in range(10, 700, 105):
            column = []
            for k in range(50, 700, 105):
                column.append(self.__c.create_oval(i, k, i + 50, k + 50,
                                                   fill="black",
                                                   outline="white"))
            board_state.append(column)
        return board_state

    def create_buttons(self):
        """this function create the buttons"""
        b1 = tk.Button(self.__c, text="drop disc", command=self.change(0))
        b1.place(x=10, y=10)
        b2 = tk.Button(self.__c, text="drop disc", command=self.change(1))
        b2.place(x=115, y=10)
        b3 = tk.Button(self.__c, text="drop disc", command=self.change(2))
        b3.place(x=220, y=10)
        b4 = tk.Button(self.__c, text="drop disc", command=self.change(3))
        b4.place(x=325, y=10)
        b5 = tk.Button(self.__c, text="drop disc", command=self.change(4))
        b5.place(x=430, y=10)
        b6 = tk.Button(self.__c, text="drop disc", command=self.change(5))
        b6.place(x=535, y=10)
        b7 = tk.Button(self.__c, text="drop disc", command=self.change(6))
        b7.place(x=640, y=10)

    def change(self, num):
        """"this function drop disc after the button clicked or after the Ai
        PLAYS
        """
        def change_row():
                if self.__game_mode == 1:
                    self.player_move(num)
                else:
                    if (self.__game_mode == 2 and  (self.__game.get_counter()
                                                    +1)%2 !=0)\
                    or (self.__game_mode == 3 and self.__game.
                            get_current_player() == 1):
                        self.player_move(num)
                        col = self.__computer.find_legal_move()
                        self.__root.after(1500, lambda: self.player_move(col))
        return change_row

    def player_move(self,num):
        """this function drop the disc and  emphasize thw winning strike"""
        if self.__game.get_winner() is None:  # check if the game is not over
            try:
                lst = self.__game.make_move(num)
                row = self.__game.get_row()
                if self.__game.get_current_player() == 1:
                    self.__c.itemconfig(self.__board_state[num][row],
                                        fill="yellow")
                    self.__player_display_label.config(image=self.__up)
                elif self.__game.get_current_player() == 2:
                    self.__c.itemconfig(self.__board_state[num][row],
                                        fill="red")
                    self.__player_display_label.config(
                        image=self.__down)

                if self.__game.get_winner() is not None:
                    if self.__game.get_winner() == 1:
                        for i in lst:
                            self.__c.itemconfig(
                                self.__board_state[i[1]][i[0]],
                                outline='blue', width=5)
                        self.win_mes(MSG_A)
                    elif self.__game.get_winner() == 2:
                        for i in lst:
                            self.__c.itemconfig(
                                self.__board_state[i[1]][i[0]],
                                outline='blue', width=5)
                        self.win_mes(MSG_B)
                    elif self.__game.get_winner() == 0:
                        self.win_mes(MSG_TIE)
            except Exception:
                pass

    def reset_close(self, name):
        """this function transfer the user into the main screen after the user
        choose play agin"""
        def close():
            name.destroy()
            self.__c.destroy()
            self.__player_canvas.destroy()
            self.__game = MainScreen(self.__root)
        return close

    def win_mes(self, msg):
        """this function showing win message"""
        popup = tk.Toplevel(self.__root)
        popup.wm_title("Game Over!")
        popup.tkraise(self.__root)

        tk.Label(popup, text=msg).pack(side="top", fill="x", pady=10)
        tk.Button(popup, text="play again",
                  command=self.reset_close(popup)).pack()
        tk.Button(popup, text="close game",
                  command=self.__root.destroy).pack()


if __name__ == '__main__':
    root = tk.Tk()

    MainScreen(root)
    root.mainloop()
