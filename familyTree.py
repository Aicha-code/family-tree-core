
# A member is responsible for his/her relationships with other members of the family.

# the FamilyTree class is responsible for setting up the overall structure of the family tree, managing the collection of members, and providing methods to search for members by name or other attributes. It would also handle the logic for adding new members to the tree and ensuring that relationships are correctly established between members.

# the main is reponsible for member's data input and output, it will interact with the user to gather information about family members, such as their names, ages, and relationships. It will then use this information to create member instances and build the family tree. The main function will also display the family tree in a readable format (in the terminal), showing the relationships between members.

class FamilyTree:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def create_member(self, name, age, gender):
        member = Member(name, age, gender)
        self.add_member(member)
        return member
    
    def add_parent_child_relationship(self, parent1, parent2, child):
        if not isinstance(child, Member) or not isinstance(parent1, Member) or not isinstance(parent2, Member):
            return "Invalid child member."
        if len(child.parents) >= 2:
            return f"{child.name} already has 2 parents."
        elif parent1.age - child.age <= 15 or parent2.age - child.age <= 15:
            return f"{child.name} cannot be a child of {parent1.name} and {parent2.name} due to age difference."
        else:
            child.add_parent(parent1)
            child.add_parent(parent2)

    def divorce_members(self, member1, member2):
        if member2 not in member1.past_spouses:
            member1.add_past_spouse(member2)
            if member2 in member1.spouses:
                member1.spouses.remove(member2)
                member2.spouses.remove(member1)
            return True

    def marry_members(self, member1, member2):
        #man cannot have more than 4 wives at a time, but can have multiple past wives
        if member1.gender == "m" and member2.gender == "f":
            # users will first enter the man's name and then the wife's name
            if member1.spouses and len(member1.spouses) >= 4:
                return f"{member1.name} cannot marry {member2.name} because he already has 4 wives."
            member1.add_spouse(member2)
            return f"{member1.name} and {member2.name} are now married."
        else:
            return f"Please make sure to enter first the man's name then the lady's."
            

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

class Member:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.children = []
        self.parents = []  # limit this to 2 parents
        self.spouses = []  # store all spouses
        self.past_spouses = []  # store past relationships for parents and spouse

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
        self.spouses.append(spouse)
        spouse.spouses.append(self)

    def get_spouses(self):
        return self.spouses

    def add_past_spouse(self, past_spouse):
        self.past_spouses.append(past_spouse)
        past_spouse.past_spouses.append(self)

    def get_siblings(self):
        siblings = set()
        for parent in self.parents:
            for child in parent.children:
                if child != self:
                    siblings.add(child)
        return list(siblings)

    def __str__(self):
        parents = (
            " & ".join(f"{parent.name}({parent.age})" for parent in self.parents)
            if self.parents
            else "None"
        )
        current_spouses = (
            ", ".join(f"{s.name}({s.age})" for s in self.spouses)
            if self.spouses            
            else "None"
        )
        past_spouses = (
            ", ".join(f"{ps.name}({ps.age})" for ps in self.past_spouses)
            if self.past_spouses
            else "None"
        )
        children = (
            ", ".join(f"{c.name}({c.age})" for c in self.children)
            if self.children
            else "None"
        )
        siblings_list = self.get_siblings()
        siblings = (
            ", ".join(f"{s.name}({s.age})" for s in siblings_list)
            if siblings_list
            else "None"
        )
        return (
            f"\nMember data:\n"
            f"{self.name}({self.age})\n"
            f" spouse(s): {current_spouses}\n"
            f" past spouses: {past_spouses}\n"
            f" children: {children}\n"
            f" siblings: {siblings}"
        )




if __name__ == "__main__":
    tree = FamilyTree()
    name = input("Enter member's name: ")
    age = input("Enter member's age: ")
    FamilyMember= tree.create_member(name, age, "m" if input(f"What is {name}'s gender? (m/f): ").strip().lower() == "m" else "f")
    # parents
    father_name = input("Enter father's name: ")
    father_age = input("Enter father's age: ")
    father = tree.create_member(father_name, father_age, "m")
    # FamilyMember.add_parent(father)

    mother_name = input("Enter mother's name: ")
    mother_age = input("Enter mother's age: ")
    mother = tree.create_member(mother_name, mother_age, "f")
    tree.add_parent_child_relationship(father, mother, FamilyMember)
    parents_married = input(f"Are the parents married? (y/n): ").strip().lower()
    if parents_married == "y":
        tree.marry_members(father, mother)
    else:
        tree.divorce_members(father, mother)

    print(
        f"Parents added: {father.name}({father.age}) and {mother.name}({mother.age}) "
        + "(divorced)"
        if not father.spouses
        else "(married)"
    )

    # spouse
    print(f"is {FamilyMember.name} married? (y/n): ")
    married = input().strip().lower()
    if married == "y":
        spouse_name = input("Enter spouse's name: ")
        spouse_age = input("Enter spouse's age: ")
        spouse = tree.create_member(spouse_name, spouse_age, "m" if FamilyMember.gender == "f" else "f")
        tree.marry_members(FamilyMember, spouse)
        print(f"Spouse added: {spouse.name}({spouse.age})")
    else:
        spouse = None

    while True:
        divorced = (
            input(f"Add a past spouse for {FamilyMember.name}? (y/n): ").strip().lower()
        )
        if divorced == "y":
            print("Enter details of past spouse:")
            past_spouse_name = input("Past spouse's name: ")
            past_spouse_age = input("Past spouse's age: ")
            past_spouse = tree.create_member(past_spouse_name, past_spouse_age, "m" if input(f"What is {past_spouse_name}'s gender? (m/f): ").strip().lower() == "m" else "f")
            tree.divorce_members(FamilyMember, past_spouse)
            print(f"Past spouse added: {past_spouse.name}({past_spouse.age})")
        else:
            break
    while True:
        add_more = (
            input(f"Do you want to add a child for {FamilyMember.name} and {spouse.name if spouse else 'None'}? (y/n): ")
            .strip()
            .lower()
        )
        if add_more == "y":
            child_name = input("Enter child's name: ")
            child_age = input("Enter child's age: ")
            child_member = tree.create_member(child_name, child_age, "m" if input(f"What is {child_name}'s gender? (m/f): ").strip().lower() == "m" else "f")
            tree.add_parent_child_relationship(FamilyMember, spouse, child_member ) if FamilyMember.gender == "m" else tree.add_parent_child_relationship(spouse, FamilyMember, child_member)
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
    if add_children_for_parents == "y":
        for parent in FamilyMember.parents:
            while True:
                add_more = (
                    input(f"Do you want to add another child for {father.name} and {mother.name}? (y/n): ")
                    .strip()
                    .lower()
                )
                if add_more == "y":
                    child_name = input("Enter child's name: ")
                    child_age = input("Enter child's age: ")
                    child_member = tree.create_member(child_name, child_age, "m" if input(f"What is {child_name}'s gender? (m/f): ").strip().lower() == "m" else "f")
                    tree.add_parent_child_relationship(father, mother, child_member)
                      # adding the same parent twice to satisfy the method's requirement of two parents
                else:
                    break

    print(FamilyMember)
