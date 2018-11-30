class Underscore:
  def map(self, li, callback):
    result = []
    for value in li:
      result.append(callback(value))
    return result

_ = Underscore()

my_list = [1, 2, 3, 4]
doubles = _.map(my_list, lambda x: x*2)
print(my_list)
print(doubles)