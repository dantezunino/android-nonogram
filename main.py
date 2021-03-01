from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.utils import get_random_color
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
        a.background_disabled_normal=""
        a.background_disabled_down=""
        a.background_color= get_random_color()
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
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.ids.btn1.background_color = get_random_color()
        self.ids.btn2.background_color = get_random_color()
        self.ids.btn3.background_color = get_random_color()
        self.ids.btn4.background_color = get_random_color()
        self.ids.btn5.background_color = get_random_color()
        self.ids.btn6.background_color = get_random_color()
        self.ids.btn_x.background_color = get_random_color()

    def back(self):
        self.ids.btn1.background_color = get_random_color()
        self.ids.btn2.background_color = get_random_color()
        self.ids.btn3.background_color = get_random_color()
        self.ids.btn4.background_color = get_random_color()
        self.ids.btn5.background_color = get_random_color()
        self.ids.btn6.background_color = get_random_color()
        self.ids.caruso.load_previous()
        self.ids.btn_x.background_color = get_random_color()

    def victory(self):
        view = ModalView(size_hint=(None, None), size=(240, 180))
        winLabel = Label(text="GANASTE")
        view.add_widget(winLabel)
        view.open()
    
    def lose(self):
        view = ModalView(size_hint=(None, None), size=(240, 180))
        loseLabel = Label(text="MISS-CLICK, OOPS")
        view.add_widget(loseLabel)
        view.open()

    def bebe(self):
        word = randomizer(4)
        primary_bitlist = bit_sec(word, 16)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 4)
        self.game(4, primary_bitlist, final_bitlist, 20)

    def facil(self):
        word = randomizer(4)
        primary_bitlist = bit_sec(word, 25)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 5)
        self.game(5, primary_bitlist, final_bitlist, 18)
    
    def normal(self):
        word = randomizer(12)
        primary_bitlist = bit_sec(word, 64)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 8)
        self.game(8, primary_bitlist, final_bitlist, 16)

    def dificil(self):
        word = randomizer(25)
        primary_bitlist = bit_sec(word, 100)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 10)
        self.game(10, primary_bitlist, final_bitlist, 14)
    
    def muydificil(self):
        word = randomizer(30)
        primary_bitlist = bit_sec(word, 144)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 12)
        self.game(12, primary_bitlist, final_bitlist, 12)

    def estupido(self):
        word = randomizer(33)
        primary_bitlist = bit_sec(word, 225)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 15)
        self.game(15, primary_bitlist, final_bitlist, 10)
    
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
                btn = Button(text=" ", background_down="", background_color=(0.3,0.3,0.3,1), on_release=bad_button)
                self.ids.proper_tabla.add_widget(btn)
            else:
                btn = Button(text=" ", background_down="", background_color=(0.3,0.3,0.3,1), on_release=good_button)
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
    
    def on_start(self):
        view = ModalView(size_hint=(None, None), size=(350, 500))
        box = BoxLayout(orientation='vertical')
        winLabel = Label(text="Bienvenido. Si nunca jugaste a esto, las reglas son sencillas!", text_size=(300, 150), valign="middle")
        secLabel = Label(text="1: Los números en filas y columnas indican la cantidad de casilleros contigüos a presionar.", text_size=(300, 150), valign="middle")
        terLabel = Label(text="Esas son las reglas :)", text_size=(300, 150), valign="middle")
        box.add_widget(winLabel)
        box.add_widget(secLabel)
        box.add_widget(terLabel)
        view.add_widget(box)
        view.open()

if __name__ == "__main__":
    MyApp().run()