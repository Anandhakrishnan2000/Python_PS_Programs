
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Executing")


class Myeditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Executing")


class Laptop:

    def code(self,ide):
        ide.execute()

ide = PyCharm()
ide = Myeditor()            #it can be replaced provided the execute method exists in both classes

lap = Laptop()
lap.code(ide)

