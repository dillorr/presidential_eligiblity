from datetime import date
from datetime import datetime


# quick formula to calculate age today from birth date
def calculate_age_today(birth_date):
    birth_date = datetime.strptime(birth_date, '%m/%d/%Y')
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


# define formula to calculate age on specified day with birth date
def calculate_age(birth_date, target_date):
    birth_date = datetime.strptime(birth_date, '%m/%d/%Y')
    target_date = datetime.strptime(target_date, '%m/%d/%Y')
    return target_date.year - birth_date.year - ((target_date.month, target_date.day) < (birth_date.month, birth_date.day))


# quick function to determine eligibility today
def president_eligible_today(birth_date):
    if calculate_age_today(birth_date) >= 35:
        return True
    else:
        return False


# determine eligibility to run on specified date
def president_eligible(birth_date, target_date):
    if calculate_age(birth_date, target_date) >= 35:
        return True
    else:
        return False


# create person class that contains name and date of birth
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.age = calculate_age_today(dob)


# create person named Dillon
dillon = Person('Dillon Orr', '11/23/1993')

print('Name:', dillon.name)
print('DOB:', dillon.dob)
print('Age:', dillon.age)

# create list of elections until 2099
year_list = [*range(2020, 2100)]

# get list of elections and add 1 to get actual inaugration years
inauguration_years = [(x + 1) for x in year_list if x % 4 == 0]

# choose common inauguration dat
inauguration_day = '1/20'

# add 1/20 to inauguration years
inauguration_dates = [(inauguration_day + '/' + str(x)) for x in inauguration_years]

# initialize lists
years_list = []
eligibility_list = []

# create 2 lists, one with only election years, and one with booleans reflecting eligibility per item
for x in inauguration_dates:
    years_list.append(datetime.strptime(x, '%m/%d/%Y').year-1)
    eligibility_list.append(president_eligible(dillon.dob, x))

# iterate through and create list of years eligible
eligible_years = [i for i, j in zip(years_list, eligibility_list) if j]

# if eligible now, else print when eligible
if president_eligible_today(dillon.dob):
    print('Eligible to run for president today.')
else:
    print('Eligible to run for president in the {} election.'.format(min(eligible_years)))
