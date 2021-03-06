#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
  read [item]
  q to quit
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster'
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'north' : 'Secret Room',
                  'item'  : 'potion',
                  'item'  : 'clue',
                  'broken': 'false'
                },
            'Garden'  : {
                  'north' : 'Dining Room',
                  'item'  : 'sledge hammer'
                },
            'Secret Room' : {
                  'south' : 'Dining Room',
                  'item'  : 'treasure'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    # check for broken wall
    if rooms[currentRoom] == 'Dining Room' and 'broken' in rooms[currentRoom] == 'false':
        print('ok')
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]

    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  ## if they type read
  if move[0] == 'read' :
      if move[1] in inventory :
      #display a helpful message
        print('Use a tool to break a wall')
      
      #otherwise, if the item isn't there to get
      else:
        #tell them they can't get it
        print('Nothing to Read')

  ## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster just attacked you!')
    if 'potion' in inventory:
        print('Use potion to heal or fight back')
        #if move[0]


  ## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'clue' in rooms[currentRoom]['item']:
    print('There is treasure near by')

  ## soft wall in Dining room
  if rooms[currentRoom] == 'Dining Room' :
      if move[1] == 'north':
          print('This wall seems weak')
    



