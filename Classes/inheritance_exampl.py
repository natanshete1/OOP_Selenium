

class MyClass1:

    def __init__(self,cls1_input_1):
        print('__init__ of class 1')
        self.prop_cls1 = 10
        self.cli_in_1 = cls1_input_1
        print(self.cli_in_1)

    def method_1_class_1(self):
        print("method_1_class1")

class MyClass2(MyClass1):

    def __init__(self,cl1n1,cl2in1):
        super().__init__(cl1n1)
        print('__init__ of class 2')
        self.prop_cls1 = cl2in1

    def method_1_class_2(self):
        print('method_1_class_2')

# obj1 = MyClass1()
# obj1.method_1_class_1()

obj2 = MyClass2('abc' ,'xyz')
obj2.method_1_class_2()
obj2.method_1_class_1()
print(obj2.cli_in_1)

