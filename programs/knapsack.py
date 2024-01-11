#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reincarnate(d, weights, cell):
    solution = []
    w = W
    item = len(weights)

    for i in range(len(weights) - 1, -1, -1):
        current_weight = weights[i]
        if d[w][item] == d[w - current_weight][item - 1] + cell[i]:
            solution.append(1)
            w -= current_weight
        else:
            solution.append(0)
        item -= 1

    solution.reverse()
    return solution


def knapSackWithoutRepetitions(weights, cell):
    d = [[0] * (len(weights) + 1) for _ in range(W + 1)]

    for i in range(len(weights) + 1):
        d[0][i] = 0

    for weight in range(W + 1):
        d[weight][0] = 0

    for item in range(1, len(weights) + 1):
        for weight in range(1, W + 1):
            d[weight][item] = d[weight][item - 1]
            cur_weight = weights[item - 1]

            if cur_weight <= weight:
                d[weight][item] = max(d[weight][item],
                                      d[weight - cur_weight][item - 1] +
                                      cell[item - 1])

    reincarnation = reincarnate(d, weights, cell)
    print(f"Method without repetitions counted price = {d[W][len(weights)]}")
    print("Included elements are:")

    for i in range(len(reincarnation)):
        if reincarnation[i] == 1:
            print(f"Element {i + 1}, weights {weights[i]} and costs {cell[i]}")


def knapSackWithRepetitions(W, weight, cell):
    D = [0] * (W+1)
    for w in range(1, W+1):
        for weight_i, cell_i in zip(weight, cell):
            if weight_i <= w:
                D[w] = max(D[w], D[w - weight_i] + cell_i)
    print(f"Maximum value without repetitions: {D[w]}\n")


if __name__ == '__main__':
    weights = [6, 3, 4, 2]
    cell = [30, 14, 16, 9]
    W = 10

    knapSackWithRepetitions(W, weights, cell)
    knapSackWithoutRepetitions(weights, cell)
