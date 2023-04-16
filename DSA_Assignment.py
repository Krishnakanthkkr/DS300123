#                                           PROBLEM 01


def find_pairs_with_sum(arr, target_sum):
    """
    Function to find all pairs of an integer array whose sum is equal to a given number.
    
    Parameters:
    arr (list): List of integers
    target_sum (int): The target sum to be achieved
    
    Returns:
    list: List of tuples representing pairs whose sum is equal to target_sum
    """
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pair = (num, complement) if num <= complement else (complement, num)
            pairs.append(pair)
        seen.add(num)
    
    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target_sum = 8
pairs = find_pairs_with_sum(arr, target_sum)
print("Pairs with sum", target_sum, "are:")
for pair in pairs:
    print(pair[0], "+", pair[1], "=", target_sum)
#output:
# Pairs with sum 8 are:
# 3 + 5 = 8
# 2 + 6 = 8 
                                            # PROBLEM 02


def reverse_array_in_place(arr):
    """
    Function to reverse an array in place.
    
    Parameters:
    arr (list): List of elements
    
    Returns:
    None
    """
    # Two pointers approach
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move pointers towards each other
        left += 1
        right -= 1

# Example usage:
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
reverse_array_in_place(arr)
print("Reversed array:", arr)
# output:
# Original array: [1, 2, 3, 4, 5]
# Reversed array: [5, 4, 3, 2, 1]
#                                   PROBLEM 03


def are_rotations(str1, str2):
    """
    Function to check if two strings are rotations of each other.
    
    Parameters:
    str1 (str): First string
    str2 (str): Second string
    
    Returns:
    bool: True if str1 and str2 are rotations of each other, False otherwise
    """
    # Lengths of the input strings
    len1 = len(str1)
    len2 = len(str2)
    
    # If lengths are not equal, str2 cannot be a rotation of str1
    if len1 != len2:
        return False
    
    # Concatenate str1 with itself
    str1 = str1 + str1
    
    # If str2 is a substring of the concatenated str1, it's a rotation
    if str2 in str1:
        return True
    else:
        return False

# Example usage:
str1 = "hello"
str2 = "lohel"
print("String 1:", str1)
print("String 2:", str2)
if are_rotations(str1, str2):
    print("String 2 is a rotation of String 1")
else:
    print("String 2 is not a rotation of String 1")
# OUTPUT:
# String 1: hello
# String 2: lohel
# String 2 is a rotation of String 1
#                                        PROBLE3M 04


def find_first_non_repeated_character(s):
    """
    Function to find the first non-repeated character from a string.
    
    Parameters:
    s (str): Input string
    
    Returns:
    str: The first non-repeated character, or None if no non-repeated character is found
    """
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeated character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeated character is found, return None
    return None

# Example usage:
s = "abccdeedcf"
print("Input string:", s)
first_non_repeated_char = find_first_non_repeated_character(s)
if first_non_repeated_char is not None:
    print("The first non-repeated character is:", first_non_repeated_char)
else:
    print("No non-repeated character found in the string")
# OUTPUT:
# Input string: abccdeedcf
# The first non-repeated character is: a
#                                         PROBLEM 05


