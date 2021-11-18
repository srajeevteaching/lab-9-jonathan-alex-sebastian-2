# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: October 18th, 2021
# Lab Number: 9
# Program Inputs: Data file and name of new file which will be created
# Program Outputs: creates file from given data, adding a column for profits of each move, also displays max/min profit

# Assigning index values to a variable
date = 0
title = 1
budget = 2
box_gross = 3
profit = 4


# Creates the list of list from the users file
def load_movie_data(filename):
    data = []
    try:
        movies = open(filename, "r")
        # Tracks line
        line_counter = 0
        for line in movies:
            # Converts each line to a list of its proper type
            try:
                line_counter += 1
                # For every line in the given file it will separate the string into a list using "," as a separator
                line_entries = line.split(",")
                # Converts element of created list into its proper type
                line_entries[date] = line_entries[date].strip()
                line_entries[title] = line_entries[title].strip()
                line_entries[budget] = float(line_entries[budget])
                line_entries[box_gross] = float(line_entries[box_gross])
                # Adds the line made into a list into the list of lists which will contain all the data
                data.append(line_entries)
            # Will run if the line is not of the correct type
            except ValueError:
                print("Value not accepted, line", line_counter, "will be skipped!")
        # Closes the file given by the user
        movies.close()
    # Will run if the file given by the user is not found
    except FileNotFoundError:
        print("File Not Found!")
        exit()
    return data


# Calculates each movies profits and adds it to each movie's list inside the list of movies
def add_profit_column(dataset):
    for i in range(len(dataset)):
        gross_earnings = dataset[i][box_gross]
        movies_budget = dataset[i][budget]
        # Calculates movie's profit by subtracting its earnings from its starting budget
        profits = gross_earnings - movies_budget
        # Adds movie's profit to its list of attributes
        dataset[i].append(profits)
    return dataset


# Finds the movie with the least and greatest amount of profit and prints it for the user
def print_min_and_max_profit(dataset):
    profit_list = []
    # Loops through the list movies, adding a movie's profit into a new list of all profits
    for i in range(len(dataset)):
        profit_list.append(dataset[i][profit])
    # Finds the greatest number of profit using the max function
    max_value = max(profit_list)
    # Finds the lowest number of profit using the min function
    min_value = min(profit_list)
    # Finds the index of the movie with the greatest amount of profit
    max_index = profit_list.index(max_value)
    # Finds the index of the movie with the least amount of profit
    min_index = profit_list.index(min_value)
    print("Highest Profit Movie:", dataset[max_index], "| total profit:", max_value)
    print("Lowest Profit Movie:", dataset[min_index], "| total profit:", min_value)


def save_file(filename, data_list):
    # Opens/Creates a new file with the name given by the user
    with open(filename, "w") as file:
        for line in data_list:
            for element in line:
                # Writes each element in the list and separates it by commas until the list finishes
                file.write(str(element) + ",")
            file.write("\n")


def main():
    # Gets the name of the data file from the user
    file_choice = input("What is the file name: ")
    # Gets the name of the new file the user will create
    created_file_name = input("What would you like to name the second file including movie's profits: ")
    # List of list of all movie data
    movie_list = load_movie_data(file_choice)
    # New list with a new column for profits within each movie's list
    movie_profit_list = add_profit_column(movie_list)
    # Prints the movies with the least and most profit
    print_min_and_max_profit(movie_profit_list)
    # Saves/Creates a new file using the name given by the user and the created list of movies with profits
    save_file(created_file_name, movie_profit_list)


main()
