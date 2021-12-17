suit = ("diamonds", "clubs", "hearts", "spades")#tuple suit
card_number=tuple("A")+tuple(i for i in range(2,11)) +("J","Q","K")#tuple of values
card=(str(s)+" "+i for i in suit for s in card_number)
card=iter(card)#iteration of the result
while True:
  print (next(card))