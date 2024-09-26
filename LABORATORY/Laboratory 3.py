#Customer's Salary
customer_salary = int(input("Enter the amount of salary "))
loan_amount = int(input("Enter the amount of loan "))
months = int(input("Enter the amount of months "))


if customer_salary >= 30000.00:
#Months to pay
 monthly_payment= loan_amount* 0.1
 interest = float(loan_amount* 0.1) 
 print ("Approved!")
 print ("You are eligible for a loan")
 payment = interest + loan_amount 
 print ("Payable amount:", payment)

else :
 customer_salary* 10 <= 30000.00 
 print("You are not eligible for a loan due to low salary") 
 loan_amount > customer_salary * 10 
 print("You are not eligible for a loan due to high loan request") 
 print("Disapproved")
 
 
 exit
 