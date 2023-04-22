import pyautogui
import autoit
import time

images_folder = "images/"
enter = (1172, 707)

# Set the location of the image to be searched for
image_locations = {
    images_folder + 'single.png': (1108, 539),
    images_folder + 'double.png': (1165, 538),
    images_folder + 'large.png': (1151, 596),
    images_folder + 'chips.png': (1129, 659),
    images_folder + 'drink.png': (1190, 654)
}

# Set the coordinates of the area on the screen to search for the image
area = (1000, 337, 600, 220) # left, top, width, height

# If the image is found within the specified area, click on a particular section of the screen
while True:
    # Search for the image within the specified area
    found = False
    for image_name, click_location in image_locations.items():
        image_position = pyautogui.locateOnScreen(image_name, region=area, confidence=0.97)
        if image_position is not None:
            found = True
            break
    
    if found:
        for image_name, click_location in image_locations.items():
            image_position = pyautogui.locateOnScreen(image_name, region=area, confidence=0.97)
            if image_position is not None:
                # Click on a section of the screen relative to the center of the image
                autoit.mouse_move(*click_location)
                pyautogui.click()

        autoit.mouse_move(*enter)
        pyautogui.click()
        time.sleep(1)