my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

my_partner_expenses = {
    "Hotel": 100,
    "Food": 900,
    "Transportation": 600,
    "Attraction": 400,
    "Miscellaneous": 150
}
my_total_expenses = sum(my_expenses.values())
my_partner_expenses = sum(my_partner_expenses.values())
print("My total expenses is ", my_total_expenses)
print("My partner's expenses is ", my_partner_expenses)

if my_total_expenses > my_partner_expenses:
    print("I spent more")

elif my_total_expenses < my_partner_expenses:
    print("My partner partner spent more")
else:
    print("We spent the same amount")

for category in my_expenses:
    if my_expenses[category] > my_partner_expenses[category]:
        print("I spent more on", category,
              "by", my_expenses[category]-my_partner_expenses[category])



