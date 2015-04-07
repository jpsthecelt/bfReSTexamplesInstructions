# read numbers till eof and show squares
import sys
     
def menu():
    print 'System Fixlet Execution Menu'                      # print sends to sys.stdout
    print '1 - Find all computers'
    print '2 - Find all fixlets'
    print '3 - Find number of fixlet containing string'
    print '4 - Execute fixlet number...'

    while 1:
        num = 0
        reply = ''
        try:
            reply  = raw_input('Enter a number>')   # raw_input reads sys.stdin
        except EOFError:
            break                                   # raises an except on eof
        except:
            print '\n'
            print sys.exc_info()
            print '\n\n'
        else:                                       # input given as a string
            num = int(reply)
            print "Menu item #%d selected" % num
        finally:
		if num == 1:
		    findAllComputers()
		elif num == 2:
		    findAllFixlets()
                elif num == 3:
                    findFixletContaining()
                elif num == 4:
                    executeFixletByNumber()

	
    print '\nBye\n\n'
		
def findAllComputers():
    print 'Selected Menu1...'

def findAllFixlets():
    print 'Selected Menu2...'

def findFixletContaining():
    print 'Selected Menu3...'

def executeFixletByNumber():
    print 'Selected Menu4...'

     
if __name__ == '__main__': 
    menu()    
