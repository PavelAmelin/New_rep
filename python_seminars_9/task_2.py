# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

class MetaType(type):
    MyClass = None

    def __call__(cls):
        if cls.MyClass is None:
            new_obj = super.__call__()
            MyClass = new_obj
        return cls.MyClass

class MyClass(metaclass=MetaType):

    def method_1(self):
        pass

obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)
