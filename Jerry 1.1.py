name = input ("What is your name?") # ask what is your name
print ( "Hello" , name) # says hello your name
print ("Hello! My name is Jerry!")
welness = 0 # the variable wellness equals 0
wellness =  int (input ("How are you doing? (respond as a positive number for well and a negetive number for not well do not choose zero)")) # asks if you are doing well


if wellness > 0: # if the variable wellness is greater than zero
    print("Awesome!") # say awsome

    
    favor = int (input ("Do you need any help from me? (reply with a positive number for yes and a negative number for no do not type zero).")) # asks if you want a favor

    
    if favor < 0: # if the favor is less than zero
        print("Bye! More upgrades will come!") # say bye! more upgrades will come

    
    else: #if not
        print("The favor would be a fun shape") # says the favor would be a fun shape
        import turtle # first step on bringing the turtle
        import random
        fred = turtle.Pen()# second step on bringing the turtle
        colorlist = ["red","orange","yellow","green","blue","purple","pink"] # make a list called colorlist
        fred.shape("turtle") # Change the shape of the turtle to a turtle
        fred.speed(0) # sets speed to zero

        for i in range(456): # repeat 456 times
            col=random.choice (colorlist)# pick a random color from color list
            fred.color(col) # change color to col
            fred.left(78) # turns left 78 degrees
            fred.forward(90) # moves forward 90 pixels
        print("Bye! More upgrades will come!")   # says bye! more upgrades will come  
    
else: # if not
    print("Hope you get better!") # says hope you get better
    favor = int (input ("Do you need any help from me? (reply with a positive number for yes and a negative number for no do not type zero).")) # asks if you need a favor

    

    if favor < 0: # if the favor is less than zero
        print("Bye! More upgrades will come!") 

    
