while True:
    try:
        marks = int(input("Enter student's marks from range (0-100): "))

        if 0 <= marks <= 100:
            print("Valid marks:", marks)
            break
        else:
            print("Marks must be between 0 and 100.")

    except ValueError:
        print("Invalid input! Please enter marks as an integer.")