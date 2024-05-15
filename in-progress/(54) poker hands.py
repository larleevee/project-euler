def initialise() -> list:
  '''
  WORKS
  turns the text file into a 4-dimensional array
  '''
  with open('hands.txt') as f:
    games = f.read()

  twoHands = games.strip().split('\n') #list consisting of all hands per game
  hands = [] #individual hands per player per game

  for game in twoHands:
    firstHand = cardsToLists(game[:14])
    secondHand = cardsToLists(game[15:])
    hands.append([firstHand, secondHand])
  
  return hands


def cardsToLists(playerHand) -> list: #whole players hand as one str block
  '''
  WORKS
  turns a player's hand into two embedded lists, one with value, one with suites
  8C TS KC 9H 4S =-> [[8, T, K, 9, 4],[C, S, K, H, S]]
  '''

  cards = playerHand.split(' ')
  cardValue = []
  cardSuite = []
  focusCard = ''

  for i in range(0, 4+1):
    focusCard = cards[i]
    cardValue.append(focusCard[0])
    cardSuite.append(focusCard[1])
    
  return ([cardValue, cardSuite])

hands = initialise()