import random
class Person:
    def __init__(self,name ,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>=18:
             self.__age=age
        else:
            print("Invalid age")
            return
    
class  Member(Person):
    def __init__(self,name ,age,member_id,activity):
        super().__init__(name,age)
        self.member_id=member_id
        self.activity=activity

class Club:  
    def __init__(self):
        self.members = []
        self.activities = ["Programming", "Design", "Culture", "Math", "Science"]
        self.load_from_file() 
    def save_to_file(self):
     with open("data.txt", "w") as file:
        for m in self.members:
            line = f"{m.name},{m.get_age()},{m.member_id},{m.activity}\n"
            file.write(line)


    def load_from_file(self):
     try:
        with open("data.txt", "r") as file:
            for line in file:
                name, age, member_id, activity = line.strip().split(",")
                member = Member(name, int(age), int(member_id), activity)
                self.members.append(member)
     except FileNotFoundError:
        pass
     

    def add_member(self):
        name = input("Enter name: ")
        if not name.isalpha():
          print("Name must contain letters only")
          return
        age = int(input("Enter age: "))
        print("=====================")
        if age>=18:
           age = age
        else:
           print("Age must be 18 or above")
           return 
        member_id = random.randint(100, 999)
        
        while True:
           for i, act in enumerate(self.activities, 1):
             print(i, act)
           try:
                i = int(input("Enter activity number : "))
                if i < 1 or i > len(self.activities):
                  print("Invalid activity number")
                  
                else:
                   break
           except ValueError:
             print("Please enter a valid number")
             
        activity = self.activities[i - 1]
        member = Member(name, age, member_id, activity)
        self.members.append(member)
        self.save_to_file()
        print(f"Your member ID is: {member_id} 🎓")

    def display_all(self):
        if len(self.members)==0:
            print("No members found")
        else:
         for m in self.members:
           print( f'Name: {m.name}| Age: {m.get_age()}| id: {m.member_id}| activity: {m.activity}')
           
    def delete_member(self):
          d = int(input("Enter id you want delete: "))
          found = False
          
          

          for m in self.members:
           if d==9998:
             self.members.clear()
             self.save_to_file()
             print("Deleted")
           elif m.member_id == d:
             self.members.remove(m)
             self.save_to_file()   
             print("Deleted")
             found = True
             break   

          if not found:
           print("Not Found")

    def update_member(self):
        d=int(input("Enter id you want update:"))
        found = False
        for m in self.members:
          if m.member_id == d:
            u=int(input("What do you want to update?\n1. Name\n2. Age\n3. Activity\nEnter your choice: "))
            if u == 1:
                m.name=input("Enter new name:")
            elif u==2:
                m.set_age(int(input("Enter new age: ")))
            elif u ==3:
                for i, act in enumerate(self.activities, 1):
                   print(i, act)
                i = int(input("Enter activity number : "))
                activity = self.activities[i - 1]
                m.activity = activity 
            self.save_to_file()       
            found=True

            
        
        if found==True:
         print("update✅")
        else:
         print("Not Found")

    def search_member(self):
        d=int(input("Enter id you want search:"))
        found = False
        for m in self.members:
          if m.member_id == d:
            print( f'Name: {m.name}| Age: {m.get_age()}| id: {m.member_id}| activity: {m.activity}')
            found=True
        
        if  not found:
         print("Not Found")
    

    def statistics_member(self):
     count = {}

     for m in self.members:
        if m.activity in count:
            count[m.activity] += 1
        else:
            count[m.activity] = 1

     print(f"Total members: {len(self.members)}")  

     for activity, c in count.items():
         print(f"{activity}: {c}")


def main_menu():
    c1 = Club()
    while True:
      
        print("\n--- 🎓 Student Club System ---")
        print("  1. ➕ Add Member")
        print("  2. 📋 Display All")
        print("  3. 🗑️  Delete Member")
        print("  4. ✏️  Update Member")
        print("  5. 🔍 Search Member")
        print("  6. 📊 Statistics")
        print("  7. 🚪 Exit")
        print("-" * 30)
        choes = int(input("Enter your choice: "))
        if choes == 1:
            c1.add_member()
        elif choes == 2:
            c1.display_all()
        elif choes == 3:
            c1.delete_member()
        elif choes == 4:
            c1.update_member()
        elif choes == 5:
            c1.search_member()
        elif choes == 6:
            c1.statistics_member()
        elif choes == 7:
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main_menu()