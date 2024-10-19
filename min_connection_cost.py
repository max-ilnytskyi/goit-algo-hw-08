import heapq


def min_connection_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        print(f"Connect {first} and {second}")

        current_cost = first + second
        total_cost += current_cost

        heapq.heappush(cables, current_cost)

    return total_cost


cables = [4, 3, 2, 6, 7, 12, 1]
print(min_connection_cost(cables))
