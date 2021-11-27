class Bot:

  def __init__(self, prefix, data):

    self.prefix = prefix
    self.data = list(data.split(' '))
    self.processData(self.data)

  def processData(self, data):

    try:

      if data[0][0] is self.prefix:
        
        for i in commands[0:]:

          if i == data[0].replace(self.prefix, ''):
            
            executeCommands.append(i)

    except:
      
      pass

nickname = 'Guest'
commands = ['nickname']
executeCommands = []

while True:

  data = input(f'[{nickname}]: ').lower().strip()
  
  BOT('/', data)
