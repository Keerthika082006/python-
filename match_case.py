#match-case statement(switch)=an alternative to using elif statements
#                               executive some code if a value matches a 'case'
#                               benifits: cleaner and syntax is more readable
'''
def week(day):
    match day:
        case 1:
            return "its sunday"
        case 2:
            return "its monday"
        case 3:
            return "its tuesday"
        case 4:
            return "its wednesday"
        case 5:
            return "its thursday"
        case 6:
            return "its friday"
        case 7:
            return "its saturday"
        case _:
            return "not a valid day"
print(week(8))
'''
'''
def is_weekend(day):
    match day:
        case "sunday":
            return True
        case " monday":
            return False
        case " tuesday":
            return False
        case " wednesday":
            return False
        case "thursday":
            return False
        case " friday":
            return False
        case" saturday":
            return True
        case _:
            return False
print(is_weekend("sunday"))
'''
def is_weekend(day):
    match day:
        case "sunday"|" saturday":
            return True
        case " monday"|" tuesday"|" wednesday"|"thursday"|" friday":
            return False
        case _:
            return False
print(is_weekend("sunday"))

