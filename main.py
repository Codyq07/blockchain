#calls the main function
def main():
  #imports all the modules needed
  import hashlib  
  from time import time
  from pprint import pprint
  import random
  import os
  #lets you login and if you arent registered then you will be prompted to create a new user
  def login_block():
    check = 0
    f = open('logins.txt', 'r')
    fw = open("logins.txt", "a")
    lines = f.readlines()
    f.close()
    global users
    users = {}
    for line in lines:
      entry = line.split()
      username = entry[0]
      password = entry[1]
      users[username] = password
  
      
    while check == 0: 
      userinp = input("Enter your username: ")
      passinp = input("Enter your password: ")
      if userinp in users:
        if users[userinp] == passinp:
          print("Hey", userinp)
          check = 1
        else:
          check = 0
          print("Your password is incorect please try again")
          
  
      else:
        print("That username is not in the file")
        add = input("Would you like to add a new account: (Y/N): ")
        if (add == "Y") or (add == "y"):
          global newuser
          newuser = userinp
          newpass = passinp
          two = newuser + " " + newpass
          fw.write("\n" + two)
          newuserfm = open(newuser + "money.txt", "w")
        
          newuserfm.write("0")
          newuserfh = open(newuser + "hold.txt","w")
          newuserfh.write("0")
          
          global sender
          sender = newuser
          check = 1
          fw.close()
    sender = userinp
    

  

   #calls the login function
  login_block()
 
   #sets variables for the menu options
  
  SEND = 1
  SHOWBLOCKS = 2
  SELL = 3
  BUY = 4
  GAMBLE = 5
  CHECKBALANCE = 6
  QUIT = 7

  #opens the registered user files
  #also checks to make sure the file is empty if this wasn't here the program would break if the file is empty
  holdi = open(sender + "hold.txt", "r")
  hold = holdi.readline()
  if os.path.getsize(sender + 'hold.txt') == 0:
    hold = 0
  hold = int(hold)
  holdi.close()
  
 
  #I had to arrange the code in this order or else it erases the file content
  mone = open(sender + "money.txt","r")
  
  mon = mone.readline()
  if os.path.getsize(sender + 'money.txt') == 0:
    mon = 0
  moni = open(sender + "money.txt", "w")
  again = "y"
  # i got this from pythonhow https://pythonhow.com/how/check-if-a-text-file-is-empty/
  #it checks to see if the file is empty
  
  
  
 
  money = float(mon)
                
  


  
 






  #This is the blockchain code this runs the hashing and the validation
  #most of this code i got from a website(website unknown)
  #however i had to edit a good bit of this to make it runnable
  class blockchain():
      def __init__(self):
          self.blocks = []
          self.__secret = ''
          self.__difficulty = 4 
          # guessing the nonce
          i = 0
          secret_string = '/*SECRET*/'
          #This is where it creates the hash
          while True:
              _hash = hashlib.sha256(str(secret_string+str(i)).encode('utf-8')).hexdigest()
              if(_hash[:self.__difficulty] == '0'*self.__difficulty):
                  self.__secret = _hash
                  break
              i+=1
       #function to create the block and sees the information
      def create_block(self, sender:str, information:str, reviver):
          block = {
              'index': len(self.blocks),
              'sender': sender,
              'timestamp': time(),
              'Message': information,
              "Reciver" : reviver
          }
          
          
          if(block['index'] == 0): block['previous_hash'] = self.__secret # for genesis block
          else: block['previous_hash'] = self.blocks[-1]['hash']
          # guessing the nonce
          i = 0
          while True:
              block['nonce'] = i
              _hash = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
              if(_hash[:self.__difficulty] == '0'*self.__difficulty):
                  block['hash'] = _hash
                  break
              i+=1
          self.blocks.append(block)
        #opens the blockhistory
          f = open("blockhistory.txt", "a")
          bloc = str(block)
          
          f.write(f"{bloc}\n")
          #validates the block
      def validate_blockchain(self):
          valid = True
          n = len(self.blocks)-1
          i = 0
          while(i<n):
              if(self.blocks[i]['hash'] != self.blocks[i+1]['previous_hash']):
                  valid = False
                  break
              i+=1
          if valid: print('The blockchain is valid...')
          else: print('The blockchain is not valid...')
      def show_blockchain(self):
          f = open("blockhistory.txt", "w")
          
          for block in self.blocks: 
              pprint(block)
              
              
              
              print()
  #i got lazy and didnt want to type blockchain() everytime so i set it to b
  b = blockchain()
  









  
  #creats a while loop to keep it going
  while (again == "y") or (again == "Y"):
    
     #creates a menu
    print("")
    print("           MENU            ")
    print("---------------------------")
    print("Send a block - 1")
    print("Show block history - 2")
    print("Sell - 3")
    print("Buy - 4")
    print("Gamble - 5")
    print("Check your balance - 6")
    print("Quit - 7")
    print("WARNING: If you stop the program without selecting Quit you will lose your progress.")
    print()
    #gets the option number
    opt = input("Enter option number: ")
    try:
      opt = int(opt)
    except ValueError:
      print("That is not on the menu please try again.")
    f = open("blockhistory.txt", "r")
    
    
    
    #creates the send block
    if opt == SEND:
      
      revive = input("Enter who you want to send the block too: ")
      if revive != sender:
        if revive in users:
          holder = open(revive + "hold.txt", "r")
          g = holder.readline()
          hold = int(g)
          hold = hold + 10
          holderw = open(revive + "hold.txt", "w")
          holderw.write(str(hold))
          holder.close()
          holderw.close()
      message = input("Enter the message you want to include: ")
      
      b.create_block(sender, message, revive)
      
      
      sender.lower()
      revive.lower()
      if sender == revive:
        hold = hold + 10
    
    if opt == SHOWBLOCKS:
      fr = open("blockhistory.txt", "r")
      
      read = fr.read()
      print(read)
      fr.close()
      #the sell part
    if opt == SELL:
      print(f"You have {hold} coins")
      print("One coin is $5")
      print("To get more coins send blocks to yourself")
      sell = input("Enter Y/N: ")
      if sell == "Y" or sell == "y":
        money = hold * 5
        hold = 0
        print(f"You have ${money}")
        
      else:
        continue
      #lets you check the balance
    if opt == CHECKBALANCE:
        print(f"Your balance is ${money:.2f}")
        print(f"You are holding {hold:.2f} coins")
    #lets you buy different coins
    if opt == BUY:
      print("Option 1: Offbrand Bitcoin = $5 per coin")
      print("Option 2: Vio = $10 per coin")
      print("Option 3: Peak = $15 per coin")
      print("What do you want to swap to?")
      swap = int(input("Enter the option number: "))
      if swap == 1:
        hold = money / 5
        money = 0
        print(f"You have ${money}")
        print(f"You have {hold:.2f} Offbrand Bitcoin")
      elif swap == 2:
        hold = money / 10
        money = 0
        print(f"You have ${money}")
        print(f"You have {hold:.2f} Vio")
      elif swap == 3:
        hold = money / 15
        money = 0
        print(f"You have ${money}")
        print(f"You have {hold:.2f} Peak")
      #gambling ;)
    if opt == GAMBLE:
      print("Do you want to gamble")
      print("WARNING: You may lose money")
      inv = input("Y/N: ")
      if (inv == "Y") or (inv == "y"):
        winlose = ["Win", "Lose"]
        
        result = random.choice(winlose)
        
        if result == "Win":
          print("You Won!!")
          money = money * 1.5
          print(f"Your balance is {money: .2f}")

        if result == "Lose":
          print("You lost.")
          money = money *.75
          print(f"Your balance is {money: .2f}")
      if (inv != "y") or (inv != "Y"):
        continue
      #closes the program
    if opt == QUIT:
      
      again = "n"
      holder = open(sender + "hold.txt", "w")
      holder.write(str(hold))
      holder.close()
      
      money = str(money)
      moni.write(money)
      moni.close()
    #had to create a try statment because if there was a letter in the input it would throw an error
    try:
      if opt >= 8:
        print("That is not on the menu please try again.")
    except:
      continue
    
  f.close()
  moni.close()
  mone.close()
  
    
main()