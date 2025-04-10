class Link_Node:
    def __init__(self, elem):
        self.elem = elem
        self.nextNode = None
        self.prevNode = None

class Link_Array:
    def __init__(self):
        self._Start = None
        self._End = None

    def Add_In_End(self, elem):
        new_node = Link_Node(elem)

        if self._Start == None:
            self._Start = new_node
            self._End = new_node
        else:
            self._End.nextNode = new_node
            new_node.prevNode = self._End
            self._End = new_node
        
    def Add_In_Start(self, elem):
        new_node = Link_Node(elem)

        if self._Start == None:
            self._Start = new_node
            self._End = new_node
        else:
            self._Start.prevNode = new_node
            new_node.nextNode = self._Start
            self._Start = new_node

    def Add_In_Position(self, elem, position : int):
        if position >= self.Get_Count_Elements():
            self.Add_In_End(elem)
        elif position <= 0:
            self.Add_In_Start(elem)
        else:
        
            new_node = Link_Node(elem)
            
            counter = 0

            p = self._Start
            prev = p

            if p == None:
                print("There is no positions, adding in _Start")
                self._Start = new_node
                self._End = new_node
            else:

                while counter < position:
                    prev = p
                    p = p.nextNode
                    counter = counter + 1

                prev.nextNode = new_node
                new_node.prevNode = prev
                new_node.nextNode = p

    def Delete_From_End(self):
        if self._Start == None:
            print("There is no elements")
        elif self._Start == self._End:
            self._Start = None
            self._End = None
        else:
            p = self._End
            self._End = self._End.prevNode
            self._End.nextNode = None
            p.prevNode = None
            p = None
            
    def Delete_From_Start(self):
        if self._Start == None:
            print("There is no elements")
        elif self._Start == self._End:
            self._Start = None
            self._End = None
        else:
            p = self._Start
            self._Start = self._Start.nextNode
            self._Start.prevNode = None
            p.nextNode = None
            p = None

    def Delete_From_Position(self, position):
        if self._Start == None:
            print("There is no elements")
        elif self._Start == self._End:
            self._Start = None
            self._End = None
        else:
            if position >= self.Get_Count_Elements():
                self.Delete_From_End()
            elif position <= 0:
                self.Delete_From_Start()
            else:
                counter = 0
                p = self._Start
                prev = p
                while counter < position:
                    prev = p
                    p = p.nextNode
                    counter = counter + 1
            
                n = p.nextNode
                prev.nextNode = p.nextNode
                p.prevNode = None
                p.nextNode = None
                n.prevNode = prev
                n = None

    def Get_Elem_By_Position(self, position):
        if self._Start == None:
            print("There is no elements")
        elif self._Start == self._End:
            print("There is only one element")
            return self._Start.elem
        else:
            counter = 0
            p = self._Start
            prev = p
            while counter < position:
                prev = p
                p = p.nextNode
                counter = counter + 1
            
            return prev.elem

    def Get_Node_By_Position(self, position):
        if self._Start == None:
            print("There is no node")
        elif self._Start == self._End:
            print("There is only one node")
            return self._Start
        else:
            counter = 0
            p = self._Start
            prev = p
            while counter < position:
                prev = p
                p = p.nextNode
                counter = counter + 1
            
            return prev

    def Get_Count_Elements(self):
        counter = 0
        p = self._Start
        while p != None:
            counter = counter + 1
            p = p.nextNode

        return counter

    def Print_Array(self):
        p = self._Start
        while p != None:
            print(p.elem, "\n")
            p = p.nextNode

if __name__ == "__main__":
    spis=Link_Array()

    for i in range(13):
        spis.Add_In_End(i)

    spis.Add_In_Position("test", 6)

    spis.Delete_From_End()
    spis.Delete_From_Start()

    spis.Delete_From_Position(5)
    spis.Delete_From_Position(50)
    spis.Delete_From_Position(-4)
    spis.Delete_From_Position(5)
    spis.Delete_From_Position(5)
    spis.Delete_From_Position(5)
    
    print(spis.Get_Count_Elements())

    print(spis.Get_Elem_By_Position(3))

    spis.Print_Array()
