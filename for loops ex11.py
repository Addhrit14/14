negative = input('how many negatives did you get:')
negative = int(negative)
if negative==1:
  for i in range(10):
    print('prompt')
elif negative==2:
  for i in range(50):
    print('reminder')
elif negative==3:
  for i in range(100):
    print('warning')
else:
  for i in range(100):
    print('removal')