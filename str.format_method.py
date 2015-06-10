'''Example of basic Format method'''


# {} is the placeholder for the substituted variables.

variable_1 = "Hi This is {}".format("String Format Method")
print(variable_1)
# o/p: Hi This is String Format Method



variable_2 = " {} Method belongs to {}".format("format()","String class")
print(variable_2)
# o/p: format() Method belongs to String class



# You can use the numeric position of the variables

variable_3 = " {0} is better than {1} ".format("Python 3.3","Python 2.7")
print(variable_3)
# o/p: Python 3.3 is better than Python 2.7 



# Named Arguments

obj = " Good Morning {name}. you had taken your {food} ? ".format(name = "John", food = "Breakfast")
print(obj)
# o/p:  Good Morning John. you had taken your Breakfast ?



# Reuse Same Variable Multiple Times

str = " Oh {0} {0}!!! what is this {1}".format("god","Ramesh")
print(str)
# o/p: Oh god god!!! what is this Ramesh
