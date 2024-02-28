
class piece:
    def __init__(self, value=None, team=None):
        self.value = value
        self.team = team

    def __str__(self):
        if self.value is not None:
            if self.team == 'w':
                stri = "\033[1;37;48m" + self.value + "\033[1;39;48m"
            else:
                stri = "\033[1;30;48m" + self.value + "\033[1;39;48m"
        else:
            stri = " "
        return stri


class chess:
    def __init__(self):
        self.gamewonyet = False
        self.lost = []
        self.turn = "w"
        self.board = [[] for _ in range(8)]
        self.lastmovedone = []
        self.lastmoveate = None
        for i in range(0, 8, 7):
            if i == 0:
                color = 'b'
            else:
                color = 'w'
            self.board[i].append(piece("♜", color))
            self.board[i].append(piece("♞", color))
            self.board[i].append(piece("♝", color))
            if i == 7:
                self.board[i].append(piece("♛", color))
                self.board[i].append(piece("♚", color))
            else:
                self.board[i].append(piece("♚", color))
                self.board[i].append(piece("♛", color))
            self.board[i].append(piece("♝", color))
            self.board[i].append(piece("♞", color))
            self.board[i].append(piece("♜", color))
        for _ in range(8):
            self.board[1].append(piece("♟", 'b'))
            self.board[6].append(piece("♟", 'w'))
        for i in range(2, 6):
            for _ in range(8):
                self.board[i].append(piece())

    def is_check(self, color):
        temp = chess()
        temp.board = self.board
        for i in range(len(temp.board)):
            for j in range(len(temp.board[i])):
                if temp.board[i][j].value is not None:
                    if temp.board[i][j].team == color:
                        if temp.board[i][j].value == "♟":
                            if j == 0:
                                if color == "w":
                                    if (temp.board[i - 1][j + 1].value == "♚" and temp.board[i - 1][j + 1].team != temp.board[i][j].team) :
                                        return True
                                else:
                                    if (temp.board[i + 1][j + 1].value == "♚" and temp.board[i + 1][j + 1].team != temp.board[i][j].team):
                                        return True
                            elif j == 7:
                                if color == "w":
                                    if (temp.board[i-1][j-1].value == "♚" and temp.board[i-1][j-1].team != temp.board[i][j].team):
                                        return True
                                else:
                                    if(temp.board[i+1][j-1].value == "♚" and temp.board[i+1][j-1].team != temp.board[i][j].team):
                                        return True
                            else :
                                if color == "w":
                                    if (temp.board[i-1][j+1].value == "♚" and temp.board[i-1][j+1].team != temp.board[i][j].team) or (temp.board[i-1][j-1].value == "♚" and temp.board[i-1][j-1].team != temp.board[i][j].team):
                                        return True
                                else:
                                    if (temp.board[i+1][j+1].value == "♚" and temp.board[i+1][j+1].team != temp.board[i][j].team) or (temp.board[i+1][j-1].value == "♚" and temp.board[i+1][j-1].team != temp.board[i][j].team):
                                        return True
                        elif temp.board[i][j].value == "♜":
                            add = 1
                            try:
                                while temp.board[i][j+add].value is None:
                                    add += 1
                                if temp.board[i][j+add].value == "♚" and temp.board[i][j+add].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i + add][j].value is None:
                                    add += 1
                                if temp.board[i + add][j].value == "♚" and temp.board[i + add][j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i][j - add].value is None:
                                    add += 1
                                if temp.board[i][j - add].value == "♚" and temp.board[i][j - add].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i - add][j].value is None:
                                    add += 1
                                if temp.board[i - add][j].value == "♚" and temp.board[i - add][j].team != color:
                                    return True
                            except IndexError:
                                pass
                        elif temp.board[i][j].value == "♞":
                            try:
                                if (temp.board[i+1][j-2].value == "♚" and temp.board[i+1][j-2].team != color) or (temp.board[i+2][j - 1].value == "♚" and temp.board[i+2][j - 1].team != color) or (temp.board[i+2][j + 1].value == "♚" and temp.board[i+2][j + 1].team != color) or (temp.board[i+1][j + 2].value == "♚" and temp.board[i+1][j + 2].team != color) or(temp.board[i-1][j + 2].value == "♚" and temp.board[i-1][j + 2].team != color) or (temp.board[i-1][j - 2].value == "♚" and temp.board[i-1][j - 2].team != color) or (temp.board[i-2][j - 1].value == "♚" and temp.board[i-2][j - 1].team != color) or (temp.board[i-2][j + 1].value == "♚" and temp.board[i-2][j + 1].team != color):
                                    return True
                            except IndexError:
                                pass
                        elif temp.board[i][j].value == "♝":
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i+add_i][j+add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i+add_i][j+add_j].value == "♚" and temp.board[i +add_i][j+add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i - add_i][j + add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i - add_i][j + add_j].value == "♚" and temp.board[i - add_i][j + add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i + add_i][j - add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i + add_i][j - add_j].value == "♚" and temp.board[i + add_i][j - add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i - add_i][j - add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i - add_i][j - add_j].value == "♚" and temp.board[i - add_i][j - add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                        elif temp.board[i][j].value == "♛":
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i + add_i][j + add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i + add_i][j + add_j].value == "♚" and temp.board[i + add_i][
                                    j + add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i - add_i][j + add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i - add_i][j + add_j].value == "♚" and temp.board[i - add_i][
                                    j + add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i + add_i][j - add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i + add_i][j - add_j].value == "♚" and temp.board[i + add_i][
                                    j - add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add_i, add_j = 1, 1
                            try:
                                while temp.board[i - add_i][j - add_j].value is None:
                                    add_i += 1
                                    add_j += 1
                                if temp.board[i - add_i][j - add_j].value == "♚" and temp.board[i - add_i][j - add_j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i][j + add].value is None:
                                    add += 1
                                if temp.board[i][j + add].value == "♚" and temp.board[i][j + add].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i + add][j].value is None:
                                    add += 1
                                if temp.board[i + add][j].value == "♚" and temp.board[i + add][j].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i][j - add].value is None:
                                    add += 1
                                if temp.board[i][j - add].value == "♚" and temp.board[i][j - add].team != color:
                                    return True
                            except IndexError:
                                pass
                            add = 1
                            try:
                                while temp.board[i - add][j].value is None:
                                    add += 1
                                if temp.board[i - add][j].value == "♚" and temp.board[i - add][j].team != color:
                                    return True
                            except IndexError:
                                pass
                        elif temp.board[i][j].value == "♚":
                            try:
                                if temp.board[i][j-1].value == "♚" or temp.board[i][j+1].value == "♚" or temp.board[i+1][j].value == "♚" or temp.board[i-1][j].value == "♚" or temp.board[i-1][j-1].value == "♚" or temp.board[i-1][j+1].value == "♚" or temp.board[i+1][j-1].value == "♚" or temp.board[i+1][j+1].value == "♚":
                                    return True
                            except IndexError:
                                pass
        return False


    def show_board(self):
        if self.turn =="w":
            print()
            a = 7
            for ele in self.board:
                print(end="\t\t")
                for j in range(len(ele)):
                    if j != len(ele)-1:
                        print(ele[j], end="|")
                    else:
                        print(ele[j], end="\t\t ")
                        for i in range(65, 73):
                            print(f"{chr(i)}{str(a + 1)}", end=" ")
                        a -= 1
                        if len(self.lost) != 0:
                            lst_2, lst_1 = [], []
                            for ele in self.lost:
                                if ele.team == 'w':
                                    lst_1.append(ele)
                                else:
                                    lst_2.append(ele)
                            if a==5:
                                print("\tLost pieces WHITE: ", end=" ")
                                for ele in lst_1:
                                    stri = "\033[1;37;48m" + ele.value + "\033[1;39;48m"
                                    print(stri, end=" ")
                            elif a == 4:
                                print("\tLost pieces BLACK: ", end=" ")
                                for ele in lst_2:
                                    stri = "\033[1;30;48m" + ele.value + "\033[1;39;48m"
                                    print(stri, end=" ")
                            elif a==1:
                                if self.is_check("w"):
                                    print("\tCheck \033[1;37;48m" + "♚" + "\033[1;39;48m", end="")
                                elif self.is_check("b"):
                                    print("\tCheck \033[1;30;48m" + "♚" + "\033[1;39;48m", end="")
                        if a==3:
                            if self.turn =="w":
                                print("\tBLACK's turn", end="")
                            else:
                                 print("\tWHITE's turn", end="")
                        print()
        else:
            print()
            a = 1
            for idx in range(len(self.board)-1, -1, -1):
                print(end="\t\t")
                ele = self.board[idx]
                for j in range(len(ele)):
                    if j != len(ele) - 1:
                        print(ele[j], end="|")
                    else:
                        print(ele[j], end="\t\t ")
                        for i in range(65, 73):
                            print(f"{chr(i)}{str(a)}", end=" ")
                        a += 1
                        if len(self.lost) != 0:
                            lst_2, lst_1 = [], []
                            for ele in self.lost:
                                if ele.team == 'w':
                                    lst_1.append(ele)
                                else:
                                    lst_2.append(ele)
                            if a == 3:
                                print("\tLost pieces WHITE: ", end=" ")
                                for ele in lst_1:
                                    stri = "\033[1;37;48m" + ele.value + "\033[1;39;48m"
                                    print(stri, end=" ")
                            elif a == 4:
                                print("\tLost pieces BLACK: ", end=" ")
                                for ele in lst_2:
                                    stri = "\033[1;30;48m" + ele.value + "\033[1;39;48m"
                                    print(stri, end=" ")
                            #elif a == 7:
                            #    if self.is_check("w"):
                            #        print("\tCheck \033[1;37;48m" + "♚" + "\033[1;39;48m", end="")
                            #    elif self.is_check("b"):
                            #        print("\tCheck \033[1;30;48m" + "♚" + "\033[1;39;48m", end="")
                        if a == 5:
                            if self.turn == "w":
                                print("\tBLACK's turn", end="")
                            else:
                                print("\tWHITE's turn", end="")
                        print()


    def make_move(self, move):
        if move == "undo":
            self.undo()
            self.show_board()
            return
        x = len(self.lost)
        if len(move.split(" ")) != 2:
            print("wrong input")
            return False
        i, j = 8 - int(move[1]) , ord(move[0])-65
        to_i, to_j = 8 - int(move[4]), ord(move[3])-65
        if not self.turn == self.board[i][j].team:
            print(f"Not your turn")
            return False
        if to_i<0 or to_i>7 or to_j>7 or to_j<0:
            print(f"{move} not a valid position")
            return False
        elif i==to_i and j==to_j:
            print(f"{self.board[i][j]} is already in {move[3] + move[4]}")
            return False
        if self.board[i][j].value is None:
            print(f"No piece in {move[0]+move[1]}")
            return False
        elif self.board[i][j].team == self.board[to_i][to_j].team:
            if ((self.board[i][j].value == "♜" and self.board[to_i][to_j] == "♚") or (self.board[i][j].value == "♚" and self.board[to_i][to_j] == "♜")) and (self.board[i][j].team =="w" and i==7 and (j==0 or j==3)  and to_i ==7 and (to_j == 3 or to_j == 0) ) or (self.board[i][j].team =="b" and i==0 and (j==0 or j==4)  and to_i ==0 and (to_j == 4 or to_j == 0)):
                for temp0 in range(min([j, to_j]+1, max([j, to_j]))):
                    if self.board[i][temp0].value is None:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                    self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
            else:
                print(f"cannot move {self.board[i][j]} to {move[3]+move[4]}")
                return False
        elif self.board[i][j].value == "♟":
            if self.board[i][j].team == "w":
                if i == to_i+1 and to_j == j:
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j],  self .board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                elif i == to_i+2 and to_j == j:
                    if i == 6:
                        if self.board[to_i][to_j].value is None and self.board[i-1][j].value is None:
                            self.board[i][j],  self .board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                        else:
                            print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                elif i == to_i + 1 and (j == to_j +1 or j == to_j-1):
                    if self.board[to_i][to_j].value is not None:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                else:
                    print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                    return False
                if to_i == 0:
                    c = int(input("enter 1 2 3 4 for ♜ ♞ ♝ ♛ to upgrade "))
                    while c < 5 and c >- 1:
                        if c == 1:
                            self.board[to_i][to_j] = piece("♜", self.board[to_i][to_j].team)
                        elif c == 2:
                            self.board[to_i][to_j] = piece("♞", self.board[to_i][to_j].team)
                        elif c == 3:
                            self.board[to_i][to_j] = piece("♝", self.board[to_i][to_j].team)
                        elif c == 4:
                            self.board[to_i][to_j] = piece("♛", self.board[to_i][to_j].team)
                        else:
                            c = int(input("Wrong input, enter 1 2 3 4 for ♜ ♞ ♝ ♛ to upgrade "))

            else:
                if i == to_i-1 and to_j==j:
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j],  self .board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                elif i == to_i-2 and to_j == j:
                    if i == 1:
                        if self.board[to_i][to_j].value is None and self.board[i+1][j].value is None:
                            self.board[i][j],  self .board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                        else:
                            print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                elif i == to_i - 1 and (j == to_j + 1 or j == to_j-1):
                    if self.board[to_i][to_j].value is not None:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
                    else:
                        print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                        return False
                else:
                    print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                    return False
                if to_i == 7:
                    c = int(input("enter 1 2 3 4 for ♜ ♞ ♝ ♛ to upgrade "))
                    while c < 5 and c >- 1:
                        if c == 1:
                            self.board[to_i][to_j] = piece("♜", self.board[to_i][to_j].team)
                        elif c == 2:
                            self.board[to_i][to_j] = piece("♞", self.board[to_i][to_j].team)
                        elif c == 3:
                            self.board[to_i][to_j] = piece("♝", self.board[to_i][to_j].team)
                        elif c == 4:
                            self.board[to_i][to_j] = piece("♛", self.board[to_i][to_j].team)
                        else:
                            c = int(input("Wrong input, enter 1 2 3 4 for ♜ ♞ ♝ ♛ to upgrade "))
        elif self.board[i][j].value == "♜":
            if i != to_i and j != to_j:
                print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                return False
            else:
                if i == to_i:
                    for idx in range(min([to_j, j])+1, max([to_j, j])):
                        if self.board[i][idx].value is not None:
                            print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
                else:
                    for idx in range(min([to_i, i])+1, max([to_i, i])):
                        if self.board[idx][j].value is not None:
                            print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
        elif self.board[i][j].value == "♞":
            if (to_i==i+1 and to_j==j-2) or (to_i==i+2 and to_j==j-1) or (to_i==i+2 and to_j==j+1) or (to_i==i+1 and to_j==j+2) or (to_i==i-1 and to_j==j+2) or (to_i==i-1 and to_j==j-2) or (to_i==i-2 and to_j==j-1) or (to_i==i-2 and to_j==j+1):
                if self.board[to_i][to_j].value is None:
                    self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                else:
                    self.lost.append(self.board[to_i][to_j])
                    self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
            else:
                print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                return False
        elif self.board[i][j].value == "♝":
            if abs(i-to_i) == abs(j-to_j):
                if j>to_j:
                    if i>to_i:
                        idx0, idx1 = i-1, j-1
                        while idx0 != to_i and  idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 -= 1
                            idx1 -= 1
                    else:
                        idx0, idx1 = i + 1, j - 1
                        while idx0 != to_i and idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 += 1
                            idx1 -= 1
                else:
                    if i>to_i:
                        idx0, idx1 = i-1, j+1
                        while idx0 != to_i and idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 -= 1
                            idx1 += 1
                    else:
                        idx0, idx1 = i + 1, j + 1
                        while idx0 != to_i and idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 += 1
                            idx1 += 1
                if self.board[to_i][to_j].value is None:
                    self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                else:
                    self.lost.append(self.board[to_i][to_j])
                    self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
            else:
                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                return False
        elif self.board[i][j].value == "♛":
            if abs(i-to_i)==abs(j-to_j):
                if j>to_j:
                    if i>to_i:
                        idx0, idx1 = i-1, j-1
                        while idx0 != to_i and  idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 -= 1
                            idx1 -= 1
                    else:
                        idx0, idx1 = i + 1, j - 1
                        while idx0 != to_i and idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 += 1
                            idx1 -= 1
                else:
                    if i>to_i:
                        idx0, idx1 = i-1, j+1
                        while idx0 != to_i and  idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 -= 1
                            idx1 += 1
                    else:
                        idx0, idx1 = i + 1, j + 1
                        while idx0 != to_i and idx1 != to_i:
                            if self.board[idx0][idx1].value is not None:
                                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                                return False
                            idx0 += 1
                            idx1 += 1
                if self.board[to_i][to_j].value is None:
                    self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                else:
                    self.lost.append(self.board[to_i][to_j])
                    self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
            elif i == to_i or j == to_j:
                if i==to_i:
                    for idx in range(min([to_j, j])+1, max([to_j, j])):
                        if self.board[i][idx].value is not None:
                            print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
                else:
                    for idx in range(min([to_i, i])+1, max([to_i, i])):
                        if self.board[idx][j].value is not None:
                            print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                            return False
                    if self.board[to_i][to_j].value is None:
                        self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                    else:
                        self.lost.append(self.board[to_i][to_j])
                        self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
            else:
                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                return False
        elif self.board[i][j].value == "♚":
            if (to_i == i and (to_j ==j-1 or to_j==j+1)) or (to_j==j and(to_i==i+1 or to_i == i-1)) or (to_i==i-1 and (to_j==j-1 or to_j==j+1)) or (to_i==i+1 and (to_j==j-1 or to_j==j+1)):
                if self.board[to_i][to_j].value is None:
                    self.board[i][j], self.board[to_i][to_j] = self.board[to_i][to_j], self.board[i][j]
                else:
                    self.lost.append(self.board[to_i][to_j])
                    self.board[i][j], self.board[to_i][to_j] = piece(), self.board[i][j]
            else:
                print(f"Cannot move {self.board[i][j]} to {move[3] + move[4]}")
                return False
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
        self.lastmovedone = [i, j, to_i, to_j]
        if len(self.lost) != x:
            self.lastmoveate = True
        else:
            False
        if self.lost:
            if self.lost[len(self.lost)-1].value == "♚":
                self.gamewonyet = True
        return True

    def undo(self):
        if len(self.lastmovedone) != 0:
            if self.turn =="w":
                self.turn == "b"
            else:
                self.turn =="w"
            if self.lastmoveate:
                self.board[self.lastmovedone[0]][self.lastmovedone[1]], self.board[self.lastmovedone[2]][self.lastmovedone[3]] = self.board[self.lastmovedone[2]][self.lastmovedone[3]], self.lost.pop(len(self.lost - 1))
            else:
                self.board[self.lastmovedone[0]][self.lastmovedone[1]], self.board[self.lastmovedone[2]][self.lastmovedone[3]] = self.board[self.lastmovedone[2]][self.lastmovedone[3]], piece()
            self.lastmovedone.pop(len(self.lastmovedone)-1)
        else:
            print("Cannot undo")

    def make_move_safe(self, move):
        if self.make_move(move):
            if self.turn =="w":
                if self.is_check("b"):
                    self.undo()
                    print("This piece is protecting the king")
                    return False
            else:
                if self.is_check("w"):
                    self.undo()
                    print("This piece is protecting the king")
                    return False
        if self.is_check(self.turn):
            print()
            print("\t\tCheck")
        return True


    def play(self):
        print("Enter piece to destination: A7 A6")
        self.show_board()
        stri = input()
        while stri != "quit":
            state = self.make_move(stri)
            while not state:
                stri = input()
                state = self.make_move(stri)
            if self.gamewonyet:
                if self.lost[len(self.lost) - 1].team == "w":
                    print(end="\n\n")
                    print("\t\t\tBLACK WINS")
                else:
                    print(end="\n\n")
                    print("\t\t\tWHITE WINS")
                break
            self.show_board()
            stri = input()
        print(end="\n\n")
        c = input("Enter \"chess\" to play a new game or \"quit\" to exit: ")
        while c != "chess" and c!= "quit":
            c = input("Enter \"chess\" to play a new game or \"quit\" to exit: ")
        if c == "chess":
            newboard = chess()
            newboard.play()
        else:
            print()
            print("\t\t\tGREAT DAY")


s = chess()
s.play()
