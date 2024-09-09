#Create a Dictionary called Fruits
fruits = {
    "apple":"red",
    "banana":"yellow",
    "orange":"orange"
}
#Access Banana Key and store it in variable called banana_color
banana_color = fruits ["banana"]
# Change the color of the apple to green
fruits["apple"] = "green"
#Delete Orange
del fruits["orange"]
print (fruits.keys())