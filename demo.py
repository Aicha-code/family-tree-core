# this is the main demo file
from familyTree import member
#demos to be added here
if __name__ == "__main__":
    member1 = member("Alice", 30)
    print(f"test member created: {member1.name}({member1.age})")
    member2 = member("Bob", 32)
    member1.add_spouse(member2)
    print(f"{member1.name} is married to {member1.spouse.name}({member1.spouse.age})")
    parent1 = member("Charlie", 60)
    parent2 = member("Diana", 58)
    parent1.add_spouse(parent2)
    member1.add_parent(parent1)
    member1.add_parent(parent2)
    print(f"{member1.name}'s parents are: {', '.join([f'{p.name}({p.age})' for p in member1.get_parents()])}")
    child1 = member("Eve", 5)
    child2 = member("Frank", 3)
    member1.add_child(child1)
    member1.add_child(child2)
    print(f"{member1.name}'s children are: {', '.join([f'{c.name}({c.age})' for c in member1.children])}")
    print(f"{child1.name}'s siblings are: {', '.join([f'{s.name}({s.age})' for s in child1.get_siblings()])}")
    # print("\nFull member details:")