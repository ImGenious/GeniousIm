from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QMessageBox, QRadioButton, QWidget, QGroupBox, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup
from random import randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_l = []
q1 = Question('Сколько хромосом у человека?', '46', '42', '23', '48')
q2 = Question('Сколько лет Егору?', '16', '15', '17', '18')
q3 = Question('Сможет ли Егор заданчить?', 'Да, через 100 лет', 'Нет', 'Да', 'Никогда')
q4 = Question('Сколько Ваня забьет против дюшки?', '0', '15', '27', '31')
q5 = Question('Сколько iq у Егора?', '15', '120', '200', '135')
q6 = Question('Кто будет официантом на день семейного отдыха?', 'Дима', 'Егор', 'Лера', 'Ваня')
q7 = Question('Кто самый харизматичный в мире?', 'Егор', 'Лера', 'Никто', 'Ваня')
question_l.append(q1)
question_l.append(q2)
question_l.append(q3)
question_l.append(q4)
question_l.append(q5)
question_l.append(q6)
question_l.append(q7)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo Card')

main_win.move(900, 70)
main_win.resize(400, 200)

btn_OK = QPushButton('Ответить')
#lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question = QLabel('Сколько хромосом у человека?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('42')
rbtn_2 = QRadioButton('23')
rbtn_3 = QRadioButton('46')
rbtn_4 = QRadioButton('48')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов:', main_win.score)
            print('Рейтинг:', (main_win.score/main_win.total*100), '%')

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов:', main_win.score)
    cur_question = randint(0, len(question_l)-1)
    q = question_l[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win = QWidget()
main_win.setLayout(layout_card)
main_win.setWindowTitle('Memo Card')
main_win.cur_question = 0
btn_OK.clicked.connect(click_ok)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec_()




