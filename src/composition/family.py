class Mom:
    def __init__(self):
        self.parent_attribute = 'I am a Mom'
        self.color = 'blue'
        print('Mom init')

    def parent_method(self):
        print('Dance')
        return 'dance mom, dance'


class Dad:
    def __init__(self):
        self.parent_attribute = 'I am a Dad'
        self.color = 'brown'
        print('Dad init')

    def parent_method(self):
        print('Code')


# Create a child class that inherits from Parent
class Child:
    def __init__(self, mom, dad):
      self.parent_method = mom.parent_method
      self.color = dad.color
      self.parent_attribute = dad.parent_attribute


# Create instance of child
mom = Mom()
dad = Dad()
me = Child(mom, dad)
# # Show attributes and methods of child class
print(me.color)
print(me.parent_method())