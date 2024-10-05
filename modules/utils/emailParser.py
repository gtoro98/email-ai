

def returnRowsDict(body):
  bodyFields = body.split('\n')
  dict = {}
  for field in bodyFields:
    print('Field: ', field)
    fieldArray = field.split(':')
    if(len(fieldArray) == 2):
      print('Array: ', fieldArray)
      dict[fieldArray[0]] = fieldArray[1]
  return dict
