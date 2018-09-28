import random
from PIL import Image, ImageDraw

"""
Доступные режимы (Mode:):
0 - оттенки серого(усредняем каждый пиксель).
1 - сепия (depth = 30);
Чтобы получить сепию, нужно посчитать среднее значение и взять какой — нибудь коэффициент. 
middle = (R + G + B) / 3
Первое значение пиксела ( R ) = middle + 2 * k
Второе значение пиксела ( G ) = middle + k
Третье значение пиксела ( B ) = middle
2 - нигатив (каждое значение пиксела вычесть из 255).
3 - добавление шумов, factor = 70 (добавляем к пикселу какое — нибудь рандомное значение. Чем больше разброс этих 
значений, тем больше шумов).
4 - яркость factor = 100, factor = -100 (Для регулирования яркости к каждому пикселу добавляем определенное значение. 
Если оно > 0, то картинка становится ярче, иначе темнее).
5 - черно - белое изображение, factor = 100 (Все пикселы надо разбить на 2 группы: черные и белые. Для проверки 
принадлежности к определенной группе смотрим к чему ближе значение пиксела: к белому цвету или к чёрному).
"""
mode = int(input('Mode: '))  # Выбираем режим
image = Image.open("tmp.jpg")  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаём инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

if mode == 0:
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))

if mode == 1:
    depth = int(input('depth: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

if mode == 2:
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))

if mode == 3:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

if mode == 4:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

if mode == 5:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))

image.save('output.jpg', 'JPEG')  # Сохраняем результат
del draw  # Удаляем кисть
