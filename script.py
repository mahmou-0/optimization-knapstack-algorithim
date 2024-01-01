class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value

def main():
    items = []
    n = int(input("Enter the number of items: "))

    for i in range(n):
        value = float(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack = {max_value}")

if __name__ == "__main__":
    main()
