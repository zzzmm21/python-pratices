class user:
    def __init__(self,id,password) -> None:
        self.id= id
        self.password = password
    def printUser(self):
        print(f"id: {self.id} , password : {self.password}")

    def change_id(self,id):
        self.id = id

