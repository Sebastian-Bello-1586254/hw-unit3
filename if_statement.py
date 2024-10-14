'''
2024-10-14
1586254
title = Project unit 3
'''

# imports

'''
Student activity 1:
It is commonly said that one human year is equivalent to 7 dog years,
However, this simple conversion fails to recognize that dogs reach 
adulthood in approximately 2 years. 
As a result, some people believe that it is better to count each of the 
first 2 human years ad 10.5 dog years, and then count each additional 
human year a 4 dog year.
Write a program that implements the conversion from human years to 
dog years described. Ensure your program works correctly.
Should a negative value be input, the program should advise user of the
issue.
'''
print('==============Student Activity 1====================')
hAge = int(input('How old is your dog in human years approximately? '))
if hAge <=0:
    print('Negative values are not accepted')  
elif hAge >= 2:
    dAge= (10.5*2)
    hAge = hAge - 2
    dAge = dAge + hAge * 4
    print(f'Your dogs is {dAge} years old.')
else:
    print('Your dog is 10.5 dog years old')
    

    
   
   
        
'''
Student activity 2:
Chinese Zodiac assigns animals to years in a 12-year cycle.
One 12 year cycle is shown in the 
link = https://www.chinahighlights.com/travelguide/chinese-zodiac/
The pattern repeats periodically.
Write a program that reads a year from the user and displays the animal
associated with that year.
The program should work with a year greater than zero.
'''

print('==============Student Activity 2====================')
        

'''
Student activity 3:
The length of a month varies from 28-31 days. Create a program which
reads the name of a month from user as a string, then your program 
should display the number of days in that month.
Display "28 or 29 days" for February.
https://c.tadst.com/gfx/1200x675/calendar-2024-printable.png?1
'''   
print('==============Student Activity 3====================')
month = str(input('Enter a month (in lowercase): '))
if month in ('january', 'march', 'may', 'july', 'august', 'october', 'december'):
    print('31 days in this month')
elif month in ('april', 'june', 'september', 'november'):
    print('30 days in this month') 
else:
    print('February has 28 or 29 days depending on the year')
'''
Student activity 4:
Write program that reads a month and day from the user. If the month
and day match one of the holidays listed, then your program should display the 
holiday's name. Otherwise, the program should indicate that the entered holiday
does not correspond to a fixed-date holiday.
https://www.commerce.gov/hr/employees/leave/holidays
'''
print('==============Student Activity 4====================')       
day = str(input('Enter a month then day in lower case (ex. january 1): '))
if day == 'january 1':
    print('New Year\'s Day')
elif day == 'june 19':
    print('Juneteenth National Independence Day')
elif day == 'july 4':
    print('Independence Day')
elif day == 'november 11':
    print('Veterans\' day')
elif day == 'december 25':
    print('Christmas Day')
else:
    print('The following holidays are federal holidays but do not fall on a specific date \nMLK day, Washington\'s Birthday, Memorial Day, Labor Day, \nColumbus Day, and Thanksgiving Day.')       
'''
activity 5:
Make a program which asks students in elementary school
5 multiple choice questions, checks how many the student 
got right.
1-shows the total of questions correctly answered
2-Provides a percent grade
3-Make two of the questions have 2 answers providing
  1/2 point for every correct choice.

'''
print('==============Student Activity 5====================')               
        
'''
Student activity 6:
Write a program which asks the user to enter his or her month and day of 
birth. Then, your program should report the user's zodiac sign as part of an
appropriate output message.
https://www.shape.com/lifestyle/mind-and-body/zodiac-signs-meanings-dates         
        
'''       
print('==============Student Activity 6====================')
