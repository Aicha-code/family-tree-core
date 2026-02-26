from familyTree import FamilyTree


def ask(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value


def ask_gender(prompt):
    while True:
        gender = input(prompt).strip().lower()
        if gender in ("m", "f"):
            return gender
        print("Please enter 'm' or 'f'.")


def prompt_member(tree, label="member", gender=None):
    name = ask(f"Enter {label} name: ")
    age = ask(f"Enter {label} age: ")
    gender = gender or ask_gender(f"What is {name}'s gender? (m/f): ")
    return tree.create_member(name, age, gender)


def add_children(tree, parent1, parent2):
    while True:
        add_more = ask(
            f"Add a child for {parent1.name} and {parent2.name}? (y/n): "
        ).lower()

        if add_more != "y":
            break

        child = prompt_member(tree, "child")
        tree.add_parent_child_relationship(parent1, parent2, child)


def run_cli():
    tree = FamilyTree()

    print("\n*** Family Tree CLI***\n")

    # Create main member
    member = prompt_member(tree, "main member")

    # Parents
    print("\n--- Enter parent details ---")
    father = prompt_member(tree, "father", gender="m")
    mother = prompt_member(tree, "mother", gender="f")

    tree.add_parent_child_relationship(father, mother, member)

    status = ask(
        "Parents' relationship status: 1) Married 2) Divorced 3) None — choose 1/2/3: "
    )

    if status == "1":
        tree.marry_members(father, mother)
    elif status == "2":
        tree.marry_members(father, mother)
        tree.divorce_members(father, mother)

    # Current spouse
    if ask(f"\nIs {member.name} married? (y/n): ").lower() == "y":
        spouse = prompt_member(
            tree,
            "spouse",
            gender="f" if member.gender == "m" else "m",
        )

        tree.marry_members(member, spouse)
        add_children(tree, member, spouse)

    # Past spouses
    while ask(
        f"\nAdd a past spouse for {member.name}? (y/n): ",
        required=False,
    ).lower() == "y":

        past = prompt_member(
            tree,
            "past spouse",
            gender="f" if member.gender == "m" else "m",
        )

        tree.marry_members(member, past)
        tree.divorce_members(member, past)
        add_children(tree, member, past)

    # Final Output
    print("\n--- Member Summary ---")
    print(member)

    print("\n--- Full Family Tree ---")
    print(tree)


if __name__ == "__main__":
    run_cli()