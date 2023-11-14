class Node:
    def __init__(self,data=None,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
    
    def set_data(self,data) -> None:
        self.data=data

    def get_data(self) -> object:
        return self.data

    def set_next(self,next) -> None:
        self.next=next
    
    def get_next(self) -> object:
        return self.next

    def set_previous(self,previous) -> None:
        self.previous=previous

    def get_previous(self) -> object:
        return self.previous

    def __eq__(self,node) -> bool:
        return self.data==node.get_data()
    
    def __ne__(self,node) -> bool:
        return not self==node

    def __str__(self) -> str:
        return str(self.data)