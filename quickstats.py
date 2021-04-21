from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import namer_module
os.system('clear')

# Character IDs:
#Agnor - 354350
#Ailith 298736
#Arya - 354348
#Ruby - #23559244
#Sana #10788708
#Typh - #607240
#Lucky - 422436
#Soraya - 1496718
#Krenaxios - 46364292
#Drusilia - 28192770
#Akta - 58813
#Komazur - 14820665
#Zaag - 14820702
#Qrix - 29117600

campaignCharacter =  [354350, 298736, 354348, 23559244, 10788708, 607240]
standardWaitInSeconds = 10
driver = webdriver.Chrome()
driver.implicitly_wait(0)
driver.set_window_size(1920, 1080)
   
def waitForElementXpath(waitTimeInSeconds, Xpath):
    return WebDriverWait(driver, waitTimeInSeconds).until(EC.presence_of_element_located((By.XPATH, Xpath)))

class ParentElements:
    def __init__(self):
        pass
    
    def quickInfoParent(self):
        return  waitForElementXpath(standardWaitInSeconds,'//section/div[1]/div/div[2]/div/div[2]')
                                  
    def attributesCollectionParent(self):
        return self.quickInfoParent().find_elements_by_xpath('./div[1]/div')

    def attributeByName(self, attrName):
        for i in (self.attributesCollectionParent()):
            ele = i.find_element_by_xpath('./div/div[2]/span[1]')
            if attrName in ele.text:
                return i

    def saveParent(self):
        return waitForElementXpath(standardWaitInSeconds,'//section/div/div/div[2]/div/div[3]/div[1]/div[1]')
                                                         
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
        for i in (self.skillsCollectionParent()):
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
        return waitForElementXpath(standardWaitInSeconds, '//div[1]/div/div[3]/div/section/div/div/div[2]/div/div[3]')
                                                                                                                  
