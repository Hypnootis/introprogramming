special_price = False
is_student = False
good_month = False

student_status = input("Are you a student?\n").lower()

if student_status == "y":
    is_student = True
else:
    is_student = False

travel_month = int(input("Travel month? (y/n)\n"))

if travel_month == 6 or travel_month == 7 or travel_month == 8:
    good_month = False
else:
    good_month = True

if is_student and good_month:
    special_price = True
    print("Special price!")
else:
    special_price = False
    print("Normal price.")

