from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
import random
import string

__version__ = "1.2"

action = ["O"]
win_condition = [0]

def set_wincondition(bitlist):
    for num in bitlist:
        if num == "1":
            win_condition[0] += 1

def bit_sec(word, limit):
    win_condition[0] = 0
    bit_list = []
    for letter in word:
        bits_bins = (bin(ord(letter))[2:])
        for binbin in bits_bins:
            bit_list.append(binbin)
    while len(bit_list) > limit:
        bit_list.remove(bit_list[0])
    return bit_list

def randomizer(big):
    random_bitholder = ""
    for letter in range(big):
        random_bitholder += random.choice(string.ascii_letters)
    return random_bitholder

def table_params(primary_bitlist, table_root):
    final_list = []
    col_list = []
    fil_list = []
    col_bit_bin = ""
    fil_bit_bin = ""
    for i in range(table_root):
        for ind in range(table_root):
            fil_num = ind*table_root+i
            col_num = ind+table_root*i
            if primary_bitlist[fil_num] == "0":
                fil_bit_bin += " "
            if primary_bitlist[fil_num] == "1":
                fil_bit_bin += primary_bitlist[fil_num]
            if primary_bitlist[col_num] == "0":
                col_bit_bin += " "
            if primary_bitlist[col_num] == "1":
                col_bit_bin += primary_bitlist[col_num]
        fil_list.append(fil_bit_bin)
        col_list.append(col_bit_bin)
        fil_bit_bin = ""
        col_bit_bin = ""
    for h in range(table_root):
        fil_number = ""
        col_number = ""
        fil_segment = fil_list[h].split(" ")
        col_segment = col_list[h].split(" ")
        for mini in fil_segment:
            if len(mini) != 0:
                fil_number += str(len(mini)) + " "
            else:
                pass
        for cmini in col_segment:
            if len(cmini) != 0:
                col_number += str(len(cmini)) + " "
            else:
                pass
        fil_list[h] = fil_number
        col_list[h] = col_number
    final_list.append(fil_list)
    final_list.append(col_list)
    return final_list

def good_button(a):
    if action[0] == "O":
        a.text=""
        a.disabled=True
        print(win_condition[0])
        win_condition[0] -= 1
        if win_condition[0] == 0:
            MyLayout.victory(MyLayout)
    if action[0] == "X":
        a.text = "X"

def bad_button(a):
    if action[0] == "O":
        a.text="ERROR"
        MyLayout.lose(MyLayout)
    if action[0] == "X":
        a.text = "X"     

class MyLayout(Widget):
    def victory(self):
        view = ModalView(size_hint=(None, None), size=(180, 120))
        winLabel = Label(text="GANASTE")
        view.add_widget(winLabel)
        view.open()
    
    def lose(self):
        view = ModalView(size_hint=(None, None), size=(180, 120))
        loseLabel = Label(text="TEQUIVOCASTE")
        view.add_widget(loseLabel)
        view.open()

    def facil(self):
        word = randomizer(4)
        primary_bitlist = bit_sec(word, 25)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 5)
        self.game(5, primary_bitlist, final_bitlist, 18)
    
    def normal(self):
        word = randomizer(15)
        primary_bitlist = bit_sec(word, 100)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 10)
        self.game(10, primary_bitlist, final_bitlist, 14)

    def dificil(self):
        word = randomizer(33)
        primary_bitlist = bit_sec(word, 225)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 15)
        self.game(15, primary_bitlist, final_bitlist, 10)

    def estupido(self):
        word = randomizer(58)
        primary_bitlist = bit_sec(word, 400)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 20)
        self.game(20, primary_bitlist, final_bitlist, 8)
    
    def clean(self):
        self.ids.proper_tabla.clear_widgets()
        self.ids.fil_label_row.clear_widgets()
        self.ids.col_label_row.clear_widgets()
    
    def toggleSim(self, val):
        if val == "O":
            self.ids.button_x.state = 'normal'
            self.ids.button_o.state = 'down'
            self.ids.button_o.disabled = True
            self.ids.button_x.disabled = False
            action.remove(action[0])
            action.append("O")
            print(action[0])
        if val == "X":
            self.ids.button_o.state = 'normal'
            self.ids.button_x.state = 'down'
            self.ids.button_x.disabled = True
            self.ids.button_o.disabled = False
            action.remove(action[0])
            action.append("X")
            print(action[0])

    def game(self, cols, primary_bitlist, final_bitlist, sal):
        self.clean()
        self.ids.proper_tabla.cols = cols
        for bitbit in primary_bitlist:
            if bitbit == "0":
                btn = Button(text=" ", background_down="", background_color=(1,1,1,1), on_release=bad_button)
                self.ids.proper_tabla.add_widget(btn)
            else:
                btn = Button(text=" ", background_down="", background_color=(1,1,1,1), on_release=good_button)
                self.ids.proper_tabla.add_widget(btn)
        for h in range(cols):
            text_L = final_bitlist[1][h]
            lbl = Label(text=text_L, font_size=sal)
            self.ids.fil_label_row.add_widget(lbl)
        for j in range(cols):
            prov_text_C = final_bitlist[0][j]
            text_C = ""
            for letter in prov_text_C:
                text_C += letter + "\n"
            lbl = Label(text=text_C, font_size=sal)
            self.ids.col_label_row.add_widget(lbl)
            text_C = ""
        self.ids.caruso.load_next()

class MyApp(App):
    def build(self):
        Builder.load_file("interface.kv")
        self.title = "R-Nonogram"
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()