print("Welcome to Arfa Lift")
current_floor=1
while True:
    print("Doors opening")
    floor=int(input("Enter Floor Number [1-17]=="))
    
    if floor > current_floor:
     print("Doors closing--going up")
    if floor < current_floor:
     print("Doors closing--going down")
    elif floor == 1:
     print("Welcome you are on floor 1")
    elif floor == 2:
     print("Welcome you are on floor 2")
    elif floor == 3:
     print("Welcome you are on floor 3")
    elif floor == 4:
      print("Welcome you are on floor 4")
    elif floor == 5:
      print("Welcome you are on floor 5")    
    elif floor == 6:
      print("Welcome you are on floor 6") 
    elif floor == 7:
     print("Welcome you are on floor 7")       
    elif floor == 8:
     print("Welcome you are on floor 8")                     
    elif floor == 9:
     print("Welcome you are on floor 9")           
    elif floor == 10:
     print("Welcome you are on floor 10")           
    elif floor == 11:
     print("Welcome you are on floor 11")           
    elif floor == 12:
     print("Welcome you are on floor 12")       
    elif floor == 13:
     print("Welcome you are on floor 13")       
    elif floor == 14:
     print("Welcome you are on floor 14")       
    elif floor == 15:
     print("Welcome you are on floor 15")       
    elif floor == 16:
     print("Welcome you are on floor 16")       
    elif floor == 17:
     print("Welcome you are on floor 17")   
    elif floor == 0:
     # Marked 0 as emergency button
     print("Stopping Lift--Opening Doors")
     break
    current_floor=floor
    
    

