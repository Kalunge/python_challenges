# Create a function that finds the maximum range of a triangles third edge
# maximum range of third edge = (side1 + side2) - 1 .

def next_edge(side1, side2):
    third = (side1 + side2) - 1
    return third

print(next_edge(8, 10))

print(next_edge(5, 7)) #➞ 11

print(next_edge(9, 2)) #➞ 10



# Create a function that takes a list and returns the first element.

def get_first_value(list):
    return list[0]

print(get_first_value([1, 2, 3])) #➞ 1

print(get_first_value([80, 5, 100])) #➞ 80

print(get_first_value([-500, 0, 50])) #➞ -500



# e)You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. 
# Return the total number of legs on your farm. (CREATE A FUNCTION)

# example:

def animals(chickens, cows, pigs):
    legs = (chickens * 2) + (cows * 4) + (pigs * 4)
    return legs

print(animals(2, 3, 5)) #➞ 36

print(animals(1, 2, 3)) #➞ 22

print(animals(5, 2, 8)) #➞ 50


# f)Create a function that takes a list of numbers. Return the largest number in the list.

# example:

def findLargestNum(list):
    return max(list)


print(findLargestNum([4, 5, 1, 3])) #➞ 5

print(findLargestNum([300, 200, 600, 150])) #➞ 600

print(findLargestNum([1000, 1001, 857, 1])) #➞ 1001


# g)Given a list of integers, return the difference between the largest and smallest integers in the list.

# example:

# 15 - (-9) = 24

def difference(list):
    return (max(list)) - (min(list))

print(difference([10, 15, 20, 2, 10, 6])) #➞ 18
print(difference([-3, 4, -9, -1, -2, 15])) #➞ 24


# h) Create a function to concatenate two integer lists.

def concat(list1, list2):
    list3 = list1 + list2
    return list3

# example:

print(concat([1, 3, 5], [2, 6, 8])) #➞ [1, 3, 5, 2, 6, 8]

print(concat([7, 8], [10, 9, 1, 1, 2])) #➞ [7, 8, 10, 9, 1, 1, 2]

print(concat([4, 5, 1], [3, 3, 3, 3, 3])) # ➞ [4, 5, 1, 3, 3, 3, 3, 3]


# i)Create a function that takes two strings as arguments and return either True or False depending on 
# whether the total number of characters in the first string is equal to the total number of characters in the second string.

# example:

def comp(str1, str2):
    if len(str1) == len(str2):
        return True
    else:
        return False


print(comp("AB", "CD")) #➞ True

print(comp("ABC", "DE")) #➞ False

print(comp("hello", "edabit")) #➞ False



# j)Write a function that converts a dictionary into a list, where each element represents a key-value pair.

# example:

def convert_to_array(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append([key, value])
    return dict_list

print(convert_to_array({ "a": 1, "b": 2 })) #➞ [["a", 1], ["b", 2]]

print(convert_to_array({ "shrimp": 15, "tots": 12 })) #➞ [["shrimp", 15], ["tots", 12]]

print(convert_to_array({})) #➞ []


# k)You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting 
# inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.

# example:

def profit(dict):
    profit = (dict['sell_price'] - dict['cost_price']) * dict['inventory']
    return round(profit)

print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
})) #➞ 14796

print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
})) #➞ 32411


print(profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
})) #➞ 44030

# Abigail and Benson are playing Rock, Paper, Scissors.

# Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played.

# Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

# R stands for Rock
# P stands for Paper
# S stands for Scissors

def calculate_score(list):
    counter = []
    for item in list:
        if item[0] == item[1]:
            counter.append('T')
        if item[0] == 'R' :
            if item[1] == 'P':
                counter.append('B')
            elif item[1] == 'S':
                counter.append('A')

        if item[0] == 'P':
            if item[1] == 'S':
                counter.append('B')
            elif item[1] == 'R':
                counter.append('A')
        
        if item[0] == 'S':
            if item[1] == 'R':
                counter.append('B')
            elif item[1] == 'P':
                counter.append('A')

    abigail = counter.count('A')
    benson = counter.count('B')
    tie = counter.count('T')

    if abigail > benson and abigail > tie:
        return 'Abigail'
    elif benson > abigail and benson > tie:
        return 'Benson'
    else:
        return 'Tie'

    # return counter

mylist = [["R", "P"], ["R", "S"], ["S", "P"]]

result = calculate_score(mylist)

result2 = calculate_score([["R", "S"], ["S", "S"]]) #➞ "Tie"

result3 = calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) #➞ "Tie"



print(result)
print(result2)
print(result3)



# result = counter.count()




# calculate_score(mylist)






























































































# calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"

# Ben wins the first game (Paper beats Rock).
# Abigail wins the second game (Rock beats Scissors).
# Abigail wins the third game (Scissors beats Paper). 
# Abigail wins 2/3.

# calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"

# calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"