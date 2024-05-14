from faker import Faker
import sys

fake = Faker()


args = sys.argv[1:]
if len(args) == 1:
    output_filename = args[0]

    persons = []
    for _ in range(0, 20):
        p = {"firstname": fake.first_name(), "lastname": fake.last_name()}
        persons.append(p)

    persons = iter(persons)

    data = [f"{p['firstname']} {p['lastname']}" for p in persons]
    data = ", ".join(data) + ", "

    with open(output_filename, "a") as f:
        f.write(data)
else:
    print("You need to pass the output filepath!")
