# 类定义 关键字class 类名首字母大写，(object)表示继承，括号里面表示父类
class Student(object):

    #绑定强制属性，第一个参数永远是self,表示创建实例，有了__init__方法，
    # 创建实例的时候就不能使用空参数了
    # 变量名前加上“__”表示类的私有变量
    def __init__(self,name,score):
        self.__name = name
        self.__score = score


    def print_score(self):
        print('%s : %s' %(self.__name,self.__score))


student = Student('Lili',80)
student.print_score()
