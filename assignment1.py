import time
'''
Unit_conversion_machine_v3.0

Made by: Johnny Doan (obsessed with cats)
Short program made by none other than meeeeeee! ^.^ meow? <(^o.o^)>
Basically it ask for the distance of each runner in different units
then converts them to 3 results. The second runner in cm, distance
distance between the two and distance in km m cm.

Last revised: May 28 2016 5:41 PM

Time spent(hrs): about 1 hr (15 minute thinking/reading and 45 minute
writing and decorating :P)
'''
#========================AWESOME INTRO!! :D :3=================================
print('''Welcome everyone to the one-legged race. Each runner\'s results are \
posted here:\n''')
print('''(result1) Runner 1 ran 1km, 1m, 1cm. While runner 2 ran 1mi, 1yrd, 1ft. \
\n(result2) Runner 1 ran 0km, 0m, 1cm. While runner 2 ran 0mi, 0yrd, 1ft. \
\n(result3) Runner 1 ran 10km, 10m, 10cm. While runner 2 ran 1mi, 1yrd, 1ft\n''')
print('''runner 1 (result1) all in cm: 100101.00 cm\
\nrunner 1 (result2) all in cm: 1.00 cm\
\nrunner 1 (result3) all in cm: 1001010.00 cm\n''')
print('''We are going to use my machine to mash numbers together. kinda like a \
mini broken calculater except there\'s a kitty doing the work :3.\nAnyways, \
feel free to use those results in the machine or make up your own! :D\n''')
print('					MOST IMPORTANTLY HAVE FUN!!!!!\n')

#========================HELLO HOW ARE MEW? (ASKING THE USER)==================
runner_one_km = int(input('How far did the first runner travel in kilometers?'))
runner_one_m = int(input('How far did the first runner travel in meters?'))
runner_one_cm = int(input('How far did the first runner travel in centimeters?'))
runner_two_mi = int(input('How far did the second runner travel in miles?'))
runner_two_yrd = int(input('How far did the second runner travel in yards?'))
runner_two_ft = int(input('How far did the second runner travel in feets?'))

#========================CALCULATING BEEP BOOP BOP O.O=========================
# calc_one converts runner 2 to cm
calc_one = ((runner_two_mi * 1760 + runner_two_yrd) * 3 + runner_two_ft) * 30.48
calc_two = (runner_one_km * 1000 + runner_one_m) * 100 + runner_one_cm        # calc_two converts runner 1 to cm
distance = abs(calc_one - calc_two)       # absolute function to calculate distance between the the runners in cm
convert_m = distance // 100     # converts the result of distance to meters
remain_cm = distance % 100      # remainder is the centimeters
convert_km = convert_m // 1000      # converting meters to km
remain_m = convert_m % 1000     # remainder will be in meters
integer_km = int(convert_km)     # integer_ converting from float to integer
integer_m = int(remain_m)
integer_cm = int(remain_cm)
#========================PRINTING MEOW MEOW :3=================================
print('''\n==================MEOW! MEOW! (^=._.=^) PLEASE WAIT WHILE CODE \
KITTY CALCULATES...========================''')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(2)
print('.')
time.sleep(1)
print('TRACE paw: runner 1 all in cm is: {:.2f} cm\n'.format(calc_two))
print('==================FIRST RESULT==========================')
print('Runner 2 ran {:.2f} cm.\n'.format(calc_one))
print('==================SECOND RESULT=========================')
print('The distance between the two covered is {:.2f} cm.\n'.format(distance))
print('==================THIRD RESULT==========================')
print('The difference in another form: {:d} km, {:d} m and {:d} cm.\n\n\n'.format(integer_km, integer_m, integer_cm))
print('CODE KITTY getting sleepy.. powering down')
time.sleep(3)
print('.')
time.sleep(3)
print('.')
time.sleep(3)
print('.')
print('''(^=-.-=^)\nThat\'s the end of the program, \
let code kitty rest for a bit and I hope you like!!! BYEE :3\
\np.s no cats were actually put into a computer.\nI had too \
much fun writing this ^.^''')

