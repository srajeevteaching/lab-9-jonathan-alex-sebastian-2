# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: October 18th, 2021
# Lab Number: 9
# Program Inputs:
# Program Outputs:

date = 0
title = 1
budget = 2
box_gross = 3
profit = 4


def load_movie_data(filename):
    data = []
    try:
        movies = open(filename, "r")
        line_counter = 0
        for line in movies:
            try:
                line_counter += 1
                line_entries = line.split(",")

                line_entries[date] = line_entries[date].strip()
                line_entries[title] = line_entries[title].strip()
                line_entries[budget] = float(line_entries[budget])
                line_entries[box_gross] = float(line_entries[box_gross])

                data.append(line_entries)
            except ValueError:
                print("Value not accepted, line", line_counter, "will be skipped!")
        movies.close()
    except FileNotFoundError:
        print("File Not Found!")
    return data


def add_profit_column(dataset):
    for i in range(len(dataset)):
        gross_earnings = dataset[i][box_gross]
        movies_budget = dataset[i][budget]
        profit = gross_earnings - movies_budget
        dataset[i].append(profit)
    return dataset


def print_min_and_max_profit(dataset):
    max_profit = 0
    min_profit = 0
    max_profit_index = 0
    min_profit_index = 0
    for i in range(len(dataset)):
        if dataset[i][profit] > max_profit:
            max_profit = dataset[i][profit]
            max_profit_index = i
        elif dataset[i][profit] < min_profit:
            min_profit = dataset[i][profit]
            min_profit_index = i

    return max_profit_index, min_profit_index


movie_list = load_movie_data("movies.csv")
new_list = add_profit_column(movie_list)
indexes = print_min_and_max_profit(new_list)
print(new_list)
print("\n")
print(indexes)
print(new_list[29])
print(new_list[4])
