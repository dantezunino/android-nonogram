from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView
from kivy.utils import get_random_color
import random
import string

__version__ = "1.5"

action = ["O"]
win_condition = [0]
custom_table = [0]
game = [""]

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
            randi = random.randint(0,2)
            if randi == 0:
                bit_list.append("1")
            else:
                bit_list.append(binbin)
    while len(bit_list) > limit:
        bit_list.remove(bit_list[0])
    return bit_list

def game_set(actual):
    game.remove(game[0])
    game.append(actual)

def randomizer(big):
    random_bitholder = ""
    for letter in range(big):
        randi = random.randint(0,2)
        if randi < 2:
            random_bitholder += str(random.randint(0,1)) + random.choice(string.ascii_letters)
        else:
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
        rc = get_random_color()
        yu = (rc[0]+0.2, rc[1]+0.2, rc[2]+0.2, rc[3])
        a.background_color= yu
        a.disabled=True
        win_condition[0] -= 1
        if win_condition[0] == 0:
            MyLayout.victory(MyLayout)
    if action[0] == "X":
        if a.text == "X":
            a.text = " "
        else:
            a.text = "X"

def bad_button(a):
    if action[0] == "O":
        a.text="X"
        a.disabled=True
        MyLayout.lose(MyLayout)
    if action[0] == "X":
        if a.text == "X":
            a.text = " "
        else:
            a.text = "X"    

def add_text(a, tx):
    new_text = a
    tx.text = tx.text + new_text

def rem_text(a, tx):
    tx.text = a

def compute(view, tx, btok):
    custom_table.remove(custom_table[0])
    num = 0
    if tx == "":
        num = 0
    else:
        num = int(tx)
    custom_table.append(num)
    btok.text = "Dificultad: \n(" + str(num) + ")"


    view.dismiss()



