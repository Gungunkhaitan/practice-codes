class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    stack = []
    current = head

    # Push each node onto the stack
    while current:
        stack.append(current)
        current = current.next

    # Pop nodes from the stack to reverse the linked list
    if stack:
        head = stack.pop()
        current = head
        while stack:
            current.next = stack.pop()
            current = current.next

        current.next = None

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Creating the linked list D->A->T->A->S->T->R->U->C->T->U->R->E
D = Node('D')
A = Node('A')
T = Node('T')
A2 = Node('A')
S = Node('S')
T2 = Node('T')
R = Node('R')
U = Node('U')
C = Node('C')
T3 = Node('T')
U2 = Node('U')
R2 = Node('R')
E = Node('E')

D.next = A
A.next = T
T.next = A2
A2.next = S
S.next = T2
T2.next = R
R.next = U
U.next = C
C.next = T3
T3.next = U2
U2.next = R2
R2.next = E

print("Original Linked List:")
print_linked_list(D)

# Reverse the linked list
D = reverse_linked_list(D)

print("\nReversed Linked List:")
print_linked_list(D)