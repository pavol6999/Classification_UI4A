import time
import Gui
import math
from random import random, randrange, gauss






def classify(point, training_points, k):
    distances = []

    for classes, positions in training_points.items():
        for position in positions:
            distance = math.sqrt((position[0] - point[0]) ** 2 + (position[1] - point[1]) ** 2)
            distances.append((distance, classes))
    freq_dict = {'R': 0,
                 'G': 0,
                 'B': 0,
                 'P': 0}

    sorted_distances = sorted(distances)[:k]
    for i in range(k):
        freq_dict[sorted_distances[i][1]] += 1

    return max(freq_dict, key=freq_dict.get)



    # canvas.mainloop()


def random_point(function, c):
    borders = {'R':(-5000, 500, -5000, 500), 'G':(-500, 5000, -5000, 500), 'B':(-5000, 500, -500, 5000), 'P':(-500, 5000, -500, 5000)}

    if random() < 0.99:
        if function == 'gauss':
            return round(gauss((borders[c][0] + borders[c][1]) // 2, 1000)), round(gauss((borders[c][2] + borders[c][3]) // 2, 1000))
        elif function == 'default':
            return randrange(borders[c][0], borders[c][1]), randrange(borders[c][2], borders[c][3])
    else:
        point = randrange(-5000, 5000), randrange(-5000, 5000)
        while borders[c][0] < point[0] < borders[c][1] and borders[c][2] < point[1] < borders [c][3]:
            point = (randrange(0, 10000), randrange(0, 10000))
        return point

def generate_points(distribution,num_points):
    all_points = []
    colors = ('R', 'G', 'B', 'P')

    for i in range(num_points):

        while True:
            point = random_point(distribution, colors[i%4])
            if point in all_points:
                continue
            else:
                all_points.append(point)
                break
    print(f"{i}")
    return all_points


def menu():
    distribution = input("Rozdelenie ( default - gauss ): ")
    num_points = int(input("Pocet bodov: "))
    k = int(input("K: "))
    add_dataset = input("Pridat body do datasetu ( y - n ): ")
    if add_dataset == 'y':
        add_dataset = True
    else:
        add_dataset = False

    return distribution,num_points, k, add_dataset

def test(distribution,points, k, add_dataset, test_name):

    # classified_points = {'R': [],
    #                      'G': [],
    #                      'B': [],
    #                      'P': []}
    classified_points = []

    default_points = {
        'R': [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
        'G': [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
        'B': [(-4500, 4400), (-4100, 3000), (-1800, +2400), (-2500, +3400), (-2000, +1400)],
        'P': [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
    }

    num_err = 0
    canvas = Gui.GUI(800, test_name)

    time0 = time.time()



    all = []
    for i in range(len(points)):

        color = classify(points[i], default_points,k)
        if color != list(default_points.keys())[i % 4]:
            num_err += 1
        if add_dataset:
            default_points[color].append(points[i])
            classified_points.append((points[i], color))
        else:

            classified_points.append((points[i],color))

    time1=time.time()
    print("Num of errors: ", num_err)
    print(f"Test ran for {(time1-time0)/60} minutes")

    if distribution == 'gauss':
        canvas.draw_points(classified_points,False,distribution)
    else:
        animate = input("Animate result ( y - n ): ")
        if animate == 'y':
            canvas.draw_points(classified_points,True,distribution)
        else:
            canvas.draw_points(classified_points,False,distribution)


def main():


    controller = 0
    while controller != 3:
        controller = int(input("1. Vlastny test\n2. Testy zo zadania\nVyber: "))
        if controller == 1:
            distribution, num_points, k, add_dataset = menu()
            points=generate_points(distribution,num_points)
            test(distribution, points, k, add_dataset,"Vlastny test")
        if controller == 2:
                points=generate_points('default',5000)
                print("Spustam prvy test na 5000 bodov pre K - 1")
                test('default', points, 1, True, "Test 1")

                print("Spustam prvy test na 5000 bodov pre K - 3")
                test('default', points, 3, True, "Test 2")

                print("Spustam prvy test na 5000 bodov pre K - 7")
                test('default', points, 7, True, "Test 3")

                print("Spustam prvy test na 5000 bodov pre K - 15")
                test('default', points, 15, True, "Test 4")





main()
