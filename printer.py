import time

def printLaterFewSec(fewSec):
    time.sleep(fewSec)
    
def printInfo(contents):
    print('=======================================================================\n')
    print(contents)
    print('\n=======================================================================')

def printWarning(contents):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    print(contents)
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    
def printWind(contents):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(contents)
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def printLineFeed1(contents):
    print('\n')
    print(contents)
    print('\n')

def printLineFeed2(contents):
    print('\n\n')
    print(contents)
    print('\n\n')

def printMenu(contents):
    print('\n\n\n')
    print(contents)
    print('\n\n\n')


