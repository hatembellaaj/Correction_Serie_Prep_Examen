#Question 1 - Classe Pile
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            #last In First out
            #Exemple [1,2,3,4,5] => ça retourne le 5 c'est le dernier élément qu'a entré 
            return self.items.pop()  

    def is_empty(self):
        return len(self.items) == 0

#question 3
def reverse_stack(stack):
    reversed_stack = Stack()
    while not stack.is_empty():
        reversed_stack.push(stack.pop())
    return reversed_stack
#question 5
def parentheses_balance(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if not is_matching(top, char):
                return False
    return stack.is_empty()

def is_matching(opening, closing):
    return (opening == "(" and closing == ")") or \
           (opening == "{" and closing == "}") or \
           (opening == "[" and closing == "]")

# Exemple d'utilisation
expression = "{[()]}"
result = parentheses_balance(expression)
print(f"L'expression {expression} est équilibrée : {result}")






s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Dépilement : ",s.pop())

r = reverse_stack(s)
print("Contenu de r: ", r.items)
print("contenu de s: ", s.items) #On remarque que s s'est vidé et c'est normal 

