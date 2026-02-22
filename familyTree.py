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
                return m  # return existing member

        member = Member(name, age, gender)
        self.add_member(member)
        return member

    def add_parent_child_relationship(self, parent1, parent2, child):
        if not all(isinstance(x, Member) for x in (parent1, parent2, child)):
            return "Invalid member."

        if parent1.gender == parent2.gender:
            return "A child must have one male and one female parent."

        if len(child.parents) >= 2:
            return f"{child.name} already has 2 parents."

        if parent1.age - child.age < 15 or parent2.age - child.age < 15:
            return "Parents must be at least 15 years older than the child."

        child.add_parent(parent1)
        child.add_parent(parent2)

    def divorce_members(self, member1, member2):
        # Divorce is only possible if the members were previously married or in a recognized union, and they are not already divorced.
        if not member1.is_alive or not member2.is_alive:
            return "Cannot divorce a deceased member."
        if member2 not in member1.spouses:
            return "They are not currently married."
        member1.add_past_spouse(member2)
        if member2 in member1.spouses:
            member1.spouses.remove(member2)
            member2.spouses.remove(member1)
        return f"{member1.name} and {member2.name} are now divorced."

    def marry_members(self, member1, member2):
        if not isinstance(member1, Member) or not isinstance(member2, Member):
            return "Both members must be valid Member instances."

        # Prevent self marriage
        if member1 is member2:
            return "A member cannot marry themselves."

        # Prevent marriage if deceased
        if not member1.is_alive or not member2.is_alive:
            return "Cannot marry a deceased member."

        # Prevent close-relative marriage
        if (
            member2 in member1.parents
            or member2 in member1.children
            or member2 in self.get_siblings(member1)
        ):
            return "Marriage is not allowed between close relatives."

        # check gender
        if member1.gender == member2.gender:
            return "Marriage requires a man and a woman."

        man = member1 if member1.gender == "m" else member2
        woman = member2 if man is member1 else member1

        # Account for cultural norms ( a maximum of 4 wives for a man and only 1 husband for a woman)
        if len(man.spouses) >= 4:
            return (
                f"{man.name} cannot marry {woman.name} because he already has 4 wives."
            )

        if len(woman.spouses) >= 1:
            return f"{woman.name} cannot marry {man.name} because she already has a husband."

        # Prevent duplicate marriages
        if woman in man.spouses:
            return f"{man.name} and {woman.name} are already married."

        man.add_spouse(woman)
        return f"{man.name} and {woman.name} are now married."
    
    def get_parents(self, member):
        return member.parents
    
    def get_couple_children(self, parent1, parent2):
        return [child for child in parent1.children if child in parent2.children]
    

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
        return None

    def get_uncles_aunts(self, member):
        uncles_aunts = set()
        for parent in member.parents:
            for sibling in self.get_siblings(parent):
                uncles_aunts.add(sibling)
        return list(uncles_aunts)

    def get_cousins(self, member):
        cousins = set()
        for uncle_aunt in self.get_uncles_aunts(member):
            for child in uncle_aunt.children:
                cousins.add(child)
        return list(cousins)

    def get_grandparents(self, member):
        grandparents = set()
        for parent in member.parents:
            for grandparent in parent.parents:
                grandparents.add(grandparent)
        return list(grandparents)

    def __str__(self):
        if not self.members:
            return "<No members in family tree>"

        lines = ["Family Tree Members:\n"]

        for m in self.members:
            lines.append(str(m))

            half_sibs = self.get_half_siblings(m)
            full_sibs = self.get_full_siblings(m)
            cousins = self.get_cousins(m)
            grandparents = self.get_grandparents(m)

            lines.append(
                f" Half siblings: {', '.join(f'{hs.name}({hs.age})' for hs in half_sibs) if half_sibs else 'None'}"
            )
            lines.append(
                f" Full siblings: {', '.join(f'{fs.name}({fs.age})' for fs in full_sibs) if full_sibs else 'None'}"
            )
            lines.append(
                f" Cousins: {', '.join(f'{c.name}({c.age})' for c in cousins) if cousins else 'None'}"
            )
            lines.append(
                f" Grandparents: {', '.join(f'{gp.name}({gp.age})' for gp in grandparents) if grandparents else 'None'}"
            )
            lines.append("-" * 40)
        return "\n".join(lines)


class Member:
    id_counter = 1

    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.children = []
        self.parents = []
        self.spouses = []  # all current spouses
        self.past_spouses = []  # Past spouses
        self.is_alive = True
        self.id = Member.id_counter
        Member.id_counter += 1

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

        return (
            f"{self.name} ({self.age}, {'Male' if self.gender=='m' else 'Female'})\n"
            f" Parents: {parents}\n"
            f" Spouse(s): {current_spouses}\n"
            f" Past spouses: {past_spouses}\n"
            f" Children: {children}\n"
        )
