def payslipMenu():
    print("<><><><><><><><><><><><><><>\n    Rate calculator\n<><><><><><><><><><><><><><>")
    name = input("Enter you full name: ")# used to find the name of the person using this print("<><><><><><><><><><><><><><>")
    regularHours = input("Do you do regular hours, Enter y for yes or n for no: ").lower() #used to determine if the person has custom hours
    if regularHours.lower() == "n":
        print("<><><><><><><><><><><><><><> ")
        customHours = float(input("what hours do you do: "))#used to find out what the custom hours are print("<><><><><><><><><><><><><><>") hourlyRate = float(input("what is your hourly rate: "))#used to find hourly rate print("<><><><><><><><><><><><><><>") overtime = float(input("How many hours of overtime do you have: "))#used to find overtime print("<><><><><><><><><><><><><><>") if overtime > 10: overtime = 10 #Overtime cannot exceed over ten hours and as such is capped at ten overtimeCorrected = overtime*1.5 #calculations to find out what the total pay is weeksPayBeforeFinalization = customHours*hourlyRate weeksPayFinal = weeksPayBeforeFinalization+overtimeCorrected print("Name: ", name, "    Pay: £", round(weeksPayFinal, 3))#prints name and pay else: print("<><><><><><><><><><><><><><>") hourlyRate = float(input("what is your hourly rate: "))#used to find hourly rate print("<><><><><><><><><><><><><><>") overtime = float(input("How many hours of overtime do you have: "))#used to find overtime print("<><><><><><><><><><><><><><>") if overtime > 10: overtime = 10 #Overtime cannot exceed over ten hours and as such is capped at ten overtimeCorrected = overtime*1.5#calculations to find out what the total pay is

weeksPayBeforeFinalization = 40*hourlyRate weeksPayFinal = weeksPayBeforeFinalization+overtimeCorrected

 print("Name: ", name, "    Pay: £", round(weeksPayFinal, 3))#prints name and pay