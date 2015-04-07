def menu1():
    print 'menu1' 

def menu2():
    print 'menu2' 

def menu():
    while 1:
	print 'This is the start of the menu'
        try:
            reply = int(raw_input('Enter a number'))
        except EOFError:
            break
        else:
		if reply == 1:
                    menu1()
		else:
                    if reply == 2:
                        menu2()
	print 'Ending program...'
     
if '__NAME__' == '__MAIN__':
    menu()
