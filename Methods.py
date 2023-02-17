import random

# giving the user instructions on how to enter the data
print("Enter tasks in the following format: c1,c2,...\nwhere cx is cost")
print("Type END to finish entering tasks")
# lists for my variables
inputting_data = True
cases = []
count = 1
# inputting the data for users tasks
while inputting_data:
    try:
        cur_task = input(f"Task #{count}:")
        if cur_task.upper() == "END":
            break
        list = cur_task.split(",")
        task_values = []
        if len(list) == 3:
            best_case = int(list[0])
            average_case = int(list[1])
            worst_case = int(list[2])
            cur_list = []
            cur_list.append(best_case)
            cur_list.append(average_case)
            cur_list.append(worst_case)
            cases.append(cur_list)
            count += 1
        else:
            print(
                "Enter the values in the format.\nTask #n: 10,20,40 where 10 is best case,20 is average,40 is worst."
            )
            continue
    except:
        print(
            "Please enter the values in the correct format.\nTask #n: 10,20,40 where 10 is best case,20 is average,40 is worst."
        )
        continue


# values for monte carlo method, this is the list that will be used to find the minimum,maximum and average time
random_task_durations = []
maximum = 0
minimum = 0
# implementation of monte carlo method to get 10000 random durations for the task
for i in range(1, 10001):
    cur_task_duration = 0
    for value in cases:
        random_choice = random.randint(0, len(cases) - 1)
        cur_task_duration += value[random_choice]
    random_task_durations.append(cur_task_duration)
    if i == 1:
        maximum = cur_task_duration
        minimum = cur_task_duration
    if cur_task_duration > maximum:
        maximum = cur_task_duration
    if cur_task_duration < minimum:
        minimum = cur_task_duration

# finding the average task duration
total_duration_values = 0
for value in random_task_durations:
    total_duration_values += value

# the value displayed for the average
average_duration = round(total_duration_values / len(random_task_durations))

# displaying the values for minimum,maximum and average number of days
print(f"\nMinimum = {minimum} days")
print(f"Maximum = {maximum} days")
print(f"Average = {average_duration} days\n")

# probability of finishing the plan in given number of days
print("Probability of finishing the plan in:")
range = maximum - minimum
bin_width = round(range / 10)
i = minimum
j = 0
while j < 11:
    values_in_range = []
    values_in_lower_range = []
    if i == minimum:
        for value in random_task_durations:
            if value <= i:
                values_in_range.append(value)
        probability = round((len(values_in_range) / len(random_task_durations)) * 100)
        print(f"{i} days: {probability}%")
        i += bin_width
        j += 1
        continue
    if i != minimum:
        for value in random_task_durations:
            if value <= i:
                values_in_range.append(value)
        for value in random_task_durations:
            if value <= (i - bin_width):
                values_in_lower_range.append(value)
    probability = (round((len(values_in_range) / len(random_task_durations)) * 100)) - (
        round((len(values_in_lower_range) / len(random_task_durations)) * 100)
    )
    print(f"{i} days: {probability}%")
    i += bin_width
    j += 1

# printing a blank line to separate
print()

# accumulated probability of finishing the task on or before calculation
print("Accumulated probability of finishing the task in or before:")
# calculating the bin width
range = maximum - minimum
bin_width = round(range / 10)
i = minimum
j = 0
while j < 11:
    values_in_range = []
    for value in random_task_durations:
        if value <= i:
            values_in_range.append(value)
    probability = round((len(values_in_range) / len(random_task_durations)) * 100)
    print(f"{i} days: {probability}%")
    i += bin_width
    j += 1
