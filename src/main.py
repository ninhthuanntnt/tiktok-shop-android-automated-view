import pyautogui
import time
import logging

def locateOnScreenWithoutException(imagePath, region=None, confidence=0.7):
  try:
    if region == None:
      return pyautogui.locateOnScreen(imagePath, confidence=confidence, grayscale=True)
    else:
      return pyautogui.locateOnScreen(imagePath, region=region, confidence=confidence, grayscale=True)
  except Exception as e:
    logging.error('Error while locating image on screen', e)
    return None

def waitAndGetCenterPositionOfImage(imagePath, timeout=30, region=None, confidence=0.7):
  print('Waiting for image to appear', imagePath, region)
  position = locateOnScreenWithoutException(imagePath, region, confidence)
  while position == None and timeout > 0:
    position = locateOnScreenWithoutException(imagePath, region, confidence)
    time.sleep(1)
    timeout -= 1
  print('Found the image', imagePath)
  return pyautogui.center(position)

def waitForImage(imagePath, timeout=30, region=None, confidence=0.7):
  logging.info('Waiting for image to appear', imagePath, region, confidence)
  position = locateOnScreenWithoutException(imagePath, region, confidence)
  while position == None and timeout > 0:
    position = locateOnScreenWithoutException(imagePath, region, confidence)
    time.sleep(1)
    timeout -= 1
  logging.info('Found the image', imagePath, region)

def clickOnImage(imagePath, timeout=30, region=None, confidence=0.7):
  position = waitAndGetCenterPositionOfImage(imagePath, timeout, region, confidence)
  pyautogui.click(position)

# Start application =======================================

# Step 1 - Open Tiktok
# positionOfTikTokIcon = clickOnImage('./assets/tiktok-icon.png', region=(0, 30, 540, 960))

# Step 2 - Click on the search icon
# waitForImage('./assets/tiktok-add-icon.png', region=(0, 30, 540, 960))
# print('Found the add icon - Tiktok has opened')
# waitForImage('./assets/tiktok-search-icon.png', region=(0, 30, 540, 960))

# waitForImage('./assets/tiktok-add-icon.png')

# pyautogui.screenshot('screenshot.png', region=(0, int(30), int(540), int(960)))
# pyautogui.locateOnScreen('./assets/tiktok-icon.png', grayscale=True, confidence=0.3)
position = pyautogui.locateOnScreen('./assets/tiktok-icon.png', region=(0, 30, 540, 960), grayscale=True, confidence=0.7)
pyautogui.moveTo(position)
