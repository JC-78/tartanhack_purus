from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import pytesseract
import subprocess
import cv2
import numpy as np

def extract_image_to_text(png_path):
    # heic_path = '/Users/joonghochoi/Desktop/purus/white_orange.HEIC'
    # png_path = '/Users/joonghochoi/Desktop/purus/white_orange.png'

    # heic_path = '/Users/joonghochoi/Desktop/purus/white.HEIC'
    # png_path = './white.png'

    # Use sips to convert HEIC to PNG
    # subprocess.run(["sips", "-s", "format", "png", heic_path, "--out", png_path])

    # Read the PNG image using PIL
    image = Image.open(png_path)

    # Rotate the image to the right by 90 degrees
    rotated_image = image.rotate(-90, expand=True)  # currently the image is not straight

    text = pytesseract.image_to_string(rotated_image)

    # print("Extracted Text from original image:")
    # print(text)

    # Grayscale Conversion
    gray_image = rotated_image.convert('L')
    gray_array = np.array(gray_image)

    # cv2.imshow('gray', gray_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    text = pytesseract.image_to_string(gray_image)
    # print("Extracted Text from gray image:")
    # print(text)

    #skip thresholding cuz not doing well for us
    # Thresholding to segment the image into binary (black and white) regions -> contrast text and background
    # _, thresh_array = cv2.threshold(gray_array, 128, 255, cv2.THRESH_BINARY)

    # cv2.imshow('thresholded gray', thresh_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Contrast Adjustment. Adjust the contrast of the image to make the text more prominent.
    # enhancer = ImageEnhance.Contrast(rotated_image)
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)  # Adjust the enhancement factor as needed
    enhanced_array = np.array(enhanced_image)
    # cv2.imshow('enhanced_image', enhanced_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # Noise Reduction (Blurring) to reduce unwanted details and improve OCR accuracy.
    blurred_image = enhanced_image.filter(ImageFilter.BLUR)
    blurred_array = np.array(blurred_image)

    # cv2.imshow('blurred_image', blurred_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    text = pytesseract.image_to_string(blurred_image)
    # print("Extracted Text from blurred image:")
    # print(text)
    #skipping this cuz it didn't work out 
    # Inverting Colors: Invert the colors of the image, especially if the text is darker than the background.
    # inverted_image = ImageOps.invert(blurred_image)
    # inverted_array = np.array(inverted_image)

    # cv2.imshow('inverted_image', inverted_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Perform OCR using pytesseract on the preprocessed image
    # text = pytesseract.image_to_string(inverted_image)

    ingredients_index = text.lower().find('ingredients')
    if ingredients_index != -1:
        ingredients_text = text[ingredients_index:]
        
        # Save the extracted text to a text file
        with open('/Users/choo/GithubProjects/CMU_Spring_2024/tartanhack_purus/puru/output.txt', 'w') as text_file:
            text_file.write(ingredients_text)

        print("Saved Ingredients and beyond to output.txt.")
    else:
        print("No 'Ingredients' found in the extracted text.")
