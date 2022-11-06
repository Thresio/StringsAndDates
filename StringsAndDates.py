#Zack Wilcox | CIS261 | StringsAndDates

class StringsAndDates():

    MonthsMaster = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

    print('Enter a date:')
    dateInput = str(input())

    cutDate = dateInput.split(' ')

    if cutDate[1].find(',') == False:
        errorMessage()

    temp = cutDate[1]
    cutDate[1] = temp.replace(',','')
    print(cutDate[1])

    validMonth = False

    for i in range(11):
        if cutDate[0] == MonthsMaster[i]:
            validMonth = True

    print(validMonth)

def errorMessage():
    print('Please input the date exactly as shown: \nMonth Day, Year (Ex. March 31, 2021)')