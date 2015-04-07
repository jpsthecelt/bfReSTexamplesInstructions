# read numbers till eof and show squares
import sys
     
def menu():
    print 'System Fixlet Execution Menu'                      # print sends to sys.stdout
    while 1:
        try:
            reply  = int(raw_input('Enter a number>'))   # raw_input reads sys.stdin
        except EOFError:
            break                                   # raises an except on eof
        except:
            print '\n'
            print sys.exc_info()
            print '\n\n'
        else:                                       # input given as a string
#            num = int(reply)
            print "Menu item #%d selected" % reply
        finally:
		if reply == 1:
		    menu1()
		elif reply == 2:
		    menu2()
	
    print '\nBye\n\n'
		
def menu1():
    print 'Menu1...'

def menu2():
    print 'Menu2...'
     
if __name__ == '__main__': 
    menu()    
