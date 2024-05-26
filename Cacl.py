import tkinter as tk

# Функція для обробки натискань кнопок
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Функція для обчислення результату
def button_equal():
    global expression
    result = str(eval(expression)) # eval функція для обчислення виразу
    input_text.set(result)
    expression = ""

# Функція для очищення дисплею
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Головне вікно
window = tk.Tk()
window.title("Калькулятор")

# Глобальна змінна для збереження виразу
expression = ""

# Текстове поле для введення/виведення
input_text = tk.StringVar()

input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Кадр для кнопок
btns_frame = tk.Frame(window)
btns_frame.pack()

# Розташування кнопок у сітці
button_texts = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Створення кнопок і їх розташування
for row in range(4):
    for col in range(4):
        btn_text = button_texts[row][col]
        if btn_text == '=':
            btn = tk.Button(btns_frame, text=btn_text, fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=button_equal)
        elif btn_text == 'C':
            btn = tk.Button(btns_frame, text=btn_text, fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=button_clear)
        else:
            btn = tk.Button(btns_frame, text=btn_text, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda x=btn_text: button_click(x))
        
        btn.grid(row=row, column=col, padx=1, pady=1)

# Кнопка очищення (додаємо її окремо, щоб вона була у відповідному місці)
clear_button = tk.Button(btns_frame, text='C', fg='black', width=22, height=3, bd=0, bg='#eee', cursor='hand2', command=button_clear)
clear_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

window.mainloop()
