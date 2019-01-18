'''
Test function i wrote to test future applications takes 3 args

	1. function name
	2. function input		#TODO update for mutiple args*
	3. function output

and compares result, displaying expected and actual returns if test is not passed.

'''

def test(func, inp, out):
    print('Testing ... ', end='')
    if func(inp) == out:
        print('[Passed]')
        return True
    else:
        print('[Failed]')
        print('Expected: ' + str(inp) + ' => ' + str(out))
        print('Actual: ' + str(inp) + ' => ' + str(func(inp))) 
        return False

