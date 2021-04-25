from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
os.system('clear')

# Character IDs:
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
# Komazur - 14820665
# Zaag - 14820702
# Qrix - 29117600
# Cloron - 14820937

campaignCharacter = [14820937, 14820665]  # 354350, 298736, 354348, 23559244, 10788708, 607240]
standardWaitInSeconds = 10
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0)

   
def waitForElementXpath(waitTimeInSeconds, Xpath):
    return WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.XPATH, Xpath)))


def waitForElementCssSelector(waitTimeInSeconds, CssSelector):
    return WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, CssSelector)))


class ParentElements:
    def __init__(self):
        pass
    
    def quickInfoParent(self):
        return waitForElementCssSelector(standardWaitInSeconds, '.ct-quick-info')
                                  
    def attributesCollectionParent(self):
        return self.quickInfoParent().find_elements_by_xpath('./div[1]/div')

    def attributeByName(self, attrName):
        for i in (self.attributesCollectionParent()):
            ele = i.find_element_by_xpath('./div/div[2]/span[1]')
            if attrName in ele.text:
                return i

    def saveParent(self):
        return waitForElementXpath(standardWaitInSeconds, '//section/div/div/div[2]/div/div[3]/div[1]/div[1]')
                                                         
    def saveCollectionParent(self):
        return self.saveParent().find_elements_by_xpath('./div[2]/div/div')
    
    def saveByName(self, saveName):
        for i in (self.saveCollectionParent()):
            ele = i.find_element_by_xpath('./div[3]')
            if ele.text == saveName:
                return i
                                                                 
    def skillsParent(self):
        return driver.find_element_by_xpath('//section/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]')
    
    def skillsCollectionParent(self):
        return self.skillsParent().find_elements_by_xpath('./div[2]/div[@class="ct-skills__item"]')
                
    def skillByName(self, skillName):
        for i in (driver.find_elements_by_css_selector('div.ct-skills__item')):
            ele = i.find_element_by_xpath('./div[3]')
            if ele.text == skillName:
                return i

    def spellsParent(self):
        self.spellButtonWait().click()
        return waitForElementXpath(standardWaitInSeconds, '//section/div/div/div[2]/div/div[3]/div[6]')
                                                                  
    def spellButtonWait(self):
        return waitForElementXpath(standardWaitInSeconds, '//section/div/div/div[2]/div/div[3]/div[6]/div/div[2]/div[1]/div[2]/span')

    def characterTidbits(self):
        return waitForElementXpath(standardWaitInSeconds, '//section/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/div[2]')

    def combatSummary(self):
        return waitForElementCssSelector(standardWaitInSeconds, '.ct-combat__summary')
                                                                                                                  
