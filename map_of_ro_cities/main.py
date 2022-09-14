import turtle
import pandas

screen = turtle.Screen()
screen.title("Cities of Romania")
image = "cities_of_Romania.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("cities.csv")
all_cities = data.city.to_list()
guessed_cities = []
missing_cities = []


while len(guessed_cities) < 110:
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/110", prompt="Enter city name or exit to end game: ")
    print(answer_city)
    
    if not answer_city:
        break
    
    answer_city = answer_city.title()    
    if answer_city == "Exit":
        for city in all_cities:
            if city not in guessed_cities:
                missing_cities.append(city)

        data_dict = {
            "Cities you missed": missing_cities
        }        
        data = pandas.DataFrame(data_dict)
        data.to_csv("cities_to_learn.csv")
        break 

    if answer_city in all_cities:
        guessed_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city = data[data.city == answer_city]
        t.goto(int(city.x), int(city.y))
        t.write(answer_city)




        
 