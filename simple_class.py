#!/usr/bin/env python


class Blorch():

    def __init__(self, name):
        self._name = name

    def snork(self):
        print("SNORK SNORK")


    @property  # "getter" property
    def name(self):
        return self._name

    @name.setter # "setter" property
    def name(self, new_name):
        self._name = new_name

    # props + TAB
    @property
    def spam(self):
        return

    @spam.setter
    def spam(self, value):
        pass

#-----------------

b1 = Blorch('Fred')  # Blorch b1 = new Blorch()
b2 = Blorch('Martha')

b1.snork()
b2.snork()

Blorch.snork(b1)

print(b1.name)

b1.name  = 'Chester'


class Car():
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            self._color = new_color
        else:
            raise TypeError("Color must be a string")

c1 = Car("Red")
print(c1.color)

c1.color = 'purple'
print(c1.color)

c1.color = 5.234
