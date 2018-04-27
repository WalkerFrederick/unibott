import random
message = raw_input("type input here:")
if message[0] == '/' and message[1] == '/':
     commandArray = message.replace('/', '').split();
     if commandArray[0] == 'roll':
          #roll a dice, min val 1, max specified in command.
          print(random.randint(1,int(commandArray[1])));
     elif commandArray[0] == 'ping':
          #prints pong.
          print('pong!');
     elif commandArray[0] == 'ping':
          #prints pong.
          print('pong!');
else:
     print("not a command")
