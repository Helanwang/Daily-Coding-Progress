
import numpy as np


def set1():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    sum_data = np.sum(data)
    print(sum_data)

    max_value = np.max(data)
    print(max_value)

    min_value = np.min(data)
    print(min_value)

    mean_value = np.mean(data)
    print(mean_value)


def set2():
    data2 = np.array([1000, 7500, 8500, 3000, 4000, 5000, 6000])
    data_sum = np.sum(data2)
    print(data_sum)

    data2_max = np.max(data2)
    print(data2_max)

    data2_mean = np.mean(data2)
    print(data2_mean)

    above_average_days = np.sum(data2 > data2_mean)
    print(above_average_days)


def set3():
    data3 = np.array([22.1, 19.5, 25.3, 18.0, 21.4, 23.5, 20.0])
    average_temperature = np.mean(data3)
    print(average_temperature)

    highest_temperature = np.max(data3)
    print(highest_temperature)

    lowest_temperature = np.min(data3)
    print(lowest_temperature)

    above_average_days = np.sum(data3 > highest_temperature)
    print(above_average_days)

    below_average_temperature = np.sum(data3 < lowest_temperature)
    print(below_average_temperature)

    differences_temperature = highest_temperature - lowest_temperature
    print(differences_temperature)


set3()
