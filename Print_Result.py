average_score = int(input('Enter your average score to print your result: '))

if average_score >= 0 and average_score <= 50:
    print('Fail')
elif  average_score <= 75:
    print('Second Class')
elif average_score <= 90:
    print('First Class')
elif average_score <= 100:
    print('Distinction')
else:
    print('Invalid Input')
