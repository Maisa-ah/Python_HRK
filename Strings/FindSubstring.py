def count_substring(string, sub_string):
  check = 0
  while sub_string in string:
    check+=1
    i = string.find(sub_string)
    string = string[:i] + string[i+1:]
  return check

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
  
  count = count_substring(string, sub_string)
  print(count)