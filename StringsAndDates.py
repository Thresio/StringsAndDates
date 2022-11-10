#Zack Wilcox | CIS261 | StringsAndDates

class StringsAndDates():

    MonthsMaster = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    
    dateInput = ''

    while dateInput != '-1':

        print('Enter date:')
        dateInput = str(input())

        cutDate = dateInput.split(' ')

        if 0 < 1 < len(cutDate) and 0 < 2 < len(cutDate):

            if cutDate[1].find(',') == 2:

                temp = cutDate[1]
                cutDate[1] = temp.replace(',','')

                validMonth = False

                for i in range(12):
                    if cutDate[0] == MonthsMaster[i]:
                        validMonth = True
                        monthNumber = i + 1

                if validMonth == True:
                
                    dateFinal = str(monthNumber) + '/' + cutDate[1] + '/' + cutDate[2]
                    print(dateFinal)

                else:
                    print('Date entered is not valid')
            else:
                print('Date entered is not valid')
        else:
            if dateInput != '-1':
                print('Date entered is not valid')