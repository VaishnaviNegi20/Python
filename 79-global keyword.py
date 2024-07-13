# a = 10 #global 
# def display():
#     print(a)
# display()


# a = 10 #global 
# def display():
#     a=15 #local
#     print(a) #first it'll check for local scope, if not found then global scope
# display()


# def display():
#     a=15
# display()
# print(a)  #a is a local variable that's why we are having error


# a= 10  #global
# def display():
#     a=a+1 # can't modify the global variable within a function, you can only access it within a function also
#     print(a)
# display()


#but if you have to modify global var within a function then use global keyword
# a= 10  #global
# def display():
#     global a 
#     a=a+1 
#     print(a)
# display()


# def display():
#     a=20
#     def show():
#         global a 
#         a=a+1  #it'll give error here 
#         print(a)
#     show() #because we are heving a global a var then show() will search for the variable outside of the scope of display() since show() is within the scope of display() 
# display()


# def display():
#     a=20
#     def show():
#         global a 
#         a=30 
#     print("before", a)   
#     show()
#     print("after",a)
# display()


# def display():
#     a=20
#     def show():
#         global a 
#         a=30 
#     print("before", a)   
#     show()
# print("after",a)
# display()


# def display():
#     a=20
#     def show():
#         global a 
#         a=30 
#     print("before", a)   
#     show()
# print("after",a)  #taking global a define within the function 
# display()
# print(a) #taking global a define within the function 


# a=44
# def display():
#     a=20
#     def show():
#         global a 
#         a=30 
#     print("before", a)   
#     show()
# print("after",a)  #taking global a which is define within the function 
# display() 
# print(a)  #beacause we are calling the display so it is changing the value of global a from 44 to 30


# a=44
# def display():
#     a=20
#     def show():
#         global a 
#         a=30 
#     print("before", a)   
#     show()
# print("after",a)  
# print(a) #beacause we are not calling the display so it is changing the value of global a is 44 only


# a=44
# def display():
#     a=20
#     def show():
#         a=30 
#     print("before", a)   
#     show()
# print("after",a)   
# display()
# print(a) 




