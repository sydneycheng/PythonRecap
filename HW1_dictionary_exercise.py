
def main():
    course_info = {
                'CS101':[3004,'Haynes','8:00 a.m.'],
                'CS102':[4501,'Alvarado','9:00 a.m.'],
                'CS103':[6755,'Rich','10:00 a.m.'],
                'NT110':[1244,'Burke','11:00 a.m.'],
                'CM241':[1411,'Lee','1:00 p.m.']
                }

    course_num = input("Enter a course number: ")

    print(course_info[course_num])


    codes = {
            'A':'!', 'a':'@','B':'#','b':'$','C':'%','c':'^','D':'&','d':'*','E':'(',
            'e':')','F':'-','f':'_','G':'+','g':'=','H':'[','h':']','I':'{','i':'}',
            'J':',','j':'.','K':'<','k':'>','L':'/','l':'?','M':'1','m':'2','N':'3',
            'n':'4','O':'5','o':'6','P':'7','p':'8','Q':'9','q':'10','R':'11','r':'12',
            'S':'13','s':'14','T':'15','t':'16','U':'17','u':'18','V':'19','v':'20',
            'W':'21','w':'22','X':'23','x':'24','Y':'25','y':'26','Z':'27,','z':'28'
            }

    ##Read txt file
    infile = open('info_security.txt', 'r')

    message = infile.read()
    
    infile.close()

    
    #Write to a new txt file (encrypted)
    encryption = open('encrypt_info_security.txt', 'w')

    for letter in message:
        if letter in codes:
            encryption.write(codes[letter])
        
    
    encryption.close()
    
main()
