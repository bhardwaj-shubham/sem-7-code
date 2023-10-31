# Item class with value and weight
class Item:
    def __init__(self, value, weight) -> None:
        self.value = value
        self.weight = weight


# Function to solve fractional knapsack
def fractionalKnapsack(W, arr):
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0
    for item in arr:
        # Checking if adding item will cause overflow
        if item.weight <= W:
            W -= item.weight
            total_value += item.value
        # If Knapsack is not overflow then taking fractional part
        else:
            total_value += item.value * W / item.weight
            break
    return total_value


# Driver code
if __name__ == "__main__":
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    W = 50
    print(fractionalKnapsack(W, arr))
