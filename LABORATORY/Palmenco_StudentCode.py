name = str(input("Enter your name"))
section = str(input("Enter your section"))
prelim = round(float(input("Enter your prelim grade")),2)
midterm= round(float(input("Enter your midterm grade")),2)
finals = round(float(input("Enter your final grade")),2)


if(prelim>=40 and prelim <=100) and (midterm >=40 and midterm <=100) and (finals>=40 and finals <= 100):

 prelim= (33.33 * prelim)/100
 midterm = (33.33 * midterm)/100
 finals = (33.33 * finals)/100
 calculated_final = round((prelim + midterm + finals),2)
 print("Your Grade is:", calculated_final)
 
if (calculated_final <= 100 and calculated_final >=99):
        print("Your Grade is 1.00")
elif (calculated_final <= 98 and calculated_final >=96):
        print("Your Grade is 1.25")
elif (calculated_final <= 100 and calculated_final >=99):
        print("Your Grade is 1.50")
elif (calculated_final <= 95 and calculated_final >=93):
        print("Your Grade is 1.75") 
elif (calculated_final <= 89 and calculated_final >=87):
        print("Your Grade is 2.00")  
elif (calculated_final <= 86 and calculated_final >=84):
        print("Your Grade is 2.25")
elif (calculated_final <= 80 and calculated_final >=78):
        print("Your Grade is 2.75")
elif (calculated_final <= 77 and calculated_final >=75):
        print("Your Grade is 3.00")
elif (calculated_final < 75): 
        print("Your Grade is 5.00")

else:
        print("Error!")