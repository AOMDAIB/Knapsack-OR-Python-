from ortools.algorithms.python import knapsack_solver


def main():
    
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    values = [
        90,83,59,130,187,67,230,52,93,125,98
    ]
    weights = [
        
      [7,30,22,80,94,11,81,70,64,59,18],
        
    ]
    capacities = [350]

    solver.init(values, weights, capacities)
    computed_value = solver.solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print("Total weight:", total_weight)
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)


if __name__ == "__main__":
    main()
