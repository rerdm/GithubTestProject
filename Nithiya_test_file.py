import os


class TestClass:

    def __init__(self, variable1, variable2):

        #  Konstruktor
        self._var1 = variable1
        self._var2 = variable2
        self.var3 = "köklöklölö"



    def get_var(self):
        return self._var1

    def get_actual_dir(self):

        print(os.listdir())

        for item in os.listdir():

            if item.endswith(".py"):
                print(item)


if __name__ == '__main__':

    x = TestClass(variable1=1, variable2=2)
    print(x.get_var())
    x.get_actual_dir()
