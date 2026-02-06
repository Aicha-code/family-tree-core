
# A member is responsible for his/her relationships with other members of the family.

# the FamilyTree class is responsible for setting up the overall structure of the family tree, managing the collection of members, and providing methods to search for members by name or other attributes. It would also handle the logic for adding new members to the tree and ensuring that relationships are correctly established between members.

# the main is reponsible for member's data input and output, it will interact with the user to gather information about family members, such as their names, ages, and relationships. It will then use this information to create member instances and build the family tree. The main function will also display the family tree in a readable format (in the terminal), showing the relationships between members.

class FamilyTree:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
        self.parents = []  # limit this to 2 parents
        self.spouse = None
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
        self.spouse = spouse
        spouse.spouse = self
        return spouse

    def get_spouse(self):
        return self.spouse

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
        spouse = f"{self.spouse.name}({self.spouse.age})" if self.spouse else "None"
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
            f"Member data:\n"
            f"{self.name}({self.age})\n"
            f" spouse: {spouse}\n"
            f" past spouses: {past_spouses}\n"
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
    # parents
    parent_name = input("Enter father's name: ")
    parent_age = input("Enter father's age: ")
    parent = Member(parent_name, parent_age)
    FamilyMember = Member(name, age)
    FamilyMember.add_parent(parent)
    second_parent_name = input("Enter mother's name: ")
    second_parent_age = input("Enter mother's age: ")
    second_parent = Member(second_parent_name, second_parent_age)
    FamilyMember.add_parent(second_parent)
    parents_married = input(f"Are the parents married? (y/n): ").strip().lower()
    if parents_married == "y":
        parent.add_spouse(second_parent)
    else:
        parent.add_past_spouse(second_parent)

    print(
        f"Parents added: {parent.name}({parent.age}) and {second_parent.name}({second_parent.age}) "
        + "(divorced)"
        if not parent.spouse
        else "(married)"
    )

    # spouse
    print(f"is {FamilyMember.name} married? (y/n): ")
    married = input().strip().lower()
    if married == "y":
        spouse_name = input("Enter spouse's name: ")
        spouse_age = input("Enter spouse's age: ")
        spouse = Member(spouse_name, spouse_age)
        FamilyMember.add_spouse(spouse)
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
            past_spouse = Member(past_spouse_name, past_spouse_age)
            FamilyMember.add_past_spouse(past_spouse)
            print(f"Past spouse added: {past_spouse.name}({past_spouse.age})")
        else:
            break
    while True:
        add_more = (
            input(f"Do you want to add a child for {FamilyMember.name}? (y/n): ")
            .strip()
            .lower()
        )
        if add_more == "y":
            child_name = input("Enter child's name: ")
            child_age = input("Enter child's age: ")
            child_member = Member(child_name, child_age)
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
    if add_children_for_parents == "y":
        for parent in FamilyMember.parents:
            while True:
                add_more = (
                    input(f"Do you want to add a child for {parent.name}? (y/n): ")
                    .strip()
                    .lower()
                )
                if add_more == "y":
                    child_name = input("Enter child's name: ")
                    child_age = input("Enter child's age: ")
                    child_member = Member(child_name, child_age)
                    parent.add_child(child_member)
                    print("Child added:", child_member)
                else:
                    break

    print(FamilyMember)
