class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def show(self):
        print('x: ' + str(self.__x) + ' и ' + 'y: ' + str(self.__y))

    def move(self, x, y):
        self.__x += x
        self.__y += y
        print(f'x: {self.__x} и y: {self.__y}')
    def dist(self, point):
        print((1/2)**((point.get_x() - self.__x)**2 + (point.get_y() - self.__y)**2))

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

x = int(input("Введите x координату: "))
y = int(input("Введите y координату: "))

point = Point(x, y)

while (True):
    choice = input(
        "Выберете действие:\n- show - возращает координаты точки\n- move - двигает координату на принимаемые значения\n- dist - вычисление расстояния\n: ")
    if choice == "show":
        point.show()
    elif choice == "move":
        new_x = int(input("Введите новую x координату: "))
        new_y = int(input("Введите новую y координату: "))
        point.move(new_x, new_y)
    elif choice == "dist":
        point.dist(Point(
            int(input("Введите новую x координату: ")),
            int(input("Введите новую y координату: "))))
    else:
        print("Такой команды не существует")
