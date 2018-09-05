def is_valid(x):
  x = x.split(".")
  print x
  for i in x:
    print len(i)
    if len(i) > 3 or len(i) < 1:
      print "x"
      return False

    if int(i) > 255 or int(i) < 0:
      print "xx"
      return False

    if int(i[0]) == 0 and len(i) > 1:
      print "xxx"
      return False

  return True


def main():
  ipAdd = raw_input()
  result = is_valid(ipAdd)
  if result == True:
    print('valid ip')
  else:
    print('not valid ip')


if __name__ == '__main__':
  main()
