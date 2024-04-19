from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QTimeEdit
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from time import sleep

win = QApplication([])
main_win1 = QWidget()
main_win1.setWindowTitle('здоровье')
main_win1.resize(800,600)
main_win2 = QWidget()
main_win2.setWindowTitle('здоровье')
main_win2.resize(800,600)
main_win3 = QWidget()
main_win3.setWindowTitle('здоровье')
main_win3.resize(1000,800)
#ПЕРВОЕ ОКНО----------------------------------------------------------------------------------------------


def first_button_click():
    main_win1.hide()
    main_win2.show()


first_text = QLabel('Добро пожаловать в программу по определения сдоровья!')
second_text = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )


first_button = QPushButton('Начать')


vline1_on_first_win = QVBoxLayout()

vline1_on_first_win.addWidget(first_text,alignment = Qt.AlignLeft)
vline1_on_first_win.addWidget(second_text,alignment = Qt.AlignLeft)
vline1_on_first_win.addWidget(first_button,alignment = Qt.AlignCenter)

first_button.clicked.connect(first_button_click)


main_win1.setLayout(vline1_on_first_win)
main_win1.show()


# ВТОРОЕ ОКНО--------------------------------------------------------------------------------
# global time
# def timer1Event():
#     global time
#     time = QTime(0, 0, 15)
#     timer = QTimer()
#     timer.timeout.connect(timer1Event)
#     timer.start(1000)
#     time = time.addSecs(-1)
#     text_timer.setText(time.toString("hh:mm:ss"))
#     text_timer.setFont(QFont("Times", 36, QFont.Bold))
#     text_timer.setStyleSheet("color: rgb(0,0,0)")

#     if time.toString("hh:mm:ss") == "00:00:00":
#         timer.stop()

text_timer = QLabel(time)
text_timer.setFont(QFont("Times", 36, QFont.Bold))


third_text = QLabel('Введите Ф.И.О.')
first_line_edit = QLineEdit('Ф.И.О.')
forth_text = QLabel('Полных лет')
second_line_edit = QLineEdit('0')
fifeth_text = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
second_button = QPushButton('Начать первый тест')
third_line_edit = QLineEdit('0')
sixth_text = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
third_button = QPushButton('Начать делать пресидания')
seventh_text = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, чёрным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
forth_button = QPushButton('Начать финальный тест')
forth_line_edit = QLineEdit('0')
fifeth_line_edit = QLineEdit('0')
fifeth_button = QPushButton('Отправить результаты')

def timer_test():
    global time
    time = QTime(0, 0, 15)  
    timer = QTimer()
    timer.timeout.connect(timer1Event)
    timer.start(1000)

def timer1Event():
    global time
    time = time.addSecs(-1)
    text_timer = time
    text_timer.setText(time.toString("hh:mm:ss"))
    text_timer.setFont(QFont("Times", 36, QFont.Bold))
    text_timer.setStyleSheet("color: rgb(0,0,0)")
    if time.toString("hh:mm:ss") == "00:00:00":
        timer.stop()    



def experement(third_line_edit,forth_line_edit,fifeth_line_edit,second_line_edit):
    t1 =  third_line_edit.text()
    t2 =  forth_line_edit.text()
    t3 =  fifeth_line_edit.text()
    years = second_line_edit.text()
    return (t1,t2,t3)


def to_3_win():
    main_win2.hide()
    main_win3.show()

    exp = (int(third_line_edit.text()),int(forth_line_edit.text()),int(fifeth_line_edit.text()),int(second_line_edit.text()))

    ind = (4*(int(exp[0])+int(exp[1])+int(exp[2]))-200)/10
    
    if exp[3] == 7 or exp[3]== 8:
        if ind <=6.4:
            uroven = QLabel('Высокий уровень')
        elif ind >=6.4 and ind <=11.9:
            uroven = QLabel('Уровень выше среднего')
        elif ind >=12 and ind<=16.9:
            uroven = QLabel('Средний уровень')
        elif ind >=17 and ind<=20.9:
            uroven = QLabel('Уровень удовлетворительный')
        elif ind >=21:
            uroven = QLabel('Низкий уровень')

    if exp[3] == 9 or exp[3]== 10:
        if ind <=4.9:
            uroven = QLabel('Высокий уровень')
        elif ind >=5 and ind <=10.4:
            uroven = QLabel('Уровень выше среднего')
        elif ind >=10.5 and ind<=15.4:
            uroven = QLabel('Средний уровень')
        elif ind >=15.5 and ind<=19.4:
            uroven = QLabel('Уровень удовлетворительный')
        elif ind >=19.5:
            uroven = QLabel('Низкий уровень')

    if exp[3] == 11 or exp[3]== 12:
        if ind <=3.4:
            uroven = QLabel('Высокий уровень')
        elif ind >=3.5 and ind <=8.9:
            uroven = QLabel('Уровень выше среднего')
        elif ind >=9 and ind<=13.9:
            uroven = QLabel('Средний уровень')
        elif ind >=14 and ind<=17.9:
            uroven = QLabel('Уровень удовлетворительный')
        elif ind >=18:
            uroven = QLabel('Низкий уровень')

    if exp[3] == 13 or exp[3]== 14:
        if ind <=1.9:
            uroven = QLabel('Высокий уровень')
        elif ind >=2 and ind <=7.4:
            uroven = QLabel('Уровень выше среднего')
        elif ind >=7.5 and ind<=12.4:
            uroven = QLabel('Средний уровень')
        elif ind >=12.5 and ind<=16.4:
            uroven = QLabel('Уровень удовлетворительный')
        elif ind >=16.5:
            uroven = QLabel('Низкий уровень')
    if exp[3] >= 15:
        if ind <=0.4:
            uroven = QLabel('Высокий уровень')
        elif ind >=0.5 and ind <=5.9:
            uroven = QLabel('Уровень выше среднего')
        elif ind >=6 and ind<=10.9:
            uroven = QLabel('Средний уровень')
        elif ind >=11 and ind<=14.9:
            uroven = QLabel('Уровень удовлетворительный')
        elif ind >=15:
            uroven = QLabel('Низкий уровень')

    show_ind = QLabel(str(ind))
    vline_on_3_win =QVBoxLayout()

    vline_on_3_win.addWidget(show_ind, alignment = Qt.AlignCenter)
    vline_on_3_win.addWidget(uroven, alignment = Qt.AlignCenter)

    main_win3.setLayout(vline_on_3_win)

vlain1_on_second_win = QVBoxLayout()
hlain1_on_second_win = QHBoxLayout()

vlain1_on_second_win.addWidget(third_text,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(first_line_edit,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(forth_text ,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(second_line_edit,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(fifeth_text,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(second_button,alignment = Qt.AlignLeft)
hlain1_on_second_win.addWidget(third_line_edit,alignment = Qt.AlignLeft)
vlain1_on_second_win.addLayout(hlain1_on_second_win)
vlain1_on_second_win.addWidget(sixth_text,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(third_button ,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(seventh_text,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(forth_button,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(forth_line_edit,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(fifeth_line_edit,alignment = Qt.AlignLeft)
vlain1_on_second_win.addWidget(fifeth_button,alignment = Qt.AlignCenter)
hlain1_on_second_win.addWidget(text_timer,alignment = Qt.AlignRight)
vlain1_on_second_win.addLayout(hlain1_on_second_win)

second_button.clicked.connect(timer_test)
fifeth_button.clicked.connect(to_3_win)

main_win2.setLayout(vlain1_on_second_win)






win.exec_()
