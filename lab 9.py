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
        profits = gross_earnings - movies_budget
        dataset[i].append(profits)
    return dataset


def print_min_and_max_profit(dataset):
    profit_list = []
    for i in range(len(dataset)):
        profit_list.append(dataset[i][profit])
    max_value = max(profit_list)
    min_value = min(profit_list)
    max_index = profit_list.index(max_value)
    min_index = profit_list.index(min_value)
    print("Highest Profit Movie:", dataset[max_index], "| total profit:", max_value)
    print("Lowest Profit Movie:", dataset[min_index], "| total profit:", min_value)


def save_file(filename):
    with open(filename, "w") as file:
        for line in file:
            for element in line:
                file.write(str(element) + ",")
            file.write("\n")


def main():
    movie_list = load_movie_data("movies.csv")
    movie_list_with_profits = add_profit_column(movie_list)
    print_min_and_max_profit(movie_list_with_profits)


main()
