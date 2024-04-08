#"Меню ресторана" это мини программа,
# которая показывает меню блюд с ценами, принимает заказ и выводит
# на экран сумма счёта
from tkinter import*
from functools import partial #A library that allows you to call a function with multiple arguments in the command button parameter
                              #Библиотека которая позволяет вызывать функцию с многочисленными аргументами в параметре кнопки command
from PIL import ImageTk,Image #Library for opening an image/Библиотека для открытия изображения

class Windows(Frame):
    '''This class runs the program'''
    '''Этот класс запускает программу'''
    def __init__(self, root):
        '''This method initialize the main window and calls the main menu method of the program'''
        '''Этот метод инициализирует главное окно и вызывает метод главного меню программы'''
        super().__init__(root)#Calls the constructor of the parent class Frame with the root argument to initialize the window.
        #Вызывает конструктор родительского класса Frame с аргументом root, чтобы проинициализировать окно.
        self.grid()
        self.main_menu()
    def callback_botton(self,text,command,row,column,columnspan=None,width=None,padx=None):
        '''This method is a button constructor'''
        '''Этот метод является конструктором кнопок'''
        self.button = Button(self,text=text,command=command,width=width,overrelief=RIDGE)
        self.button.grid(row=row,column=column,columnspan=columnspan,padx=padx,sticky=W)

    def main_menu(self):
        '''This method calls the main menu of the program'''
        '''Этот метод вызывает главное меню программы'''
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
        self.position4 = 0
        self.position5 = 0
        self.position6 = 0
        self.position7 = 0
        self.position8 = 0
        self.position9 = 0
        self.position10 = 0
        self.name_1='Хачапури'
        self.name_2='Хинкали'
        self.name_3='Чербули'
        self.name_4='Пури'
        self.name_5='Назуки'
        self.name_6='Чвиштари'
        self.name_7='Джонджоли'
        self.name_8='Салат'
        self.name_9='Бадриджани'
        self.name_10='Пхали'
        self.prices=0
        self.id = [self.position1, self.position2, self.position3,self.position4,self.position5,self.position6,self.position7,self.position8,self.position9,self.position10]
        self.menu=[self.name_1,self.name_2,self.name_3,self.name_4,self.name_5,self.name_6,self.name_7,self.name_8,self.name_9,self.name_10]
        self.price_rub={self.menu[0]:70,self.menu[1]:10,self.menu[2]:60,self.menu[3]:25,self.menu[4]:30,self.menu[5]:55,self.menu[6]:70,self.menu[7]:45,self.menu[8]:20,self.menu[9]:35}
        # self.entr = Entry(self, width=4, justify='center')
        # self.entr.grid(row=2, column=2, sticky=W)
        Label(self,text='Добро пожаловать в ресторан "Цвели Харчвели"',font='Times 20').grid(row=0,column=2,columnspan=3)
        Label(self,text='Меню',font='Times 17').grid(row=1,column=3)
        Label(self,text='1.Хачапури:',font='Times 15').grid(row=2,column=0,sticky=W)
        Label(self,text='2.Хинкали:',font='Times 15').grid(row=3,column=0,sticky=W)
        Label(self,text='3.Чербули:',font='Times 15').grid(row=4,column=0,sticky=W)
        Label(self,text='4.Пури:',font='Times 15').grid(row=5,column=0,sticky=W)
        Label(self,text='5.Назуки:',font='Times 15').grid(row=6,column=0,sticky=W)
        Label(self,text='6.Чвиштари:',font='Times 15').grid(row=7,column=0,sticky=W)
        Label(self,text='7.Джонджоли:',font='Times 15').grid(row=8,column=0,sticky=W)
        Label(self,text='8.Салат:',font='Times 15').grid(row=9,column=0,sticky=W)
        Label(self,text='9.Бадриджани:',font='Times 15').grid(row=10,column=0,sticky=W)
        Label(self,text='10.Пхали:',font='Times 15').grid(row=11,column=0,sticky=W)
        Label(self,text="Итого",font='Times 15').grid(row=12,column=2,sticky=W)
        Label(self,text="руб",font='Times 15').grid(row=12,column=2,columnspan=2,sticky=W,padx=130)
        self.image = ImageTk.PhotoImage(Image.open("geo_men-transformed2.jpg","r"))
        self.baner=Label(self,image=self.image)
        self.baner.grid(row=2,column=5,rowspan=30,sticky=NSEW)
        for i in range(2,12):
            Entry(self,width=4).grid(row=i,column=2,sticky=W)
        self.callback_botton(text='-',command=partial(self.operation_m,4,2,2,0),row=2,column=1,width=3)
        self.callback_botton(text='+',command=partial(self.operatiom_p,4,2,2,0),row=2,column=2,width=3,padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 3, 2,1), row=3, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 3, 2,1), row=3, column=2, width=3,padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 4, 2, 2), row=4, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 4, 2, 2), row=4, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 5, 2, 3), row=5, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 5, 2, 3), row=5, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 6, 2, 4), row=6, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 6, 2, 4), row=6, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 7, 2, 5), row=7, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 7, 2, 5), row=7, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 8, 2, 6), row=8, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 8, 2, 6), row=8, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 9, 2, 7), row=9, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 9, 2, 7), row=9, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 10, 2, 8), row=10, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 10, 2, 8), row=10, column=2, width=3, padx=28)
        self.callback_botton(text='-', command=partial(self.operation_m, 4, 11, 2, 9), row=11, column=1, width=3)
        self.callback_botton(text='+', command=partial(self.operatiom_p, 4, 11, 2, 9), row=11, column=2, width=3, padx=28)
        self.counter=2
        for i in range(len(self.price_rub)):
            self.pr=Label(self,text=str(self.price_rub.get(self.menu[i]))+" руб",font='Times 15').grid(row=self.counter,column=2)
            self.counter+=1
        self.fr_price = Entry(self, width=5, justify='center',font='TkDefaultFont 10 bold')
        #your_font = font.nametofont("TkDefaultFont")
        self.fr_price.grid(row=12, column=2)

    def operation_m(self,width,row,column,num):
        '''This method is called when the button responsible for subtraction is pressed,
        which is what this method does. He subtracts one dish. If the dish is 0,
        then the default method inserts 0 into the entry. It is also a constructor add-on for the entry widget.It also calls the price method
        Этот метод вызывается при нажатии кнопки, отвечающей за вычитание, что и делает этот метод. Он вычитает одно блюдо.
        Если блюдо равно 0, то метод по умолчанию вставляет 0 в запись.Также он является надстройкой-конструктором для виджета entry
        Также он вызывает метод price'''
        self.entr = Entry(self, width=width, justify='center')
        self.entr.grid(row=row, column=column, sticky=W)
        if self.id[num] <= 0:
            self.entr.delete(0, END)
            self.entr.insert(0, '0')
        else:
            self.id[num] -= 1
            self.num_txt = str(self.id[num])
            self.entr.delete(0, END)
            self.entr.insert(0, self.num_txt)
            self.price(num,"-")

    def operatiom_p(self,width,row,column,num):
        '''This method is responsible for increasing the amount of a particular dish.
        He just add 1 dish, as much as the customer wishes.It is also a constructor add-on for the entry widget.It also calls the price method
        Этот метод позволяет увеличить объем того или иного блюда.
        Он просто добавляет 1 блюдо, столько, сколько пожелает клиент.Также он является надстройкой-конструктором для виджета entry
        Также он вызывает метод price'''
        self.entr = Entry(self, width=width, justify='center')
        self.entr.grid(row=row, column=column, sticky=W)
        self.id[num] += 1
        self.num_txt = str(self.id[num])
        self.entr.delete(0, END)
        self.entr.insert(0, self.num_txt)
        self.price(num,"+")

    def price(self,num,status):
        '''This method calls the final score. It accepts two parameters.
        The first is the sum of the goods, the second arithmetic action is possible two + and -
        Этот метод вызывает итоговый счёт. Он принимает два параметра.
        Первый сумму товара, второй арифметическое действие возможно два + и -'''
        if status=="+":
            self.prices+=self.price_rub.get(self.menu[num])
            self.prices_txt=str(self.prices)
            self.fr_price.delete(0,END)
            self.fr_price.insert(0,self.prices_txt)
        else:
            self.prices-=self.price_rub.get(self.menu[num])
            self.prices_txt = str(self.prices)
            self.fr_price.delete(0, END)
            self.fr_price.insert(0, self.prices_txt)
'''The main part of the program
Основная часть программы'''
root = Tk()
root.state("zoomed")
root.title("Меню")
wind = Windows(root)
root.mainloop()
'''This program can and should be improved. 
Below I will give as notes what can be added. 
Maybe in the future the changes will be in force. 
-The pay button
-Expand the menu
Данную программу можно и есть куда улучшать. 
Ниже я приведу как заметки что можно добавить. 
Может быть в будущем изменения будут в силе. 
-Кнопку оплатить
-Расширить меню
'''