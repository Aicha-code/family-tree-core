from familyTree import FamilyTree

if __name__ == "__main__":
    tree = FamilyTree()

    print("Creating members...")

    ## First generation
    john = tree.create_member("John", 62, "m")
    mary = tree.create_member("Mary", 60, "f")
    tree.marry_members(john, mary)

    # Their children
    alice = tree.create_member("Alice", 35, "f")
    bob = tree.create_member("Bob", 33, "m")

    tree.add_parent_child_relationship(john, mary, alice)
    tree.add_parent_child_relationship(john, mary, bob)

    ## Alice's first marriage
    david = tree.create_member("David", 36, "m")
    tree.marry_members(david, alice)

    emma = tree.create_member("Emma", 10, "f")
    liam = tree.create_member("Liam", 8, "m")

    tree.add_parent_child_relationship(david, alice, emma)
    tree.add_parent_child_relationship(david, alice, liam)

    ## Divorce (past spouse scenario)
    tree.divorce_members(david, alice)

    # Alice remarries
    mark = tree.create_member("Mark", 40, "m")
    tree.marry_members(mark, alice)

    # Child from second marriage
    sophia = tree.create_member("Sophia", 3, "f")
    tree.add_parent_child_relationship(mark, alice, sophia)

    ## Bob's family
    clara = tree.create_member("Clara", 31, "f")
    tree.marry_members(bob, clara)

    noah = tree.create_member("Noah", 6, "m")
    tree.add_parent_child_relationship(bob, clara, noah)

    # Output the family tree and test relationships    
    print("\n--- Family Tree ---")
    print(tree)

    print("\n--- Testing Relationships ---")

    print(f"\nTest member: {alice.name}({alice.age})\n")

    print(f"Alice's parents: {[f'{parent.name}({parent.age})' for parent in alice.parents]}")

    print(
        f"Alice's current spouse: "
        f"{[f'{spouse.name}({spouse.age})' for spouse in alice.spouses]}"
    )

    print(
        f"Alice's past spouses: "
        f"{[f'{spouse.name}({spouse.age})' for spouse in getattr(alice, 'past_spouses', [])]}"
    )

    print(f"Alice's children: {[f'{child.name}({child.age})' for child in alice.children]}")

    print(f"Bob's siblings: {[f'{sibling.name}({sibling.age})' for sibling in tree.get_siblings(bob)]}")

    print(
        f"Emma's siblings: "
        f"{[f'{sibling.name}({sibling.age})' for sibling in tree.get_full_siblings(emma)]}"
    )

    print(
        f"Sophia's full siblings: "
        f"{[f'{sibling.name}({sibling.age})' for sibling in tree.get_full_siblings(sophia)]}"
    )

    print(
        f"Emma and Liam's half-siblings: "
        f"{[f'{half_sibling.name}({half_sibling.age})' for half_sibling in tree.get_half_siblings(emma)]}"
    )
    print(
        f"Emma and Liam's grandparents: "
        f"{[f'{grandparent.name}({grandparent.age})' for grandparent in tree.get_grandparents(emma)]}"
    )


    print(
        f"Emma's aunts and uncles: "
        f"{[f'{aunt_uncle.name}({aunt_uncle.age})' for aunt_uncle in tree.get_uncles_aunts(emma)]}"
    )

    print(
        f"Emma and Liam's cousins: "
        f"{[f'{cousin.name}({cousin.age})' for cousin in tree.get_cousins(emma)]}"
    )