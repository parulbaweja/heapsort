def heapsort(lst):
    """
    Sorts list in-place with a heap.
    """
    last_element = len(lst) - 1
    lst = heapify(lst)

    while last_element >= 0:
        # swap the max element with the last element
        # like popping off the max
        swap(lst, 0, last_element)
        # rebalance the remaining heap, from index 0 to last_element exclusive
        bal_down(lst, 0, last_element)
        last_element -= 1

    return lst


def heapify(lst):
    """
    Turns list into a max heap in-place, in linear time.
    Begins process at 1 depth before leaves.
    """

    # initiliazes cur at halfway point based on length of list
    if len(lst) % 2 == 0:
        cur = len(lst) / 2 - 2
    else:
        cur = len(lst) / 2 - 1

    # rebalance until reached beginning of list
    while cur >= 0:
        bal_down(lst, cur)

        cur -= 1

    return lst


def bal_down(lst, cur, last_element=None):
    """
    Rebalances heap. Keyword arg for last_element allows for re-use
    in both heapify and heapsort.
    """

    if last_element is None:
        last_element = len(lst)

    while cur < last_element:
        left_child = 2*cur + 1
        right_child = 2*cur + 2

        # check to see if we're out of bounds for the children
        # this is necessary for even length heaps
        if left_child >= last_element:
            return
        if right_child >= last_element:
            # since left child is in bounds, check for swap
            if lst[cur] < lst[left_child]:
                swap(lst, cur, left_child)
            return

        # if we're in bounds for both children, find the max
        max_child = find_max_child(lst, left_child, right_child)

        # check to see if swap needed
        if lst[cur] < lst[max_child]:
            swap(lst, cur, max_child)
        cur = max_child


def find_max_child(lst, left_child, right_child):
    """
    Returns index of larger child.
    """
    if lst[left_child] > lst[right_child]:
        child = left_child
    else:
        child = right_child

    return child


def swap(lst, i, last_element):
    """
    Swaps two elments of a list - the current and last in this case.
    """
    lst[i], lst[last_element] = lst[last_element], lst[i]


print heapsort([10, 3, 8, 2, 1, 6])
print heapsort([5, 10, 12, 2, 1, 8, 20, 7, 15, 21, 2, 1, 1, 0, 13])
