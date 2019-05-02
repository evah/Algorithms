
"""
从它们的使用上来看,

    @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
    @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。

而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
---------------------
作者：mattkang
来源：CSDN
原文：https://blog.csdn.net/handsomekang/article/details/9615239
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

class A(object):
    bar = 1

    def foo(self):
        print
        'foo'

    @staticmethod
    def static_foo():
        print
        'static_foo'
        print
        A.bar

    @classmethod
    def class_foo(cls):
        print
        'class_foo'
        print
        cls.bar
        cls().foo()


A.static_foo()
A.class_foo()
