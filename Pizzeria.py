#базовый класс
class Title():
    def __init__(self, title = ''):
        self.__title = title
#ограничиваем создание произвольных атрибутов        
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title
        


class Product(Title):
    def __init__(self, title, calorific = 1, cost = 1):
        Title.__init__(self, title)
#Проверяем не является ли цена, или каллорийность отрицательным числом        
        if (cost or calorific) <= 0:
            raise ValueError
        self.__calorific = calorific
        self.__cost = cost
#ограничиваем создание произвольных атрибутов  
    
    @property
    def calorific(self):
        return self.__calorific

    @calorific.setter
    def calorific(self, calorific):
        if calorific <= 0:
            raise ValueError
        self.__calorific = calorific

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if cost <= 0:
            raise ValueError
        self.__cost = cost
        
       

        
class Ingredient:
    def __init__(self, product = [], weight = 1):
        self.__product = product
#Проверяем не является ли вес, отрицательным числом
        if weight <= 0:
            raise ValueError
        self.__weight = weight
#ограничиваем создание произвольных атрибутов  
    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product):
        self.__product = product

    @property
    def  weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if  weight <= 0:
            raise ValueError
        self.__weight =  weight

#Находим общее количество каллорий всех продуктов    
    @property
    def сalories(self):
        сalories = 0      
        for element in self.product:
            сalories +=  element.calorific 
        return (self.weight / 100) *  сalories

#Находим общую стоймость всех продуктов
    @property
    def cost(self):
        money = 0
        for element in self.product:
            money += element.cost
        return (self.weight / 100) * money



class Pizza(Title):
    def __init__(self, title, ingredients = []):
        Title.__init__(self, title)
        self.__ingredients = ingredients

#ограничиваем создание произвольных атрибутов  
    @property
    def ingredients(self):
        return self.__ingredients
    @ingredients.setter
    def ingredients(self, ingredients):
        self.__ingredients = ingredients    

#Получаем каллорийность пиццы 
    @property   
    def сalories(self):
        сalories = 0
        for element in self.ingredients:
            сalories += element.сalories
        return float(сalories)
#Получаем стоимость пиццы
    @property  
    def сost(self):
        money = 0
        for self.element in self.ingredients:
            money = money + self.element.cost
        return float(money)
    
    def __str__(self):
        return f'{self.title} ({self.сalories} kkal) - {self.сost} руб'


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
#список продуктов
dough_product = Product('Тесто', 200, 20)
water_product = Product('Вода', 5, 20)
salt_product = Product('Соль', 20, 10)

potatoes_product = Product('Картофель', 120, 30)
tomato_product = Product('Помидоры', 100, 50)
eggplant_product = Product('Баклажаны', 110, 40)

cheese_product = Product('Сыр', 100, 120)
mushrooms_product = Product('Грибы', 150, 40)
pepper_product = Product('Перец', 100, 10)

meat_product = Product('Мясо', 300, 100)
ham_product = Product('Ветчина', 250, 100)
sausage_product = Product('Колбаса', 200, 50)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
foundation_ingredient = Ingredient([dough_product, water_product, salt_product], 150)
meat_ingredient = Ingredient([meat_product, ham_product, sausage_product], 200)
vegetables_ingredient = Ingredient([potatoes_product, tomato_product, eggplant_product], 200)
additives_ingredient = Ingredient([cheese_product, mushrooms_product, pepper_product], 180)


# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [meat_ingredient, foundation_ingredient, vegetables_ingredient, additives_ingredient])


print(pizza_margarita)