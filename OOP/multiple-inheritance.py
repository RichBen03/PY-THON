class grandParent:
    def walking(self):
        return f"you inherited your grandparent walking style"
class Parent:
    def eyes(self):
        return f"you inherited are your parent eye color"
class Children(Parent,grandParent):
    def genes(self):
        return f"You have genes from both the parents and grandparents"
    
child = Children()
print(child.eyes()) #Inheriting the method from Parent 
print(child.walking()) #Inheriting the method from grandParent
print(child.genes())

    
