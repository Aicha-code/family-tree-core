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

    def get_parents(self):
        return self.parents
        
    def add_spouse(self, spouse):
        self.spouse = spouse
        spouse.spouse = self
        return spouse
    
    def get_siblings(self):
        siblings = set()
        for parent in self.parents:
            for child in parent.children:
                if child != self:
                    siblings.add(child)
        return list(siblings)

    def __str__(self):
        parents = ' & '.join(f"{parent.name}({parent.age})" for parent in self.parents) if self.parents else 'None'
        spouse = f"{self.spouse.name}({self.spouse.age})" if self.spouse else 'None'
        children = ', '.join(f"{c.name}({c.age})" for c in self.children) if self.children else 'None'
        siblings_list = self.get_siblings()
        siblings = ', '.join(f"{s.name}({s.age})" for s in siblings_list) if siblings_list else 'None'
        return (
            f"Member data:\n"
            f"{self.name}({self.age})\n"
            f" parents: {parents}\n"
            f" spouse: {spouse}\n"
            f" children: {children}\n"
            f" siblings: {siblings}"
        )

def search_member_by_name(members, name):
    for member in members:
        if member.name == name:
            return member
    return None    
if __name__ == "__main__":
    name = input("Enter member's name: ")
    age = input("Enter member's age: ")
    #parents
    parent_name = input("Enter father's name: ")
    parent_age = input("Enter father's age: ")
    parent = member(parent_name, parent_age)
    FamilyMember = member(name, age)
    FamilyMember.add_parent(parent)
    second_parent_name = input("Enter mother's name: ")
    second_parent_age = input("Enter mother's age: ")
    second_parent = member(second_parent_name, second_parent_age)
    FamilyMember.add_parent(second_parent)
    parents_married = input(f"Are the parents married? (y/n): ").strip().lower()
    if parents_married == 'y':
        parent.add_spouse(second_parent)
       
    print(f"Parents added: {parent.name}({parent.age}) and {parent.spouse.name}({parent.spouse.age})" if not parent.spouse else f"Parent added: {parent.name}({parent.age}) and {second_parent.name}({second_parent.age}) (married)")
    
    #spouse
    print(f"is {FamilyMember.name} married? (y/n): ")
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
        add_more = input(f"Do you want to add a child for {FamilyMember.name}? (y/n): ").strip().lower()
        if add_more == 'y':
            child_name = input("Enter child's name: ")
            child_age = input("Enter child's age: ")
            child_member = member(child_name, child_age)
            FamilyMember.add_child(child_member)
            print("Child added:", child_member)
        else:
            break

    # print(f"Member added: {FamilyMember.name}({FamilyMember.age})\nParents: {FamilyMember.parents[0].name}({FamilyMember.parents[0].age}) & {FamilyMember.parents[1].name}({FamilyMember.parents[1].age}) \nSpouse: {FamilyMember.spouse.name if FamilyMember.spouse else 'None'}({FamilyMember.spouse.age if FamilyMember.spouse else ''})\nChildren: {[child.name for child in FamilyMember.children]}({[child.age for child in FamilyMember.children]})\nSiblings: {[child.name for child in FamilyMember.parents[0].children if child != FamilyMember]}")
    print("list of all family members:")
    print(FamilyMember)
    for child in FamilyMember.children:
        print(child)
    print(FamilyMember.parents[0])
    print(FamilyMember.parents[1])


    print("Do you want to add children for the parents? (y/n): ")
    add_children_for_parents = input().strip().lower()
    if add_children_for_parents == 'y':
        for parent in FamilyMember.parents:
            while True:
                add_more = input(f"Do you want to add a child for {parent.name}? (y/n): ").strip().lower()
                if add_more == 'y':
                    child_name = input("Enter child's name: ")
                    child_age = input("Enter child's age: ")
                    child_member = member(child_name, child_age)
                    parent.add_child(child_member)
                    print("Child added:", child_member)
                else:
                    break

    print(FamilyMember)