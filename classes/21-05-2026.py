# person_details = function name
# name, age, loation = parameters
# person_details('mouse', 19, 'guntur') = function calling
# mouse', 19, 'guntur' = arguments
# line 7 to 14 = function definition
# line 8 to 14 = function body

def driver_licesnse(name, age, location):
    print('Hi ' + name)

    if age > 18 and location == 'guntur':
        print('You are eligible for drivers license')
    else:
        print('You are not eligible')

    return 'hi'


if 'hi' == None:
    print('Nothing is returning')
else:
    print("It retuened something")


#
# driver_licesnse('cat', 16, 'pune')
# driver_licesnse('dog', 14, 'hyderabad')
# driver_licesnse('beetle', 22, 'newyork')
# driver_licesnse('frog', 10, 'guntur')