class ChildElements(ParentElements):
    def __init__(self):
        self.parent = ParentElements()

    def characterName(self):
        return self.parent.characterTidbits().find_element_by_xpath('./div[1]/div[1]')

    def currentHp(self):
        return self.parent.quickInfoParent().find_element_by_xpath('./div[5]/div/div[2]/div[2]/div[1]/div[2]/div')

    def armorClass(self):
        return self.parent.combatSummary().find_element_by_css_selector('.ddbc-armor-class-box__value')

    def speed(self):
        return self.parent.quickInfoParent().find_element_by_xpath('./div[3]/div/div[3]/span/span[1]')
                                         
    def maxHp(self):
        return self.parent.quickInfoParent().find_element_by_xpath('./div[5]/div/div[2]/div[2]/div[3]/div[2]/div')
                                                                  
    def proficiencyBonus(self):
        return self.parent.quickInfoParent().find_element_by_xpath('./div[2]/div/div[3]/span/span[2]')

    def attributeNames(self):
        attributeNameList = []
        for i in (self.parent.attributesCollectionParent()):
            attributeNameList.append(i.find_element_by_xpath('./div/div[2]/span[1]'))
        return attributeNameList
    
    def attributeBonusSign(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_css_selector('div.ct-quick-info__ability > div:nth-child(1) > div > span > span:nth-child(1)')
    
    def attributeBonusNumber(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_css_selector('div.ct-quick-info__ability > div:nth-child(1) > div > span > span:nth-child(2)')
                                                     
    def _attributeBigScore(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_css_selector('div.ct-quick-info__ability > div:nth-child(1) > div:nth-child(3)')

    def _attributeSmallScore(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_css_selector('div.ct-quick-info__ability > div:nth-child(1) > div:nth-child(4)')

    def attributeScore(self, attrName):
        try:
            ele = int(self._attributeBigScore(attrName).text)
            return self._attributeBigScore(attrName)
        except ValueError:
            return self._attributeSmallScore(attrName)

    def saveNames(self):
        saveNamesList = []
        for i in (self.parent.saveCollectionParent()):
            saveNamesList.append(i.find_element_by_xpath('./div[3]'))
        return saveNamesList

    def saveBonusSign(self, saveName):
        return self.parent.saveByName(saveName).find_element_by_xpath('./div[4]/span/span[1]')

    def saveBonusNumber(self, saveName):
        return self.parent.saveByName(saveName).find_element_by_xpath('./div[4]/span/span[2]')

    def skillNames(self):
        skillNamesList = []
        for skillElement in (self.parent.skillsCollectionParent()):
            skillNamesList.append(skillElement.find_element_by_xpath('./div[3]'))
        return skillNamesList

    def skillMod(self, skillName):
        return self.parent.skillByName(skillName).find_element_by_xpath('./div[2]')

    def skillSign(self, skillName):
        try:
            ele = self.parent.skillByName(skillName).find_element_by_xpath('./div[4]/span/span[1]')
            return ele
        except NoSuchElementException:
            return self.parent.skillByName(skillName).find_element_by_xpath('./div[5]/span/span[1]')

    def skillBonus(self, skillName):
        try:
            ele = self.parent.skillByName(skillName).find_element_by_xpath('./div[4]/span/span[2]')
            return ele
        except NoSuchElementException:
            return self.parent.skillByName(skillName).find_element_by_xpath('./div[5]/span/span[2]')
   
    ### SPELL LEVELS INCLUDES CANTRIPS AT INDEX 0!!!!

    def spellButtonNoWait(self):
        return driver.find_element_by_xpath('//section/div/div/div[2]/div/div[3]/div[6]/div/div[2]/div[1]/div[2]/span')
                                        
    def allSpellLevels(self):
        return self.spellsParent().find_elements_by_xpath('./div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div')
                                           
    def spellSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div[1]/div/div')

    def usedSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div/div/div[@class="ct-slot-manager__slot ct-slot-manager__slot--used"]')

class ElementActions(ChildElements):
    def __init__(self):
        self.children = ChildElements()

    def getCharacterName(self):
        return self.children.characterName().text

    def getCurrentHp(self):
        return self.children.currentHp().text

    def getMaxHp(self):
        return self.children.maxHp().text

    def getCombinedHpData(self):
        return f'{ele.getCurrentHp()}/{ele.getMaxHp()}'

    def getArmorClass(self):
        return self.children.armorClass().text

    def getSpeed(self):
        return f'{self.children.speed().text}ft.'

    def getProficiencyBonus(self):
        return f'+{self.children.proficiencyBonus().text}'

    def getAttributeNames(self):
        attributeList = []
        for i in (self.children.attributeNames()):
            attributeList.append(f'{i.text[0:3]}')
        return attributeList
        
    def combineSign(self, sign, integer):
        if sign == '-':
            return int(integer) * -1
        else:
            return int(integer)

    def getAttributeBonus(self, attrName):
        return self.combineSign(self.children.attributeBonusSign(attrName).text, self.children.attributeBonusNumber(attrName).text)

    def getAttributeScore(self, attrName):
        return self.children.attributeScore(attrName).text

    def isAttributeBonusEqual(self, skillName):
        if self.getAttributeBonus(skillName) !=  self.getSkillBonus(skillName):
            return False
        else:
            return True

    def getSaveNames(self):
        saveList = []
        for i in (self.children.saveNames()):
            saveList.append(i.text)
        return saveList
    
    def getSaveBonus(self, saveName):
        return self.combineSign(self.children.saveBonusSign(saveName).text, self.children.saveBonusNumber(saveName).text)

    def isSaveBonusEqual(self, saveName):
        if self.getAttributeBonus(saveName) != self.getSaveBonus(saveName):
            return False
        else:
            return True

    def getSkillNames(self):
        skillList = []
        for i in (self.children.skillNames()):
            skillList.append(i.text)
        return skillList

    def getSkillMod(self, skillName):
        return self.children.skillMod(skillName).text

    def getSkillBonus(self, skillName):
        return self.combineSign(self.children.skillSign(skillName).text, self.children.skillBonus(skillName).text)

    def isSkillBonusEqual(self, skillName):
        skillMod = self.getSkillMod(skillName)
        if self.getAttributeBonus(skillMod) != self.getSkillBonus(skillName):
            return False
        else:
            return True

    def getNumSpellsPerLevel(self):
        return len(self.children.allSpellLevels())

    def getSlotsEachLevel(self, spellLevel):
        totalSlots = len(self.children.spellSlotsByLevel(spellLevel))
        return totalSlots

    def getUsedSlots(self, spellLevel):
        return len(self.children.usedSlotsByLevel(spellLevel))

    def getAvailableSlots(self, spellLevel):
        return int(self.getSlotsEachLevel(spellLevel)) - int(self.getUsedSlots(spellLevel))

    def combineAttrNameAndScore(self):
        fullAttribute = []
        for attributeName in (self.getAttributeNames()):
            fullAttribute.append(f'{attributeName[0:3]}: {"{:2d}".format(int(self.getAttributeScore(attributeName)))} {"({:+})".format(int(self.getAttributeBonus(attributeName)))}')
        return fullAttribute

    def getStandardSaveBlock(self):
        fullSave = []
        for saveName in (self.getSaveNames()):
            if not self.isSaveBonusEqual(saveName):
                fullSave.append(f'{saveName} {"{:+}".format(int(self.getSaveBonus(saveName)))}')
        return fullSave

    # fullAttributeBlock = ele.combineAttrNameAndScore()
    # for i in range(0, len(fullAttributeBlock), int(len(fullAttributeBlock) / 2)):
    #    print(fullAttributeBlock[i], fullAttributeBlock[i + 1], fullAttributeBlock[i + 2])

    def allAttributesBlock(self):
        allAttributes = self.combineAttrNameAndScore()
        for i in range(0, len(allAttributes), int(len(allAttributes) / 2)):
            print(len(allAttributes))
            allAttributes = f'{allAttributes[i], allAttributes[i + 1], allAttributes[i + 2]}'
        return allAttributes

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
        self.children.spellButtonNoWait().click
        allSpells = '----------------------------------------\nSPELLS SLOTS\nLevel  Total  Used  Available\n'
        for i in range(1, self.getNumSpellsPerLevel()):
            allSpells += f'{i}|     {self.getSlotsEachLevel(i):<6} {self.getUsedSlots(i):<5} {self.getAvailableSlots(i)}\n'
        return allSpells

for h in campaignCharacter:
    driver.get(f'https://www.dndbeyond.com/characters/{h}/json')
    ele = ElementActions()
    
    print(ele.getCharacterName())
    print('HP:',ele.getCombinedHpData(), 'AC:', ele.getArmorClass(), 'Speed:', ele.getSpeed(), 'Prof:', ele.getProficiencyBonus())
    #fullAttributeBlock = ele.combineAttrNameAndScore()
    #for i in range(0, len(fullAttributeBlock), int(len(fullAttributeBlock)/2)):
    #    print(fullAttributeBlock[i], fullAttributeBlock[i+1], fullAttributeBlock[i+2])
    print(ele.allAttributesBlock())
    print(ele.allSavesBlock())
    print(ele.allSkillsBlock())
    print(ele.allSpellsBlock())
    print('\n=========================================================')

driver.close()
