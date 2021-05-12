from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

os.system('clear')

# Character IDs:
skt = [354350, 298736, 354348, 23559244, 10788708, 607240]
tiamat = [58813, 28192770, 46364292, 422436, 1496718]
trouble = [30456274, 29117600, 12203392]
curse = [31286942, 10111812, 28352221, 10107920, 10262697]

campaignCharacter = curse

# Agnor - 354350
# Ailith 298736
# Arya - 354348
# Ruby - #23559244
# Sana #10788708
# Typh - #607240
# Lucky - 422436
# Soraya - 1496718
# Krenaxios - 46364292
# Drusilia - 28192770
# Akta - 58813
# Kaeleth - 30456274
# Qrix - 29117600
# Rhurrk - 12203392
# Carris - 31286942
# Faerbor - 10111812
# Monk - 28352221
# Tail - 10107920
# Veil - 10262697
# Cloron - 14820937
# Komazur - 14820665
# Zaag - 14820702

characterName = ''
currentHp = ''
maxHp = ''
armorClass = ''
speed = ''
proficiencyBonus = ''
attributesNameList = []
savesNameList = []
skillsNameList = []
spellSlotsTotal = ''
spellSlotsUsed = ''
spellSlotsAvailable = ''
standardWaitInSeconds = 10
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0)

def waitForElementXpath(waitTimeInSeconds, Xpath):
    return WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.XPATH, Xpath)))

def waitForElementsXpath(waitTimeInSeconds, Xpath):
    WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.XPATH, Xpath)))
    return driver.find_elements_by_xpath(Xpath)

def waitForElementCssSelector(waitTimeInSeconds, CssSelector):
    return WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, CssSelector)))

def waitForElementsCssSelector(waitTimeInSeconds, CssSelector):
    WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, CssSelector)))
    return driver.find_elements_by_css_selector(CssSelector)

def attributeNames():
    attrNames = []
    for i in range(0, len(waitForElementsXpath(standardWaitInSeconds, './/section/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/span[1]'))):
        attrNames.append(waitForElementsXpath(standardWaitInSeconds, './/section/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/span[1]')[i].text[0:3])
    return attrNames

def setGlobalVariables():
    global characterName
    global currentHp
    global maxHp
    global armorClass
    global speed
    global proficiencyBonus
    global attributesNameList
    global savesNameList
    global skillsNameList
    characterName = waitForElementCssSelector(standardWaitInSeconds, '.ddbc-character-name')
    currentHp = waitForElementCssSelector(standardWaitInSeconds, 'div.ct-health-summary__hp-item:nth-child(1) > div:nth-child(2) > div')
    maxHp = waitForElementCssSelector(standardWaitInSeconds, 'div.ct-health-summary__hp-item:nth-child(3) > div:nth-child(2) > div:nth-child(1)')
    armorClass = waitForElementCssSelector(standardWaitInSeconds, '.ddbc-armor-class-box__value')
    speed = waitForElementCssSelector(standardWaitInSeconds, '.ddbc-distance-number--large > span:nth-child(1)')
    proficiencyBonus = waitForElementCssSelector(standardWaitInSeconds, '.ct-proficiency-bonus-box__value > span:nth-child(1) > span:nth-child(2)')
    attributesNameList = []
    for i in range(0, len(waitForElementsXpath(standardWaitInSeconds, './/section/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/span[1]'))):
        attributesNameList.append(waitForElementsXpath(standardWaitInSeconds, './/section/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/span[1]')[i].text[0:3])
    savesNameList = []
    for i in range(0, len(waitForElementsCssSelector(standardWaitInSeconds, 'div.ddbc-saving-throws-summary__ability'))):
        savesNameList.append(waitForElementsCssSelector(standardWaitInSeconds, 'div.ddbc-saving-throws-summary__ability > div:nth-child(3)')[i].text)
    skillsNameList = []
    for i in range(0, len(waitForElementsCssSelector(standardWaitInSeconds, 'div.ct-skills__item > div:nth-child(3)'))):
        skillsNameList.append(waitForElementsCssSelector(standardWaitInSeconds, 'div.ct-skills__item > div:nth-child(3)')[i].text)

