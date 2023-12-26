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

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Dépilement : ",s.pop())

    

