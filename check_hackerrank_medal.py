rank = int(input("Enter the rank: ").strip())
total_number_of_participants = int(input("Enter the number of participants: ").strip())

gold = 0.04 * total_number_of_participants

silver = gold + 0.08 * total_number_of_participants

bronze = gold + silver + .13 * total_number_of_participants

if rank <= gold:
    print("\n \n GOLD!!!")
    print("Ab to party hai BC\n\n")
elif rank <= silver:
    print("\n\n SILVER!! \n\n")
    print("Nobody remembers silver ppl :P\n\n")
elif rank <= bronze:
    print("\n\n BRONZE \n\n")
    print("Ja jile apni zindagi\n\n")
else:
    print("\n\nMu mat dikha BC\n\n")
