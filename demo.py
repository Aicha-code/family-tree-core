# this is the main demo file
from familyTree import FamilyTree

# demos to be added here
if __name__ == "__main__":
    tree = FamilyTree()

    # Create members using the FamilyTree factory
    alice = tree.create_member("Alice", 30, "f")
    bob = tree.create_member("Bob", 32, "m")
    print(f"test members created: {alice.name}({alice.age}) and {bob.name}({bob.age})")

    # marry with man first (FamilyTree expects man then woman)
    print(tree.marry_members(bob, alice))
    
    parent1 = tree.create_member("Charlie", 60, "m")
    parent2 = tree.create_member("Diana", 58, "f")
    tree.add_parent_child_relationship(parent1, parent2, alice)
    print(f"{alice.name}'s parents are: {', '.join([f'{p.name}({p.age})' for p in alice.get_parents()])}")
    # Add parents for Alice via the tree helper


    child1 = tree.create_member("Eve", 5, "f")
    child2 = tree.create_member("Frank", 3, "m")
    # Add children using the FamilyTree helper (ensure man is passed first)
    tree.add_parent_child_relationship(bob, alice, child1) if bob.gender == "m" else tree.add_parent_child_relationship(alice, bob, child1)
    tree.add_parent_child_relationship(bob, alice, child2) if bob.gender == "m" else tree.add_parent_child_relationship(alice, bob, child2)

    print(f"{alice.name}'s children are: {', '.join([f'{c.name}({c.age})' for c in alice.children])}")
    print(f"{child1.name}'s siblings are: {', '.join([f'{s.name}({s.age})' for s in child1.get_siblings()])}")
    # print("\nFull member details:")