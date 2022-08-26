class Fraction:
    i = 0
    def __init__(self,numerator,denominator,numerator2,denominator2):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__numerator2 = numerator2
        self.__denominator2 = denominator2
        self.i+=1
    @staticmethod
    def count(con):
        return con.i
    def set_num(self,numerator):
        self.__numerator = numerator

    def set_den(self,denominator):
        self.__denominator = denominator

    def set_num2(self,numerator2):
        self.__numerator2 = numerator2

    def set_den2(self,denominator2):
        self.__denominator2 = denominator2



    user = input("Выбирите операцию (+,-,/,*) :",)
    if user == "+":
        def get_sum(self):
            return (self.__numerator/self.__denominator) + (self.__numerator2/self.__denominator2)
    elif user == "-":
        def get_sum(self):
            return (self.__numerator/self.__denominator) - (self.__numerator2/self.__denominator2)
    elif user == "/":
        def get_sum(self):
            return (self.__numerator / self.__denominator) / (self.__numerator2 / self.__denominator2)
    elif user == "*":
        def get_sum(self):
            return (self.__numerator/self.__denominator) * (self.__numerator2/self.__denominator2)

frac = Fraction(1,2,3,2)
frac.set_num(15)
frac.set_den(30)
frac.set_num2(44)
frac.set_den2(66)
print(frac.get_sum())
print(frac.count(frac))
#================================================================================
class Temperature_conversion:
    cn = 0
    def __init__(self,celsius,fahrenheit,count):
        self.__celsius = celsius
        self.__fahrenheit = fahrenheit
        self.__count = count
    @staticmethod
    def Celsius_to_fahrenheit(temp):
        temp.__count+=1
        return f"температура из Цельсия в Фаренгейт = {temp.__celsius * 1.8 + 32}`F"
    @staticmethod
    def Fahrenheit_to_celsius(temp):
        temp.__count+=1
        return f"температура из Фаренгейт в Цельсия = {(temp.__fahrenheit - 32) / 1.8}`C"
    @staticmethod
    def count(con):
        return con.__count

temp = Temperature_conversion(10,50,0)
print(temp.Celsius_to_fahrenheit(temp))
print(temp.Fahrenheit_to_celsius(temp))
print(temp.count(temp))
#===================================================================
class Metric_system:
    def __init__(self,num):
        self.__num = num
    @staticmethod
    def eng_to_metric(eng):
        return f"{eng.__num} дюйм = {eng.__num * 25.4} мм\n" \
               f"{eng.__num} фут = {eng.__num * 304.8} мм\n" \
               f"{eng.__num} ярд = {eng.__num * 91.44} см\n" \
               f"{eng.__num} миля = {eng.__num * 1609} м\n" \
               f"{eng.__num} морская миля = {eng.__num * 1853.2} м\n" \
               f"{eng.__num} кабельтов =  {eng.__num * 185.32} м\n"
    @staticmethod
    def metric_to_eng(met):
        return f"{met.__num} км = {met.__num * 3280.840} футов\n" \
               f"{met.__num} м = {met.__num * 3280.840} футов\n" \
               f"{met.__num} см = {met.__num * 0.033} футов"
value = Metric_system(6)
print(value.eng_to_metric(value))
print(value.metric_to_eng(value))