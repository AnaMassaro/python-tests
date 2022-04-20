import requests

class People:
  def __init__(self, name, last_name):
    self.name = name
    self.last_name = last_name
    self.data = False

  def get_all_data(self):
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')

    if response.ok:
      self.data = True
      return 'CONNECTED'
    else:
      self.data = False
      return 'ERROR 404'