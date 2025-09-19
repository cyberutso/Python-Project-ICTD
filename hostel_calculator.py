#take input for the rent
hostel_rent=int(input("Enter your hostel rent: "))
#take input for food order
food_order=int(input("Enter the amount of your food: "))
#take input for electricity spend
electricity_spend=int(input("Enter the total of electricity spend: "))
#per unit cost
per_unit_cost=int(input("Enter the charge per unit:"))
#input the number of person
per_person=int(input("Enter the number of person living in the hostel:"))
#cost for electricity
total_cost_electricity= electricity_spend*per_unit_cost
output=(hostel_rent + food_order + total_cost_electricity)// per_person
print("You Have to pay:",output)