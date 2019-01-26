'''
wanted to test a roulette doubling strategy to see what success it could have
american numbers 36 + 0 + 00


i wrote this drunk, don't judge me
'''
import random


def RouletteDouble(winFloat, cash):
    baseCash = cash
    bet = 5
    count = 1
    #print('betting on evens!')
    while True:
        roll = random.randint(0, 39)
        #print('game number: ' + str(count+1) + ' and the roll is: ' + str(roll))
        if roll == 37 or roll == 38 or roll%2==1:
            cash -= bet
            bet += bet
            #print('\x1b[6;30;41m' + 'Loss! ' + str(cash) + ' ' + str(bet) + '\x1b[0m')                                #'\x1b[6;30;41m' + '[Failed]' + '\x1b[0m')
        else:
            cash += bet
            bet = 5
            #print('\x1b[6;30;42m' + 'win!: ' + str(cash) + '\x1b[0m')                 #'\x1b[6;30;42m' + '[Passed]' + '\x1b[0m'

        if cash < bet:
            #print('You Bust! ', end='')
            print('You Bust! '+ str(cash))
            #break
            return cash
        if cash  > baseCash*winFloat:
            #print('You doubled your money! ', end='')
            print('You Win!')
            #break
            return 1

    #print('You leave with ' + str(cash))


def winAssessement(runs, winFloat, cash):
    winCount = 0
    returnedValue = 0
    for count in range(runs):
        amount = RouletteDouble(winFloat, cash)
        if amount > 1:
            returnedValue += amount
        else:
            winCount += 1
        
    print('Wining ' + str(winCount/runs) + ' of the time')
    print('$' + str(cash*runs) + ' invested ' + str(round(winCount/runs*100000, 2) + returnedValue) + ' returned')

#RouletteDouble(50, 100)

print('Runs, Stop win float, starting cash')
winAssessement(int(input()), float(input()), int(input()))

