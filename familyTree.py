
# A member is responsible for his/her relationships with other members of the family.

# the FamilyTree class is responsible for setting up the overall structure of the family tree, managing the collection of members, and providing methods to search for members by name or other attributes. It would also handle the logic for adding new members to the tree and ensuring that relationships are correctly established between members.

# the main is reponsible for member's data input and output, it will interact with the user to gather information about family members, such as their names, ages, and relationships. It will then use this information to create member instances and build the family tree. The main function will also display the family tree in a readable format (in the terminal), showing the relationships between members.

class FamilyTree:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def create_member(self, name, age, gender):
        for m in self.members:
            if m.name == name and m.age == int(age):
                return m   # return existing member

        member = Member(name, age, gender)
        self.add_member(member)
        return member

    def add_parent_child_relationship(self, parent1, parent2, child):
        if not all(isinstance(x, Member) for x in (parent1, parent2, child)):
            return "Invalid member."

        if len(child.parents) >= 2:
            return f"{child.name} already has 2 parents."

        if parent1.age - child.age < 15 or parent2.age - child.age < 15:
            return "Parents must be at least 15 years older than the child."

        child.add_parent(parent1)
        child.add_parent(parent2)


    def divorce_members(self, member1, member2):
        # Divorce is only possible if the members were previously married or in a recognized union, and they are not already divorced.
        if member2 not in member1.spouses:
            return "They are not currently married."
        if member2 not in member1.past_spouses:
            member1.add_past_spouse(member2)
            if member2 in member1.spouses:
                member1.spouses.remove(member2)
                member2.spouses.remove(member1)
            return f"{member1.name} and {member2.name} are now divorced."

    def marry_members(self, member1, member2):
        if not isinstance(member1, Member) or not isinstance(member2, Member):
            return "Both members must be valid Member instances."

        if member1.gender == member2.gender:
            return "Marriage requires a man and a woman."

        man = member1 if member1.gender == "m" else member2
        woman = member2 if man is member1 else member1
        # A man can have up to 4 wives
        if len(man.spouses) >= 4:
            return f"{man.name} cannot marry {woman.name} because he already has 4 wives."

        man.add_spouse(woman)
        return f"{man.name} and {woman.name} are now married."
    
    def get_siblings(self, member):
        siblings = set()
        for parent in member.parents:
            for child in parent.children:
                if child != member:
                    siblings.add(child)
        return list(siblings)

    def get_full_siblings(self, member):
        siblings = []
        for other in self.get_siblings(member):
            if set(other.parents) == set(member.parents):
                siblings.append(other)
        return siblings


    def get_half_siblings(self, member):
        half_siblings = []
        for other in self.get_siblings(member):
            if len(set(other.parents) & set(member.parents)) == 1:
                half_siblings.append(other)
        return half_siblings
   

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member

    def __str__(self):
        if not self.members:
            return "<No members in family tree>"
        lines = ["Family Tree Members:\n"]
        for m in self.members:
            lines.append(str(m))
            lines.append("-" * 40)
        return "\n".join(lines)

class Member:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.children = []
        self.parents = []  # limit this to 2 parents
        self.spouses = []  # store all spouses
        self.past_spouses = []  # store past relationships for parents and spouse


    def add_parent(self, parent):
        if len(self.parents) < 2 and parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)

    def add_spouse(self, spouse):
        if spouse not in self.spouses:
            self.spouses.append(spouse)
            spouse.spouses.append(self)

    def add_past_spouse(self, past_spouse):
        if past_spouse not in self.past_spouses:
            self.past_spouses.append(past_spouse)
            past_spouse.past_spouses.append(self)


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

        # compute siblings (any shared parent)
        siblings_set = set()
        for parent in self.parents:
            for child in parent.children:
                if child is not self:
                    siblings_set.add(child)
        siblings = (
            ", ".join(f"{s.name}({s.age})" for s in siblings_set) if siblings_set else "None"
        )

        return (
            f"{self.name} ({self.age}, {'Male' if self.gender=='m' else 'Female'})\n"
            f" Parents: {parents}\n"
            f" Spouse(s): {current_spouses}\n"
            f" Past spouses: {past_spouses}\n"
            f" Children: {children}\n"
            f" Siblings: {siblings}\n"
        )




if __name__ == "__main__":
    def ask(prompt, required=True):
        while True:
            v = input(prompt).strip()
            if v or not required:
                return v

    def ask_gender(prompt):
        while True:
            g = input(prompt).strip().lower()
            if g in ("m", "f"):
                return g

    def prompt_member(tree, label="member", gender=None):
        name = ask(f"Enter {label} name: ")
        age = ask(f"Enter {label} age: ")
        gender = gender or ask_gender(f"What is {name}'s gender? (m/f): ")
        return tree.create_member(name, age, gender)

    def add_children(tree, parent1, parent2, parent1_is_male=True):
        while True:
            add_more = ask(f"Add a child for {parent1.name} and {parent2.name}? (y/n): ", required=True).lower()
            if add_more != "y":
                break
            child = prompt_member(tree, "child")
            if parent1_is_male:
                tree.add_parent_child_relationship(parent1, parent2, child)
            else:
                tree.add_parent_child_relationship(parent2, parent1, child)

    tree = FamilyTree()
    member = prompt_member(tree, "new member")

    # parents
    print("--- Enter parent details ---")
    father = prompt_member(tree, "father", gender="m")
    mother = prompt_member(tree, "mother", gender="f")
    tree.add_parent_child_relationship(father, mother, member)
    status = ask("Parents' relationship status: 1) Married 2) Divorced 3) None — choose 1/2/3: ")
    if status == "1":
        tree.marry_members(father, mother)
    elif status == "2":
        tree.marry_members(father, mother)
        tree.divorce_members(father, mother)

    print(f"Parents added: {father.name}({father.age}) and {mother.name}({mother.age})")

    # spouse and children for main member
    if ask(f"Is {member.name} married? (y/n): ").lower() == "y":
        spouse = prompt_member(tree, "spouse", gender="f" if member.gender == "m" else "m")
        tree.marry_members(member, spouse)
        add_children(tree, member, spouse, parent1_is_male=(member.gender == "m"))

    # past spouses
    while ask(f"Add a past spouse for {member.name}? (y/n): ", required=False).lower() == "y":
        past = prompt_member(tree, "past spouse", gender="f" if member.gender == "m" else "m")
        tree.marry_members(member, past)
        tree.divorce_members(member, past)
        add_children(tree, member, past, parent1_is_male=(member.gender == "m"))

    # allow adding spouses/children for each parent
    for parent in member.parents:
        while ask(f"Add a spouse (current/past) for {parent.name}? (y/n): ", required=False).lower() == "y":
            partner = prompt_member(tree, "partner", gender="f" if parent.gender == "m" else "m")
            rel = ask("Type 'current' or 'past': ")
            if rel == "current":
                tree.marry_members(parent, partner)
            else:
                tree.marry_members(parent, partner)
                tree.divorce_members(parent, partner)
            add_children(tree, parent, partner, parent1_is_male=(parent.gender == "m"))

    # final output
    print("\n--- Member summary ---")
    print(member)
    print("\n*** Full family tree ***")
    print(tree)
