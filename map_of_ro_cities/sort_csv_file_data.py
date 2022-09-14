import csv


# Reads data from a .csv file, for loop is used to iterate through all items of the csv object and append them into a list so we'll have a big list, a list with elements lists.
with open("state.csv") as file:
    reader = csv.reader(file)
    city_list = []
    for row in reader:
        city_list.append(row)

# Here we first sort the list and then overwrite the original file with the modified list elements.
sorted_city_names = sorted(city_list)
with open("cities.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sorted_city_names)
               