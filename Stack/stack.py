class STACK:
    def __init__(self):
        self.st=[]
        self.size=5 
    
    def push(self,data):
        if self.size==0:
            return 
        else:
            self.size-=1
            self.st.append(data)

    def print(self):
        print(self.st)
    


s=STACK()
s.push('10')
s.push('11')
print(s.print())