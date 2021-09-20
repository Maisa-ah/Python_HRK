if __name__ == '__main__':
  students = []
  low_score = 10000
  second_low = 10000
  for i in range(int(input())):
    name = input()
    score = float(input())        
    students.append([name, score])
    if score < low_score:
      second_low = low_score
      low_score = score
    if score < second_low and score != low_score:
      second_low = score
  students.sort(key=lambda x: x[0])
  for el in students:
    if el[1]==second_low:
        print(el[0])
