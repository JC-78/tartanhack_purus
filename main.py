from text_extraction import extract_image_to_text
from summarize import summarize
from processing import count_allergen_ingredients, count_harmful_ingredients, check_ingredients

if __name__ == "__main__":
    img_path = '/Users/joonghochoi/Desktop/purus OCR preprocessing/white.png'
    extract_image_to_text(img_path)
    ingredients = summarize()
    print(">>>>>>>>>>>>>>ingredients")
    print(ingredients)
    count_allergen_ingredients(ingredients)
    count_harmful_ingredients(ingredients)
    check_ingredients(ingredients)
