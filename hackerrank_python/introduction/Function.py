def is_leap(year):
    leap = False
    
    import math
    # Write your logic here
    if (year>=1900) & (year<=math.pow(10,5)): 
        '''
        The year can be evenly divided by 4;
        If the year can be evenly divided by 100, it is NOT a leap year, unless;
        The year is also evenly divisible by 400. Then it is a leap year.
        '''
        if year % 4 == 0: 
            if year % 100 == 0: 
                if year % 400 == 0: 
                    leap = True
            else:
                leap = True
             
        
    return leap