class ChildElements(ParentElements):
    def __init__(self):
        self.parent = ParentElements()

    def characterName(self):
        return self.parent.characterTidbits().find_element_by_xpath('./div[1]/div[1]')

    def currentHp(self):
        return self.parent.quickInfoParent().find_element_by_xpath('./div[5]/div/div[2]/div[2]/div[1]/div[2]/div')

    def armorClass(self):
        return self.parent.combatSummary().find_element_by_xpath('./div[5]/div/div/div[2]/div/div[3]')

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

    def saveNames(self):
        saveNamesList = []
        for i in (self.parent.saveCollectionParent()):
            saveNamesList.append(i.find_element_by_xpath('./div[3]'))
        return saveNamesList

    def skillNames(self):
        skillNamesList = []
        for skillElement in (self.parent.skillsCollectionParent()):
            skillNamesList.append(skillElement.find_element_by_xpath('./div[3]'))
        return skillNamesList
    
    def _attributeBonusBigSign(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[3]/span/span[1]')
    
    def _attributeBonusBigNumber(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[3]/span/span[2]')

    def _attributeBonusSmallSign(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[4]/span/span[1]')

    def _attributeBonusSmallNumber(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[4]/span/span[2]')
                                                     
    def _attributeBigScore(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[3]')

    def _attributeSmallScore(self, attrName):
        return self.parent.attributeByName(attrName).find_element_by_xpath('./div/div[4]')
    
    def attributeBonusSign(self, attrName):
        try:
            ele =  self._attributeBonusBigSign(attrName)
            return ele
        except NoSuchElementException:
            return self._attributeBonusSmallSign(attrName)

    def attributeBonusNumber(self, attrName):
        try:
            ele = self._attributeBonusBigNumber(attrName)
            return ele
        except NoSuchElementException:
            return self._attributeBonusSmallNumber(attrName)

    def attributeScore(self, attrName):
        try:
            ele = self._attributeBonusBigSign(attrName)
            return self._attributeSmallScore(attrName)
        except NoSuchElementException:
            return self._attributeBigScore(attrName)

    def saveBonusSign(self, saveName):
        return self.parent.saveByName(saveName).find_element_by_xpath('./div[4]/span/span[1]')

    def saveBonusNumber(self, saveName):
        return self.parent.saveByName(saveName).find_element_by_xpath('./div[4]/span/span[2]')

    def skillSign(self, skillName):
        try:
            ele = self.parent.skillByName(skillName).find_element_by_xpath('./div[4]/span/span[1]')
            return ele
        except NoSuchElementException:
            return self.parent.skillByName(skillName).find_element_by_xpath('./div[5]/span/span[1]')

    def skillBonus(self, skillName):
        try:
            ele =  self.parent.skillByName(skillName).find_element_by_xpath('./div[4]/span/span[2]')
            return ele
        except NoSuchElementException:
            return self.parent.skillByName(skillName).find_element_by_xpath('./div[5]/span/span[2]')

    def skillMod(self, skillName):
        return self.parent.skillByName(skillName).find_element_by_xpath('./div[2]')

    def spellButtonNoWait(self):
        return driver.find_element_by_xpath('//section/div/div/div[2]/div/div[3]/div[6]/div/div[2]/div[1]/div[2]/span')

        ### SPELL LEVELS INCLUDES CANTRIPS AT INDEX 0!!!!
                                                          
    def allSpellLevels(self):
        return self.spellsParent().find_elements_by_xpath('./div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div')
                                           
    def spellSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div[1]/div/div')

    def usedSlotsByLevel(self, spellLevel):
        return self.allSpellLevels()[spellLevel].find_elements_by_xpath('./div/div/div/div/div[@class="ct-slot-manager__slot ct-slot-manager__slot--used"]')

class ElementActions(ChildElements):
    def __init__(self):
        self.children = ChildElements()

    def combineSign(self, sign, integer):
        if (sign == '-'):
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

    def getAttributeNames(self):
        attributeList = []
        for i in (self.children.attributeNames()):
            attributeList.append(f'{i.text[0:3]}')
        return attributeList

    def getSaveNames(self):
        saveList = []
        for i in (self.children.saveNames()):
            saveList.append(i.text)
        return saveList
    
    def getSaveBonus(self, saveName):
        return self.combineSign(self.children.saveBonusSign(saveName).text, self.children.saveBonusNumber(saveName).text)

    def isSaveBonusEqual(self, saveName):
        if (self.getAttributeBonus(saveName) != self.getSaveBonus(saveName)):
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
        if(self.getAttributeBonus(skillMod) != self.getSkillBonus(skillName)):
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

    def getCharacterName(self):
        return self.children.characterName().text

    def getCurrentHp(self):
        return self.children.currentHp().text

    def getMaxHp(self):
        return self.children.maxHp().text

    def getCombinedHpData(self):
        return f'{ele.getCurrentHp()}/{ele.getMaxHp()}'

    def getProficiencyBonus(self):
        return f'+{self.children.proficiencyBonus().text}'

    def getArmorClass(self):
        return self.children.armorClass().text

    def getSpeed(self):
        return f'{self.children.speed().text}ft.'

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

# This method formats Saving Throws into 2 columns if there is more than 3 that need to be displayed.
    
    def fullSaveBlock(self):
        smallSaveBlock = self.getStandardSaveBlock()
        allSaves = '----------------------------------------\nSAVES\n'
        if len(smallSaveBlock) > 3:
            fullSaveBlock = self.getStandardSaveBlock()
            for i in range(0, int(len(fullSaveBlock)/2)):
                allSaves += f'{fullSaveBlock[i]}\t{fullSaveBlock[i+3]}\n'
        else:
            for i in range(0, int(len(smallSaveBlock))): 
                allSaves += smallSaveBlock[i] + '\n'
        return allSaves

    def allSkillsBlock(self):
        allSkills = '----------------------------------------\nSKILLS\n'
        for skillName in self.getSkillNames():
            if not self.isSkillBonusEqual(skillName):
                allSkills += (f'{skillName:<18} {self.getSkillMod(skillName)}   {"{:+}".format(int(self.getSkillBonus(skillName)))}\n')
        return allSkills

    def allSpellsBlock(self):
        self.children.spellButtonNoWait().click
        allSpells = '----------------------------------------\nSPELLS SLOTS\nLevel  Total  Used  Available\n'
        for i in range(1, self.getNumSpellsPerLevel()):
            allSpells += (f'{i:<6} {self.getSlotsEachLevel(i):<6} {self.getUsedSlots(i):<5} {self.getAvailableSlots(i)}\n')
        return allSpells

for h in campaignCharacter:
    driver.get(f'https://www.dndbeyond.com/characters/{h}/json')
    ele = ElementActions()
    
    print(ele.getCharacterName())
    print('HP:',ele.getCombinedHpData(), 'AC:', ele.getArmorClass(), 'Speed:', ele.getSpeed(), 'Prof:', ele.getProficiencyBonus())
    fullAttributeBlock = ele.combineAttrNameAndScore()
    for i in range(0, len(fullAttributeBlock), int(len(fullAttributeBlock)/2)):
        print(fullAttributeBlock[i], fullAttributeBlock[i+1], fullAttributeBlock[i+2])
    print(ele.fullSaveBlock())
    print(ele.allSkillsBlock())
    print(ele.allSpellsBlock())
    print('\n=========================================================')
