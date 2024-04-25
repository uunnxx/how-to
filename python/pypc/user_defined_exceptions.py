class VotersElligibility(Exception):
    def __init__(self):
        super()

def age_check(age: int):
    try:
        if age < 18:
            raise VotersElligibility
    except VotersElligibility:
        print('Age is less than 18')
    else:
        print('Age is greater than or equal to 18')


age_check(12)
age_check(21)
