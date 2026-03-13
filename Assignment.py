import cv2
image = input('Upload the image:')
img = cv2.imread(image)
if img is not None:
    print("Image Loaded Successfully.")
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img1 = input('Would you show the image otherwise save the image: (show/save)')
    if img1 == 'show':
        cv2.imshow('Gray Image', gray_image)#Display the grayscale image in a window.# open the window
        cv2.waitKey(0)#Wait for a key press to close the window.# wait for a key
        cv2.destroyAllWindows()#Close all OpenCV windows.# close the window

    elif img1 == 'save':
        name = input('Enter the name of the image (with extension .jpg/.png): ')
        success = cv2.imwrite(name, gray_image) #Save the image to a new file.#
        if success:
             print("Image Saved Successfully.")
        else:
            print("Failed to save the image.")
    else:
        print("Invalid input. Please enter 'show' or 'save'.")
else:
    print('Error: Image not found.')