class Elements():
    def __init__(self):
        super().__init__()

    def attributeChildByName(self, attrName, cssSelectorForChild):
        elementIndex = attributesNameList.index(attrName) + 1
        return driver.find_element_by_css_selector(f'div.ct-quick-info__abilities > div:nth-child({elementIndex}) > {cssSelectorForChild}')

    def attributeBonusSign(self, attrName):
        return self.attributeChildByName(attrName, 'div:nth-child(1) > div > span > span:nth-child(1)')

    def attributeBonusNumber(self, attrName):
        return self.attributeChildByName(attrName, 'div:nth-child(1) > div > span > span:nth-child(2)')

    def _attributeBigScore(self, attrName):
        return self.attributeChildByName(attrName, 'div:nth-child(1) > div:nth-child(3)')

    def _attributeSmallScore(self, attrName):
        return self.attributeChildByName(attrName, 'div:nth-child(1) > div:nth-child(4)')

    def attributeScore(self, attrName):
        try:
            ele = int(self._attributeBigScore(attrName).text)
            return self._attributeBigScore(attrName)
        except ValueError:
            return self._attributeSmallScore(attrName)

    def saveChildByName(self, saveName, cssSelectorForChild):
        elementIndex = savesNameList.index(saveName) + 1
        return driver.find_element_by_css_selector(f'div.ddbc-saving-throws-summary__ability:nth-child({elementIndex}) > div:nth-child(4) > span > {cssSelectorForChild}')

    def saveBonusSign(self, saveName):
        return self.saveChildByName(saveName, 'span:nth-child(1)')

    def saveBonusNumber(self, saveName):
        return self.saveChildByName(saveName, 'span:nth-child(2)')

    def skillChildByName(self, skillName, cssSelectorForChild):
        elementIndex = skillsNameList.index(skillName) + 1
        return driver.find_element_by_css_selector(f'div.ct-skills__item:nth-child({elementIndex}) > {cssSelectorForChild}')

    def skillMod(self, skillName):
        return self.skillChildByName(skillName, 'div:nth-child(2)')

    def skillSign(self, skillName):
        try:
            ele = self.skillChildByName(skillName, 'div:nth-child(4) > span > span:nth-child(1)')
            return ele
        except NoSuchElementException:
            return self.skillChildByName(skillName, 'div:nth-child(5) > span > span:nth-child(1)')

    def skillBonus(self, skillName):
        try:
            ele = self.skillChildByName(skillName, 'div:nth-child(4) > span > span:nth-child(2)')
            return ele
        except NoSuchElementException:
            return self.skillChildByName(skillName, 'div:nth-child(5) > span > span:nth-child(2)')

    ### SPELL LEVELS INCLUDES CANTRIPS AT INDEX 0!!!!
    def spellButtonWait(self):
        return waitForElementXpath(standardWaitInSeconds, '//section/div/div/div[2]/div/div[3]/div[6]/div/div[2]/div[1]/div[2]/span')

    def spellButtonNoWait(self):
        return driver.find_element_by_xpath('//section/div/div/div[2]/div/div[3]/div[6]/div/div[2]/div[1]/div[2]/span')

    def spellsParent(self):
        self.spellButtonWait().click()
        return waitForElementCssSelector(standardWaitInSeconds, 'div.ct-subsection:nth-child(6)')

    def allSpellLevels(self):
        return self.spellsParent().find_elements_by_xpath('./div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div')

    def spellSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div[1]/div/div')

    def usedSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div/div/div[@class="ct-slot-manager__slot ct-slot-manager__slot--used"]')