class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.ids.btn1.background_color = get_random_color()
        self.ids.btn2.background_color = get_random_color()
        self.ids.btn3.background_color = get_random_color()
        self.ids.btn4.background_color = get_random_color()
        self.ids.btn5.background_color = get_random_color()
        self.ids.btn6.background_color = get_random_color()
        self.ids.btn7.background_color = get_random_color()
        self.ids.btn_x.background_color = get_random_color()
        self.ids.btn_r.background_color = get_random_color()

    def back(self):
        self.ids.btn1.background_color = get_random_color()
        self.ids.btn2.background_color = get_random_color()
        self.ids.btn3.background_color = get_random_color()
        self.ids.btn4.background_color = get_random_color()
        self.ids.btn5.background_color = get_random_color()
        self.ids.btn6.background_color = get_random_color()
        self.ids.btn7.background_color = get_random_color()
        self.ids.caruso.load_previous()
        self.ids.btn_x.background_color = get_random_color()
        self.ids.btn_r.background_color = get_random_color()

    def reDo(self):
        nom = game[0]
        if nom == "bebe":
            self.bebe()
        if nom == "facil":
            self.facil()
        if nom == "normal":
            self.normal()
        if nom == "dificil":
            self.dificil()
        if nom == "muydificil":
            self.muydificil()
        if nom == "custom":
            self.customOK()

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
        game_set("bebe")
        word = randomizer(4)
        primary_bitlist = bit_sec(word, 16)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 4)
        self.game(4, primary_bitlist, final_bitlist, 20)

    def custom(self):
        game_set("custom")
        view = ModalView(size_hint=(0.9, 0.5))
        box = BoxLayout(orientation='vertical')
        r_box = GridLayout(cols=3)
        lb1 = Button(text="", disabled=True, background_color=(0,0,0,1))
        lb2 = Button(text="", disabled=True, background_color=(0,0,0,1))
        tx = TextInput(text="", font_size=22, halign='center', readonly=True)
        min_box = BoxLayout(orientation='vertical')
        okbtn = Button(text="OK")
        r_box.add_widget(Button(text="1", on_press=lambda a:add_text("1",tx)))
        r_box.add_widget(Button(text="2", on_press=lambda a:add_text("2",tx)))
        r_box.add_widget(Button(text="3", on_press=lambda a:add_text("3",tx)))
        r_box.add_widget(Button(text="4", on_press=lambda a:add_text("4",tx)))
        r_box.add_widget(Button(text="5", on_press=lambda a:add_text("5",tx)))
        r_box.add_widget(Button(text="6", on_press=lambda a:add_text("6",tx)))
        r_box.add_widget(Button(text="7", on_press=lambda a:add_text("7",tx)))
        r_box.add_widget(Button(text="8", on_press=lambda a:add_text("8",tx)))
        r_box.add_widget(Button(text="9", on_press=lambda a:add_text("9",tx)))
        r_box.add_widget(Button(text="-", background_color=(0.1,0.1,0.1,1), on_press=lambda a:rem_text("",tx)))
        r_box.add_widget(Button(text="0", on_press=lambda a:add_text("0",tx)))
        r_box.add_widget(Button(text="-", background_color=(0.1,0.1,0.1,1), on_press=lambda a:rem_text("",tx)))
        min_box.add_widget(lb1)
        min_box.add_widget(tx)
        min_box.add_widget(lb2)
        box.add_widget(min_box)
        box.add_widget(okbtn)
        s_box = BoxLayout(orientation='horizontal')
        s_box.add_widget(box)
        s_box.add_widget(r_box)
        view.add_widget(s_box)
        okbtn.bind(on_press=lambda a:compute(view, tx.text, self.ids.btn7))
        view.open()

    def customOK(self):
        if custom_table[0] != 0 and custom_table[0] != 1:
            num = custom_table[0]
            squarenum = num*num
            ran = round(squarenum/3, 0)
            word = randomizer(int(ran))
            primary_bitlist = bit_sec(word, squarenum)
            set_wincondition(primary_bitlist)
            final_bitlist = table_params(primary_bitlist, num)
            self.game(num, primary_bitlist, final_bitlist, 10)
        else:
            pass

    def facil(self):
        game_set("facil")
        word = randomizer(4)
        primary_bitlist = bit_sec(word, 25)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 5)
        self.game(5, primary_bitlist, final_bitlist, 18)
    
    def normal(self):
        game_set("normal")
        word = randomizer(12)
        primary_bitlist = bit_sec(word, 64)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 8)
        self.game(8, primary_bitlist, final_bitlist, 16)

    def dificil(self):
        game_set("dificil")
        word = randomizer(25)
        primary_bitlist = bit_sec(word, 100)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 10)
        self.game(10, primary_bitlist, final_bitlist, 14)
    
    def muydificil(self):
        game_set("muydificil")
        word = randomizer(30)
        primary_bitlist = bit_sec(word, 144)
        set_wincondition(primary_bitlist)
        final_bitlist = table_params(primary_bitlist, 12)
        self.game(12, primary_bitlist, final_bitlist, 12)

    def clean(self):
        self.ids.proper_tabla.clear_widgets()
        self.ids.fil_label_row.clear_widgets()
        self.ids.col_label_row.clear_widgets()
    
    def toggleSim(self, val):
        if val == "O":
            self.ids.button_x.state = 'normal'
            self.ids.button_o.state = 'down'
            self.ids.button_o.disabled = True
            self.ids.button_o.background_color = (0.3,0,0.6,1)
            self.ids.button_o.background_disabled_normal = ""
            self.ids.button_x.background_disabled_normal = "atlas://data/images/defaulttheme/button_disabled"
            self.ids.button_x.background_color = (1,1,1,1)
            self.ids.button_x.disabled = False
            action.remove(action[0])
            action.append("O")
        if val == "X":
            self.ids.button_o.state = 'normal'
            self.ids.button_x.state = 'down'
            self.ids.button_x.disabled = True
            self.ids.button_o.background_color = (1,1,1,1)
            self.ids.button_x.background_color = (0.3,0,0.6,1)
            self.ids.button_x.background_disabled_normal = ""
            self.ids.button_o.background_disabled_normal = "atlas://data/images/defaulttheme/button_disabled"
            self.ids.button_o.disabled = False
            action.remove(action[0])
            action.append("X")

    def game(self, cols, primary_bitlist, final_bitlist, sal):
        self.clean()
        self.ids.proper_tabla.cols = cols
        for bitbit in primary_bitlist:
            if bitbit == "0":
                btn = Button(text=" ", background_down="", background_color=(0.35,0.35,0.35,1), on_release=bad_button)
                self.ids.proper_tabla.add_widget(btn)
            else:
                btn = Button(text=" ", background_down="", background_color=(0.35,0.35,0.35,1), on_release=good_button)
                self.ids.proper_tabla.add_widget(btn)
        for h in range(cols):
            text_L = final_bitlist[1][h]
            lbl = Label(text=text_L, font_size=sal)
            self.ids.fil_label_row.add_widget(lbl)
        for j in range(cols):
            prov_text_C = final_bitlist[0][j]
            text_C = ""
            sale = sal-3
            for letter in prov_text_C:
                text_C += letter + "\n"
            lbl = Label(text=text_C, font_size=sale)
            self.ids.col_label_row.add_widget(lbl)
            text_C = ""
        if self.ids.caruso.index == 1:
            self.ids.caruso.load_next()
        else:
            pass

class MyApp(App):
    def build(self):
        Builder.load_file("interface.kv")
        self.title = "R-Nonogram"
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()
