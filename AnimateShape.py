from graphics import *


def draw_my_shape(x, y, win):
    rectangle1 = Rectangle(Point(x, y), Point(x + 100, y + 100))
    rectangle1.setFill('blue4')
    rectangle1.setOutline('white')
    circle1 = Circle(Point(x + 50, y + 75), 24)
    circle1.setFill("blue")
    circle1.setOutline('white')
    triangle1 = Polygon(Point(x, y), Point(x + 100, y), Point(x + 50, y + 50))
    triangle1.setFill('yellow3')
    triangle1.setOutline('white')
    rectangle1.draw(win)
    triangle1.draw(win)
    circle1.draw(win)


def main():
    win = GraphWin("Window", 400, 400, autoflush=False)
    win.setBackground('red4')
    while True:
        win.clear_win()
        mouse_point = win.getMousePosition()
        draw_my_shape(mouse_point.x, mouse_point.y, win)
        win.update()


if __name__ == '__main__':
    main()