class ElementActions(Elements):
    def __init__(self):
        super().__init__()

    def getCombinedHpData(self):
        global currentHp
        global maxHp
        return f'{currentHp.text}/{maxHp.text}'

    def getArmorClass(self):
        return armorClass.text

    def getSpeed(self):
        return f'{speed.text}ft.'

    def getProficiencyBonus(self):
        return f'+{proficiencyBonus.text}'

    def combineSign(self, sign, integer):
        if sign == '-':
            return int(integer) * -1
        else:
            return int(integer)

    def getAttributeBonus(self, attrName):
        return self.combineSign(self.attributeBonusSign(attrName).text, self.attributeBonusNumber(attrName).text)

    def getAttributeScore(self, attrName):
        return self.attributeScore(attrName).text

    def isAttributeBonusEqual(self, skillName):
        if self.getAttributeBonus(skillName) != self.getSkillBonus(skillName):
            return False
        else:
            return True

    def combineAttrNameAndScore(self):
        fullAttribute = []
        for attributeName in (attributesNameList):
            fullAttribute.append(
                f'{attributeName[0:3]}: {"{:2d}".format(int(self.getAttributeScore(attributeName)))} {"({:+})".format(int(self.getAttributeBonus(attributeName)))}')
        return fullAttribute

    def getSaveNames(self):
        saveList = []
        for i in (savesNameList):
            saveList.append(i)
        return saveList

    def getSaveBonus(self, saveName):
        return self.combineSign(self.saveBonusSign(saveName).text, self.saveBonusNumber(saveName).text)

    def isSaveBonusEqual(self, saveName):
        if self.getAttributeBonus(saveName) != self.getSaveBonus(saveName):
            return False
        else:
            return True

    def getStandardSaveBlock(self):
        fullSave = []
        for saveName in (self.getSaveNames()):
            if not self.isSaveBonusEqual(saveName):
                fullSave.append(f'{saveName} {"{:+}".format(int(self.getSaveBonus(saveName)))}')
        return fullSave

    def getSkillNames(self):
        skillList = []
        for i in (skillsNameList):
            skillList.append(i)
        return skillList

    def getSkillMod(self, skillName):
        return self.skillMod(skillName).text

    def getSkillBonus(self, skillName):
        return self.combineSign(self.skillSign(skillName).text, self.skillBonus(skillName).text)

    def isSkillBonusEqual(self, skillName):
        skillMod = self.getSkillMod(skillName)
        if self.getAttributeBonus(skillMod) != self.getSkillBonus(skillName):
            return False
        else:
            return True

    def getNumSpellsPerLevel(self):
        return len(self.allSpellLevels())

    def getSlotsEachLevel(self, spellLevel):
        totalSlots = len(self.spellSlotsByLevel(spellLevel))
        return totalSlots

    def getUsedSlots(self, spellLevel):
        return len(self.usedSlotsByLevel(spellLevel))

    def getAvailableSlots(self, spellLevel):
        return int(self.getSlotsEachLevel(spellLevel)) - int(self.getUsedSlots(spellLevel))

    def allAttributesBlock(self):
        allAttributes = self.combineAttrNameAndScore()
        printableString = ''
        for i in range(0, len(allAttributes), int(len(allAttributes) / 2)):
            printableString += f'{allAttributes[i]} {allAttributes[i + 1]} {allAttributes[i + 2]}\n'
        return printableString

    def allSavesBlock(self):
        smallSaveBlock = self.getStandardSaveBlock()
        allSaves = '----------------------------------------\nSAVES\n'
        for i in range(0, int(len(self.getStandardSaveBlock()))):
            allSaves += f'{self.getStandardSaveBlock()[i]}\t'
        return allSaves

    def allSkillsBlock(self):
        allSkills = '----------------------------------------\nSKILLS\n'
        for skillName in self.getSkillNames():
            if not self.isSkillBonusEqual(skillName):
                allSkills += f'{skillName:<18} {self.getSkillMod(skillName)}   {"{:+}".format(int(self.getSkillBonus(skillName)))}\n'
        return allSkills

    def allSpellsBlock(self):
        allSpells = '----------------------------------------\nSPELLS SLOTS\nLevel  Total  Used  Available\n'
        for i in range(1, len(self.allSpellLevels())):
            allSpells += f'{i}|     {self.getSlotsEachLevel(i):<6} {self.getUsedSlots(i):<5} {self.getAvailableSlots(i)}\n'
        return allSpells

for h in campaignCharacter:
    driver.get(f'https://www.dndbeyond.com/characters/{h}/json')
    ele = ElementActions()
    setGlobalVariables()
    print(characterName.text)
    print('HP:', ele.getCombinedHpData(), 'AC:', ele.getArmorClass(), 'Speed:', ele.getSpeed(), 'Prof:', ele.getProficiencyBonus())
    print(ele.allAttributesBlock())
    print(ele.allSavesBlock())
    print(ele.allSkillsBlock())
    if (ele.spellButtonNoWait().text == 'SPELLS'):
        print(ele.allSpellsBlock())
    print('\n=========================================================')

driver.close()
