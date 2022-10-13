from collections import Counter
from collections import deque
import heapq


def main():
    # Set
    volwels = frozenset({"a", "e", "i", "o", "u"})
    print(volwels)

    # Multiset
    inventory = Counter()
    loot = {"sword": 1, "bread": 3}
    inventory.update(loot)
    print(inventory)

    # Priority queue
    print("\nHeap:")
    my_heap = []
    heapq.heappush(my_heap, (10, "value1"))
    heapq.heappush(my_heap, (200, "value2"))
    heapq.heappush(my_heap, (1, "value3"))
    while my_heap:
        print(heapq.heappop(my_heap))

    # Queue: implemented as a double linked list
    print("\nQueue:")
    my_queue = deque()
    my_queue.append(1)
    my_queue.append(2)
    my_queue.append(3)
    while my_queue:
        print(my_queue.popleft())

    # Stack
    print("\nStack:")
    my_stack = deque()
    my_stack.append(1)
    my_stack.append(2)
    my_stack.append(3)
    while my_stack:
        print(my_stack.pop())


if __name__ == "__main__":
    main()