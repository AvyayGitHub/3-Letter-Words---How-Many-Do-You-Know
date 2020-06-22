words = []

game = "play"

while game == "play":

  new = input("Enter A 3-Letter Word. ")

  if len(new) > 3 or len(new) < 3:
    print("That Is Not A Three Letter Word. ")
    print("You Know" , len(words), "Three Letter Words")
    game = "over"
  
  else:
    
    if new in words:
      game = "over"
      print("Game Over!!!")
      print("You Know," , len(words), "Three Letter Words")
    
    else:
      print("Nice One!")
      words.append(new)
