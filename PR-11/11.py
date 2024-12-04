import tkinter as tk
from tkinter import messagebox, filedialog, ttk


# Функция для калькулятора
def calculate():
    try:
        num1 = float(entry1.get()) # получает значение из первого поля ввода (entry1), преобразует в число с плавающей точкой
        num2 = float(entry2.get()) # получает значение из второго поля ввода (entry2), преобразует в число с плавающей точкой
        operation = operation_var.get() # получает выбранную операцию из выпадающего списка
        if operation == '+': # если выбрано +
            result = num1 + num2 # переменная result вычисляет сумму
        elif operation == '-': # если выбрано -
            result = num1 - num2 # переменная result вычисляет разность
        elif operation == '*': # если выбрано *
            result = num1 * num2 # переменная result вычисляет произведение
        elif operation == '/': # если выбрано /
            if num2 != 0: # проверяет деление на ноль
                result = num1 / num2 # вычисляет частное
            else:
                result = "Ошибка: деление на ноль" # иначе будет выдаваться ошибка
        else:
            result = "Выберите операцию"

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")


# Функция для чекбоксов
def show_selection():
    selected_options = [] # создает пустой список для хранения выбранных опций
    if var1.get(): # проверяет выбран ли первый чекбокс
        selected_options.append("Первый вариант") # если первый вариант выбран, добавляет его в список
    if var2.get(): # проверяет выбран ли второй чекбокс
        selected_options.append("Второй вариант") # если первый вариант выбран, добавляет его в список
    if var3.get(): # проверяет выбран ли третий чекбокс
        selected_options.append("Третий вариант") # если третий вариант выбран, добавляет его в список

    if selected_options: # проверяет есть ли выбраные опции
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected_options)}") # отображает что выбрали
    else:
        messagebox.showinfo("Выбор", "Ничего не выбрано") # иначе, выдает ошибку что ничего не выбрано


# Функция для загрузки текста из файла
def load_text():
    file_path = filedialog.askopenfilename() # Открывает окно для выбора файла
    if file_path: # выбран ли файл
        with open(file_path, 'r', encoding='utf-8') as file: # Oткрывает выбранный файл для чтения с кодировкой UTF-8
            text = file.read() # читаем содержимое файла
            text_area.delete(1.0, tk.END)  # Очищаем текстовое поле
            text_area.insert(tk.END, text)  # Вставляем текст из файла


# главное окно
root = tk.Tk() # создаем главное окно
root.title("Лобанов Александр Андреевич")  # Название приложения
root.geometry("600x600")  # Размер окна
root.resizable(width=False, height=False)


# Создаем вкладки
tab_control = ttk.Notebook(root) # Создает вкладки

# Первая вкладка - Калькулятор
tab1 = ttk.Frame(tab_control) # фрейм для первой вкладки
tab_control.add(tab1, text='Калькулятор') # добавляет первую вкладку в Notebook

label1 = tk.Label(tab1, text="Первое число:")
label1.pack(pady=5)
entry1 = tk.Entry(tab1)
entry1.pack(pady=5)

label2 = tk.Label(tab1, text="Второе число:")
label2.pack(pady=5)
entry2 = tk.Entry(tab1)
entry2.pack(pady=5)

operation_var = tk.StringVar(value='+')
operation_menu = ttk.Combobox(tab1, textvariable=operation_var, values=['+', '-', '*', '/'])
operation_menu.pack(pady=5)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(tab1, text="Результат:")
result_label.pack(pady=5)

# Вторая вкладка - Чекбоксы
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(anchor=tk.W, padx=10)

checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(anchor=tk.W, padx=10)

checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(anchor=tk.W, padx=10)

selection_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
selection_button.pack(pady=10)

# Третья вкладка - Работа с текстом
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Работа с текстом')

load_button = tk.Button(tab3, text="Загрузить текст из файла", command=load_text) # создает кнопку
load_button.pack(pady=10) # размещаем кнопку

text_area = tk.Text(tab3, wrap=tk.WORD, width=40, height=10) #
text_area.pack(pady=10)

# Упаковываем вкладки
tab_control.pack(expand=1, fill='both') # размещает вкладки в главном окне

# Запускаем главный цикл приложения
root.mainloop()