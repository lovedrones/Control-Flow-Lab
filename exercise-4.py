# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triA = input("Enter  length of side A ")
triB = input("Enter length of side B ")
triC = input("Enter length of side C ")

if(triA == triB and triB == triC and triC == triA):
    print('All three sides are equal in length')
elif( triA == triB or triB == triC or triC == triA):
        print('two sides are the same')
else: 
    print('all three sides are unequal')
