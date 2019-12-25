class Stacks:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return self.stack==[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data

    def peep(self):
        return self.stack[-1]






stack=Stacks()
print(stack.isEmpty())
print(stack.push(5))
stack.push(15)
stack.push(25)
print(stack.pop())
print(stack.peep())
stack