def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Recursive function to solve the Tower of Hanoi puzzle.
    
    Parameters:
    n (int): Number of disks
    source (str): Source peg (e.g., 'A')
    auxiliary (str): Auxiliary peg (e.g., 'B')
    destination (str): Destination peg (e.g., 'C')
    
    Returns:
    None
    """
    if n == 1:
        # Base case: if there is only one disk, move it from source to destination peg
        print(f"Move disk 1 from {source} to {destination}")
        return
    else:
        # Move n-1 disks from source to auxiliary peg using destination peg as temporary peg
        tower_of_hanoi(n-1, source, destination, auxiliary)
        
        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")
        
        # Move n-1 disks from auxiliary to destination peg using source peg as temporary peg
        tower_of_hanoi(n-1, auxiliary, source, destination)

# Example usage:
n = 3
source = 'A'
auxiliary = 'B'
destination = 'C'
print(f"Solving Tower of Hanoi puzzle with {n} disks...")
tower_of_hanoi(n, source, auxiliary, destination)
# output:
# Solving Tower of Hanoi puzzle with 3 disks...
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
#                                      PROBLEM 06

def postfix_to_prefix(postfix_expr):
    """
    Function to convert postfix expression to prefix expression.
    
    Parameters:
    postfix_expr (str): Postfix expression
    
    Returns:
    str: Prefix expression
    """
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    # Iterate through the postfix expression from left to right
    for char in postfix_expr:
        if char not in operators:
            # If character is not an operator, it is an operand
            # Push it to the stack
            stack.append(char)
        else:
            # If character is an operator, pop top two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Construct the prefix expression by concatenating the operator
            # and the operands in reverse order
            prefix_expr = char + operand2 + operand1
            
            # Push the prefix expression back to the stack
            stack.append(prefix_expr)
    
    # The final prefix expression will be at the top of the stack
    return stack[-1]

# Example usage:
postfix_expr = "345*+"
print("Postfix expression:", postfix_expr)
prefix_expr = postfix_to_prefix(postfix_expr)
print("Prefix expression:", prefix_expr)
# output:
# Postfix expression: 345*+
# Prefix expression: +3*45
#                                  PROBLEM 07
def is_operator(char):
    """
    Function to check if a character is an operator (+, -, *, /, ^).
    
    Parameters:
    char (str): Character to check
    
    Returns:
    bool: True if the character is an operator, False otherwise
    """
    return char in set(['+', '-', '*', '/', '^'])

def prefix_to_infix(prefix_expr):
    """
    Function to convert prefix expression to infix expression.
    
    Parameters:
    prefix_expr (str): Prefix expression
    
    Returns:
    str: Infix expression
    """
    stack = []
    
    # Iterate through the prefix expression from right to left
    for char in reversed(prefix_expr):
        if not is_operator(char):
            # If character is not an operator, it is an operand
            # Push it to the stack
            stack.append(char)
        else:
            # If character is an operator, pop top two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Construct the infix expression by concatenating the operands,
            # the operator, and enclosing them in parentheses
            infix_expr = "(" + operand1 + char + operand2 + ")"
            
            # Push the infix expression back to the stack
            stack.append(infix_expr)
    
    # The final infix expression will be at the top of the stack
    return stack[-1]

# Example usage:
prefix_expr = "+*345"
print("Prefix expression:", prefix_expr)
infix_expr = prefix_to_infix(prefix_expr)
print("Infix expression:", infix_expr)
# output:
# Prefix expression: +*345
# Infix expression: ((3*4)+5)
#                                          PROBLEM 08

def are_brackets_closed(code):
    """
    Function to check if all the brackets are closed in a given code snippet.
    
    Parameters:
    code (str): Code snippet
    
    Returns:
    bool: True if all the brackets are closed, False otherwise
    """
    stack = []
    open_brackets = "([{"
    close_brackets = ")]}"
    
    for char in code:
        if char in open_brackets:
            # If character is an open bracket, push it to the stack
            stack.append(char)
        elif char in close_brackets:
            # If character is a close bracket, pop the top bracket from the stack
            if not stack:
                # If stack is empty, no matching open bracket found
                return False
            top = stack.pop()
            if open_brackets.index(top) != close_brackets.index(char):
                # If the popped open bracket does not match the current close bracket,
                # brackets are not closed properly
                return False
    
    # If stack is empty after processing all characters, brackets are closed properly
    return not stack

# Example usage:
code_snippet = "(a + b) * [c - {d / e}]"
print("Code snippet:", code_snippet)
if are_brackets_closed(code_snippet):
    print("All brackets are closed.")
else:
    print("Brackets are not closed properly.")
# OUTPUT:
# Code snippet: (a + b) * [c - {d / e}]
# All brackets are closed.

#                                          PROBLEM 09

class Stack:
    """
    Stack class to implement a stack data structure.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop the top item from the stack.
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """
        Peek at the top item in the stack.
        """
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        """
        Get the size of the stack.
        """
        return len(self.items)


def reverse_stack(stack):
    """
    Function to reverse the elements of a stack.
    
    Parameters:
    stack (Stack): Stack to reverse
    """
    if not stack.is_empty():
        # Pop the top item from the stack
        item = stack.pop()
        
        # Reverse the remaining stack
        reverse_stack(stack)
        
        # Insert the popped item at the bottom of the stack
        insert_at_bottom(stack, item)


def insert_at_bottom(stack, item):
    """
    Helper function to insert an item at the bottom of a stack.
    
    Parameters:
    stack (Stack): Stack to insert item into
    item: Item to insert
    """
    if stack.is_empty():
        # If stack is empty, push the item onto the stack
        stack.push(item)
    else:
        # If stack is not empty, recursively pop all items from the stack,
        # insert the item at the bottom of the remaining stack,
        # and push the popped items back onto the stack
        popped_item = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(popped_item)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Original stack:", stack.items)
reverse_stack(stack)
print("Reversed stack:", stack.items)


#                                         PROBLEM 10

class Stack:
    """
    Stack class to implement a stack data structure.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop the top item from the stack.
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """
        Peek at the top item in the stack.
        """
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        """
        Get the size of the stack.
        """
        return len(self.items)


def find_smallest_number(stack):
    """
    Function to find the smallest number in a stack.
    
    Parameters:
    stack (Stack): Stack to find smallest number from
    
    Returns:
    int: Smallest number in the stack
    """
    if stack.is_empty():
        return None

    # Pop the top item from the stack
    smallest = stack.pop()

    # Recursively find the smallest number in the remaining stack
    remaining_smallest = find_smallest_number(stack)

    # Compare the popped item with the smallest number in the remaining stack
    if remaining_smallest is not None and remaining_smallest < smallest:
        return remaining_smallest
    else:
        return smallest


# Example usage:
stack = Stack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(1)
stack.push(9)
print("Stack:", stack.items)
smallest_number = find_smallest_number(stack)
if smallest_number is not None:
    print("Smallest number in stack:", smallest_number)
else:
    print("Stack is empty")
