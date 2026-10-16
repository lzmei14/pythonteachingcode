# [ ] create, call and test the adding_report() function
def adding_report(report="T"):
    total = 0
    items = ""

    integer = input('Input a positive integer to add to the total or "Q" to quit: ')
    
    while True:
        if integer.isdigit():
            total += int(integer)
            if report == "A":
                items += integer + "\n"

        elif integer.upper().startswith("Q"):
            if report == "A":
                print("Items:\n" + items)
                
            print("\nTotal:")
            print(total,"\nCalculated by: Michelle Liu")
            break 
        else:
            print(integer + " is an invalid input.")
            
        integer = input('Input an integer or "Q" to quit: ')

adding_report("A")
adding_report("T")
    