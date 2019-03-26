from selenium import webdriver
from lxml import html
from lxml import etree
import re
import time
import pyautogui


def enterBarracks():

    pyautogui.moveTo(900,275)
    pyautogui.click(900,275)


def makeWeapon():
    pyautogui.moveTo(440, 410)
    pyautogui.click(440,410)

def buildHouse():
    pyautogui.moveTo(600,270)
    pyautogui.click(600,270)
    pyautogui.moveTo(440, 360)
    pyautogui.click(440, 360)
def enterMarket():
    pyautogui.moveTo(1000,270)
    pyautogui.click(1000,270)

def sellStone():
    pyautogui.moveTo(610,600)
    pyautogui.click(610,600)

def buyFeast():
    enterCenter()
    pyautogui.moveTo(950,440)
    pyautogui.click(950,440)


def setHund():
    pyautogui.moveTo(580,740)
    pyautogui.click(580,740)
    pyautogui.click(580,740)

def setOne():
    pyautogui.moveTo(580,740)
    pyautogui.click(580,740)

def sellWeapon():
    pyautogui.moveTo(610,690)
    pyautogui.click(610,690)

def buyStone():
    pyautogui.moveTo(520,600)
    pyautogui.click(520,600)

def buyFood():
    pyautogui.moveTo(530,400)
    pyautogui.click(530,400)

def buyLumber():
    pyautogui.moveTo(520,500)
    pyautogui.click(520,500)
def enterCenter():
    pyautogui.moveTo(720,270)
    pyautogui.click(720,270)
def assignTav():
    #enterCenter()
    pyautogui.moveTo(655,505)
    pyautogui.click(655,505)
def assignMiners():
    #enterCenter()
    pyautogui.moveTo(655,465)
    pyautogui.click(655,465)

def checkFood(food, gold, stone):

    if food < 300 and gold > 1000:
        enterMarket()
        setHund()
        for x in range(5):
            enterMarket()
            buyFood()
        gold = gold - 500
        food = food + 500
        setOne()


    if food < 300 and gold > 150 and gold < 1000:
        enterMarket()
        setHund()
        for x in range(9):
            if gold > 150:
                enterMarket()
                buyFood()
        gold = 100
        food = food + 500
        setOne()



    if food < 300 and gold < 100 and gold > 20:
        spendableGold = gold-20
        for x in range(spendableGold):
            enterMarket()
            buyFood()

        food = food + 50
        gold = 20

    if food < 300 and stone > 20:
        usableStone = stone-20
        deficit = 300-food
        for x in range(deficit):
            if usableStone > 0:
                sellStone()
                buyFood()
                usableStone = usableStone-1

def checkPopularity(popularity, food):
    if popularity < 35 and food > 60:
        buyFeast()

def checkStone(stone):
    if stone > 1000:
        enterMarket()
        setHund()
        for x in range(7):
            sellStone()
        setOne()

def checkWood(wood, gold):
    if wood <200 and gold > 1000:
        enterMarket()
        setHund()
        for x in range(5):
            buyLumber()
        setOne()



def checkPop(popNum, woodNum):

    popNum = int(popNum/5)
    if popNum < 5:
        loop = int(5-popNum)
        print("popNum is small")


        for x in range(loop):
            if woodNum > 100:
                buildHouse()
                woodNum = woodNum -100
                print("house built")
            else:
                print("not enough wood to build house")
        enterCenter()
        for x in range(5):
            assignTav()
        for x in range(15):
            assignMiners()

    print("checkPop ran")





def bot():
    while(True):

        innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
        htmlElem = html.document_fromstring(innerHTML)
        root = htmlElem
        stats1 = root.xpath('//div[@class="right col-lg-4"]/text()')
        pop = stats1[0]

        cleanPop = ((re.sub("[^0-9]", "", pop)))


        if len(cleanPop)==2:
            cleanestPop = int(cleanPop[1:])
        if len(cleanPop)==3:
            cleanestPop = int(cleanPop[1:])
        elif len(cleanPop)==4:
            cleanestPop = int(cleanPop[2:])

        pop2 = stats1[1]
        cleanPop2 = int(re.sub("[^0-9]", "", pop2))

        resources = root.xpath('//div[@class="right paddingZero col-lg-3"]/text()')
        food = int(resources[0])
        wood = int(resources[2])
        gold = int(resources[6])
        stone = int(resources[4])
        # enterBarracks()
        # weapons = root.xpath('//div[@id="defense"]/text()')
        # if weapons:
        #     s = int(re.sub("[^0-9]", "", weapons[0]))
        #     #print(s)
        checkFood(food,gold,stone)
        checkPopularity(cleanPop2, food)
        checkPop(cleanestPop,wood)
        checkPopularity(cleanPop2, food)
        checkStone(stone)
        checkWood(wood,gold)
        time.sleep(3)


browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "http://sovereign2.andrewdanielyoung.com/pages/program.html"
browser.get(url) #navigate to the page

start = input("Enter 's' to start bot ")

run = False
if start == "s":
    time.sleep(2)
    bot()



#root = etree.XML("<root>data</root>") #list of all td elems
#print(root)



# <div data-toggle="tooltip" title="Population and Available Beds.
# Every month travelers will visit and decide whether to stay
# They judge based on:
# --Citizen Satisfaction
# --Available Beds" class="right col-lg-4">2 / 5</div>
