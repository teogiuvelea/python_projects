import turtle 
import csv



screen = turtle.Screen()
screen.title("Romania Cities Game")
image = "map_of_Romania.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_on_click_coord(x, y):
    city = input("City: ").title()
    print(x, y)
    record = [city, x, y]
    with open("cities.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)
    


turtle.onscreenclick(get_mouse_on_click_coord)  
turtle.mainloop()