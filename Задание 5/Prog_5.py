import random
class student():

  def __init__(self, ID, FirstName, LastName, Age):
    self.ID = ID
    self.FirstName = FirstName
    self.LastName = LastName
    self.Age = Age

  

Array = []
Names = ["Никита","Алексей","Александр","Сергей","Евгений","Олег","Федор","Николай","Генадий","Борис"]
LastNames = ["Куприянов","Говядин","Лисов","Баклажанов","Бананов","Кузнецов","Мавродев","Мигеев","Фадеев","Богеев","Логеев","Сидоров","Шарапов","Бездный","мЫшь"]

for i in range(100):
  Array.append(student(i+1,random.choice(Names),random.choice(LastNames),random.randint(17,26)))

for i in range(len(Array)):
  print(" | ",Array[i].ID," | \t",Array[i].FirstName,'  '," \t|\t\t ",Array[i].LastName,' \t '," \t| ",Array[i].Age," | ")

foundName = input('Имя?')
foundLastName = input('Фамилия?')
foundAge = input('Возраст?')
Array2 = Array.copy()
def MainFunc():
  count = len(Array2)*10
  countError = 0
  res = False
  while(res == False):
    for i in range(len(Array2)):
      if(foundName != ""):
        if(Array2[i].FirstName != foundName):
          del Array2[i]
          if(countError <= len(Array2)*100):
            countError += 1            
          else:
            return 0
          break
      if(foundLastName != ""):
        if(Array2[i].LastName != foundLastName):
          del Array2[i]
          if(countError <= len(Array2)*100):
            countError += 1      
          else:
            return 0
          break
      if(foundAge != ""):
        if(Array2[i].Age != int(foundAge)):
          del Array2[i]
          if(countError <= len(Array2)*100):
            countError += 1
          else:
            #del Array2[0]
            return 0
          break
      count-=1
      if(count == 0):
        res = True
  return Array2
  

Result = MainFunc()
print("\n")
if(isinstance(Result, list)):
  for i in range(len(Result)):
    print(" | ",Result[i].ID," | \t",Result[i].FirstName," \t\t|\t\t ",Result[i].LastName," \t\t| ",Result[i].Age," | ")
else:
  print("Такой пользователь не найден")
input()
