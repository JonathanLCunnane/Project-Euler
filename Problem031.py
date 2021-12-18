# firstly we will attempt to simply brute force a onumber of combinations that work
from time import perf_counter
start = perf_counter()
total = 0
#after each iteration starts, if the value is above two pounds we break.
#loop through £2, only two possibilities
for two_pound in range(0,2):
    #loop through £1, only three possibilities
    for pound in range(0,3):
        if two_pound * 200 + pound * 100 > 200:
            break
        #loop through 50p, only five possibilities
        for fifty_pence in range(0,5):
            if two_pound * 200 + pound * 100 + fifty_pence * 50 > 200:
                break
            #loop through 20p, only eleven possibilities
            for twenty_pence in range(0,11):
                if two_pound * 200 + pound * 100 + fifty_pence * 50 + twenty_pence * 20 > 200:
                    break
                #loop through 10p, only twenty one possibilities
                for ten_pence in range(0,21):
                    if two_pound * 200 + pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 > 200:
                        break
                    #loop through 5p, only fourty one possibilities
                    for five_pence in range(0,41):
                        if two_pound * 200 + pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 > 200:
                            break
                        #loop through 2p, only one hundred and one possibilities
                        for two_pence in range(0,101):
                            if two_pound * 200 + pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 + two_pence * 2 > 200:
                                break
                            #loop through 1p, only two hundred and one possibilities
                            for one_pence in range(0,201):
                                #if the sum of coins in £2, then success, and add to the 
                                # total number of combinations of coins.
                                if two_pound * 200 + pound * 100 + fifty_pence * 50 + twenty_pence * 20 + ten_pence * 10 + five_pence * 5 + two_pence * 2 + one_pence == 200:
                                    total += 1
                                    break
print(f"Total # of different ways to sum £2 is: {total}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms.")