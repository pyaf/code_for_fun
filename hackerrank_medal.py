print("Enter the rank/total no. of participants: (ex: 432/5678)")
rank, total_number_of_participants = list(map(int, input().strip().split('/')))

gold = 0.04 * total_number_of_participants

silver = gold + 0.08 * total_number_of_participants

bronze = gold + silver + .13 * total_number_of_participants

if rank <= gold:
    print("\n\nGOLD!!!")
    print("Ab to party hai BC\n\n")
elif rank <= silver:
    print("\n\nSILVER!! \n\n")
    print("Nobody remembers silver ppl :P\n\n")
elif rank <= bronze:
    print("\n\nBRONZE \n\n")
    print("Ja jile apni zindagi\n\n")
else:
    print("\n\nMu mat dikha BC\n\n")

print("Gold: below %d rank" %(gold))
print("Silver: below %d rank" %(silver))
print("Bronze: below %d rank" %(bronze))
