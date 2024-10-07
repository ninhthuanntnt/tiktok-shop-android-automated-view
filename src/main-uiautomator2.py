import uiautomator2 as u2
import time
import random

adbConnectString = '192.168.1.20:36741'
print('Connectting to device')
d = u2.connect(adbConnectString)
print('Connected to device', d.info)
width, height = d.window_size()
print('Device screen size', width, height)

shopNameToSearch="Tabalo"
matchedShopName="Tabalo Camping ⛺️"
addButtonXpath = '//*[@resource-id="com.zhiliaoapp.musically:id/ilb"]'
searchButtonXpath = '//*[@resource-id="com.zhiliaoapp.musically:id/fv7"]'
searchInputXpath = '//*[@resource-id="com.zhiliaoapp.musically:id/et2"]'
captchaInputXpath = '//*[@resource-id="com.zhiliaoapp.musically:id/dbs"]'
shopTabXpath = '//*[@content-desc="Shop"]'
matchedShopXpath = f'//*[@content-desc="{matchedShopName}"]'
shopTabInsideTheMatchedShopXpath = '//*[@resource-id="com.zhiliaoapp.musically:id/a_k"]'
shopItemsXpath = '//com.lynx.tasm.behavior.ui.view.UIComponent'

def restartApp():
  d.app_stop('com.zhiliaoapp.musically')
  d.app_start('com.zhiliaoapp.musically')

def bypassCaptcha():
  d.xpath(captchaInputXpath).wait(timeout=5)
  print('Found the captcha input')
  
  restartApp()
  print('Restarted the app')
  startViewShop()

def detectCaptcha():
  captchaInput = d.xpath(captchaInputXpath)
  if captchaInput.exists:
    bypassCaptcha()

def swipeToNextVideoTikTok(swipeUp=True):
  time.sleep(1)
  randomWidthMinus = random.randint(0, 50)
  randomHeightMinus = random.randint(0, 50)
  centerOfScreen = (width / 2 - randomWidthMinus, height / 2 - randomHeightMinus)
  upperCenterOfScreen = (width / 2 - randomHeightMinus, height / 4 - randomHeightMinus)
  if swipeUp:
    d.swipe(centerOfScreen[0], centerOfScreen[1], upperCenterOfScreen[0], upperCenterOfScreen[1], 0.2)
  else:
    d.swipe(upperCenterOfScreen[0], upperCenterOfScreen[1], centerOfScreen[0], centerOfScreen[1], 0.2)

def startWarmUp():
  waitUntilTikTokOpened()
  
  randomNumberOfSwipeUp = random.randint(1, 5)
  print('Random number of swipe up', randomNumberOfSwipeUp)
  for i in range(randomNumberOfSwipeUp):
    swipeToNextVideoTikTok()

  randomNumberOfSwipeDown = randomNumberOfSwipeUp - random.randint(1, 3)
  print('Random number of swipe down', randomNumberOfSwipeDown)
  for i in range(randomNumberOfSwipeDown):
    swipeToNextVideoTikTok(False)

def waitUntilTikTokOpened():
  d.xpath(addButtonXpath).wait(timeout=5)
  detectCaptcha()
  print('Found the add icon - Tiktok has opened')

def waitUntilSelectorAppear(selector, timeout=10):
  d.xpath(selector).wait(timeout=timeout)
  detectCaptcha()
  print('Found the selector', selector)

def clickOnSelector(selector):
  d.xpath(selector).click()
  detectCaptcha()
  print('Clicked on selector', selector)

def clickOnSelectorWithIndex(selector, index):
  d.xpath(selector).all()[index].click()
  detectCaptcha()
  print('Clicked on selector with index', selector, index)

def inputText(selector, text):
  d.xpath(selector).set_text(text)
  detectCaptcha()
  print('Typed the text', text)

def startClickAnItemInShop():
  waitUntilSelectorAppear(shopItemsXpath, timeout=5)
  numberOfVisibleItem = d.xpath(shopItemsXpath).all().__len__()
  print('Number of visible item', numberOfVisibleItem)
  
  randomIndex = random.randint(2, numberOfVisibleItem - 1)
  print('Random index of item to pick', randomIndex)

  clickOnSelectorWithIndex(shopItemsXpath, randomIndex)

def startViewShop():
  waitUntilTikTokOpened()

  waitUntilSelectorAppear(searchButtonXpath, timeout=5)
  clickOnSelectorWithIndex(searchButtonXpath, 1)
  print('Found the search icon - Tiktok has been ready to search')

  waitUntilSelectorAppear(searchInputXpath, timeout=5)
  clickOnSelector(searchInputXpath)
  print('Found the search input - Tiktok has opened')

  inputText(searchInputXpath, shopNameToSearch)
  print('Typed the shop name and searched', shopNameToSearch)
  d.press('enter')

  time.sleep(2)
  waitUntilSelectorAppear(shopTabXpath, timeout=5)
  clickOnSelector(shopTabXpath)
  print('Clicked on the shop tab')

  waitUntilSelectorAppear(matchedShopXpath, timeout=5)
  clickOnSelectorWithIndex(matchedShopXpath, 0)
  print('Clicked on the matched shop', matchedShopName)

  waitUntilSelectorAppear(shopTabInsideTheMatchedShopXpath, timeout=5)
  clickOnSelector(shopTabInsideTheMatchedShopXpath)
  print('Clicked on the shop tab inside the shop', matchedShopName)

  startWarmUp()

  startClickAnItemInShop()

  startWarmUp()


try:
  restartApp()
  startWarmUp()
  startViewShop()
except Exception as e:
  print('Error while running the script', e)
  restartApp()