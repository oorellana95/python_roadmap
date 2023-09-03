from linked_list import LinkedList, Node


def linked_list_simple_implementation():
    llist = LinkedList()

    first_node = Node("a")
    second_node = Node("b")
    third_node = Node("c")

    first_node.next = second_node
    second_node.next = third_node

    llist.head = first_node
    return llist


def linked_list_quick_implementation():
    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    return LinkedList(nodes=nodes)


def debugging_add_last():
    llist = LinkedList(nodes=['a', 'b', 'c', 'd', 'e', 'f'])
    llist.add_last(Node("e"))
    return llist


if __name__ == "__main__":
    print(debugging_add_last())
