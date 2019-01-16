'''
UPC Check Digits



'''


def upc(number):
    if len(str(number)) > 11:
        print('Code is too long')
    
    #print(str(number))
   
    s_number=str(number)
    
    #Iterate backwards to avoid having to build into 11 str (starts at -1 the first digit, -2 second digit)
    odd = sum(int(i) for i in s_number[::-2])
    even =sum(int(i) for i in s_number[-2::-2])  
    #print(str(odd))
    #print(str(even))
    
    code=(odd*3+even)%10
    #print(code)
    if code!=0:
        code=10-code

    #print(str(code))
    print('upc(' + s_number + ') => ' + str(code))

#upc(123456)
upc(4210000526)
upc(3600029145)
upc(12345678910)
upc(1234567)
