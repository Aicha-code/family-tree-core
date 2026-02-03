class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
        self.parents = [] #limit this to 2 parents
        self.spouse = None

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)
    def get_children(self):
        return self.children

    def add_parent(self, parent):
        if len(self.parents) < 2 and parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)
        
    def add_spouse(self, spouse):
        self.spouse = spouse
        return spouse

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Parents: {[parent.name for parent in self.parents]}, Spouse: {self.spouse.name if self.spouse else 'None'}, Children: {[child.name for child in self.children]}"
    
def search_member_by_name(members, name):
    for member in members:
        if member.name == name:
            return member
    return None    
if __name__ == "__main__":
    name = input("Enter member's name: ")
    age = input("Enter member's age: ")
    parent_name = input("Enter parent's name: ")
    parent_age = input("Enter parent's age: ")
    parent = member(parent_name, parent_age)
    FamilyMember = member(name, age)
    FamilyMember.add_parent(parent)
    print("add second parent? (y/n): ")
    add_second_parent = input().strip().lower()
    if add_second_parent == 'y':
        second_parent_name = input("Enter second parent's name: ")
        second_parent_age = input("Enter second parent's age: ")
        second_parent = member(second_parent_name, second_parent_age)
        parent.add_spouse(second_parent)
    FamilyMember.add_parent(second_parent) if add_second_parent == 'y' else None
    print(f"Parents added: {parent.name}({parent.age}) and {parent.spouse.name}({parent.spouse.age})" if parent.spouse else f"Parent added: {parent.name}({parent.age})")
    print("married? (y/n): ")
    married = input().strip().lower()
    if married == 'y':
        spouse_name = input("Enter spouse's name: ")
        spouse_age = input("Enter spouse's age: ")
        spouse = member(spouse_name, spouse_age)
        FamilyMember.add_spouse(spouse)
        print(f"Spouse added: {spouse.name}({spouse.age})")
    else:
        spouse = None
    
    while True:
        add_more = input("Do you want to add a child for this member? (y/n)): ").strip().lower()
        if add_more == 'y':
            child_name = input("Enter child's name: ")
            child_age = input("Enter child's age: ")
            child_member = member(child_name, child_age)
            FamilyMember.add_child(child_member)
            print("Child added:", child_member)
        else:
            break

    print(f"Member added: {FamilyMember.name}({FamilyMember.age})\n parents: {FamilyMember.parents[0].name}({FamilyMember.parents[0].age}) & {FamilyMember.parents[1].name}({FamilyMember.parents[1].age if FamilyMember.parents[1] else ''}) \n spouse: {FamilyMember.spouse.name if FamilyMember.spouse else 'None'}({FamilyMember.spouse.age if FamilyMember.spouse else ''})\n children: {[child.name for child in FamilyMember.children]}")
