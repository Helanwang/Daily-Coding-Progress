list1 = [37, 84, 22, 95, 48, 13, 79, 53, 61, 7]
# says: if x divided by 2 the reminder is 0, then is an even number
# confused about modulus, then handwrite the division function on paper.
evens = [x for x in list1 if x % 2 == 0]  # % modulus in here means when there is no reminder when division occurred.
print(evens)


