### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # need to use == for comparison
      return True
    else  # colon : required at end of else statement
      return False
   

  dif highest_card(self, card1 card2):  # dif should be def.  Also comma needed between parameters card1 and card2.
  if card1.value > card2.value:  # whole if block needs indented inwards.
    return card  # card does not exist - should be card1
  else:
    return card2
  


def cards_total(self, cards):
  total  # variable should be assigned a starting value like 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  # incorrect indentation.  This will return after first loop.  Move return indentation back to line underneath the for statement.  Wrap total within a str() function.
  
```
