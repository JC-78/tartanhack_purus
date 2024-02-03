import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


# TOP 20 HARMFUL INGREDIENTS
harmful_ingredients = ['Avobenzone', 'Isopropyl Alcohol', 'SLS', 'Sodium Lauryl Sulfate', 'SLES', 
                       'Sodium Laureth Sulfate', 'TEA', 'Triethanolamine', 'PEG', 
                        'Polyethylene glycol', 'synthetic colors', 'isopropyl methyphnol', 
                         'sorbic acid', 'hormone', 'dht', 'dibutyl hydroxy toluene', 
                          'paraben', 'triclosan', 'BHA', 'butyl hydroxy anisole', 
                           'oxy benzone', 'imidazolidinyl urea', 'diazolidinyl urea', 'dmdm hydantoin',
                           'mineral oil', 'tymol', 'triisopropanolamine', 'synthetic fragrance', 'fragrance', 
                           'phenoxy ethanol']

harmful_ingrd_dict = {'dibutyl hydroxy toluene' : 'Causes hair loss, skin hypersensitivity, and allergies',
                      'dht':'Causes hair loss, skin hypersensitivity, and allergies',
                      'bht' : 'Causes hair loss, skin hypersensitivity, and allergies',
                      'mineral oil' : 'Causes acne, inhibits toxin discharge, interferes with cell growth, and skin aging',
                      'butyl hydroxy anisole' : 'Causes genetic abnormalities, allergies, and cancer',
                      'Sodium Lauryl Sulfate' : 'Causes cataracts, dry skin, and cancer',
                      'Sodium Laureth Sulfate' :'Causes cataracts, dry skin, and cancer',
                      'SLS' : 'Causes cataracts, dry skin, and cancer',
                      'sorbic acid' : 'Stimulates the skin membrance and causes allergies',
                      'avobenzene' : 'Generation of active oxygen, DNA damange',
                      'Avobenzone' : 'Generation of active oxygen, DNA damange',
                      'oxybenzone' : 'Causes respiratory and digestive disorders and allergies',
                      'benzophenone-3' : 'Causes respiratory and digestive disorders and allergies',
                      'imidazolidinyl urea' : 'Causes skin inflammation',
                      'diazolidinyl urea' :  'Causes skin inflammation',
                      'dmdm hydantoin' : 'Causes skin inflammation',
                      'isopropyl methyphnol' : 'Causes strong irritation, swelling, acne, and hives',
                      'isopropyl alcohol' : 'Causes headache, flushing, dizziness, and vomiting when ingested or inhaled',
                      'fragrance' : 'Vaguely describe all fragrants, so specific identity unknown',
                      'tamol' : 'Causes vomiting, diarrhea, headache, and tinnitus. Strong skin irritation',
                      'triethanolamine' : 'Causes eye disease, hair and skin dryness',
                      'TEA' : 'Causes eye disease, hair and skin dryness',
                      'triisopropanolamine' : 'Causes skin dryness by removing excessive sebum',
                      'triclosan' : 'An endocrine disruptor that causes decreased immunity and fertility',
                      'paraben' : 'Cause of contact dermatitis, allergies, blemishes, and wrinkles',
                      'phenoxyethanol' : 'Causes  irritation', 
                      'polyethylene glycol' : 'Causes liver and kidney disorders and allergies', 
                      'PEG' : 'Causes liver and kidney disorders and allergies',
                      'hormones' : 'Substances similar to medicines that causes precocious puberty in girls'
                    }


allergen = ['latex', 'Amyl cinnamal', 'Amylcinnamyl alcohol', 'Anisyl alcohol', 'Benzyl alcohol',
             'Benzyl benzoate', 'Benzyl cinnamate', 'Benzyl salicylate', 'Cinnamyl alcohol',
               'Cinnamaldehyde', 'Citral', 'Citronellol', 'Coumarin', 'Eugenol', 'Farnesol', 
               'Geraniol', 'Hexyl cinnamaladehyde', 'Hydroxycitronellal', 'Hydroxyisohexyl 3-cyclohexene carboxaldehyde',
               'HICC', 'Lyral', 'Isoeugenol', 'Lilial', 'd-Limonene', 'Linalool', 'Methyl 2-octynoate', 'g-Methylionone',
               'Oak moss extract', 'Tree moss extract', 'Methylisothiazolinone','MIT', 'Methylchloroisothiazolinone', 'CMIT', 
               'Formaldehyde', 'Bronopol', '2-bromo-2-nitropropane-1,3-diol' , '5-bromo-5-nitro-1', '3-dioxane', 'Diazolidinyl urea', 
               'DMDM hydantoin', 'dimethylol', 'dimethylhydantoin', 'Imidazolidinyl urea', 'Sodium hydroxymethylglycinate',
               'Quaternium-15', 'Dowicil 200', 'hexaminium chloride', 'p-phenylenediamine', 'ppd', 'coal-tar', 'nickel', 'gold']


rejuvenate = ['Vitamin A', 'peptides', 'vitamins E', 'vitamin C', 'AHA', 'hyaluronic acid']
hydration = ['Hyaluronic acid', 'panthenol', 'niacinamide', 'glycerin', 'squalene', 'lactic acid', 'omega-rich oils', 'vitamin A']
redness = ['Centella asiatica', 'hemp seed extract', 'probiotics', 'vitamin B', 'hydrolyzed algin', 'chamomile']
congested = ['Salicylic acid', 'clay','jojoba oil', 'linoleic oil', 'hyaluronic acid', 'niacinamide']
pigmentation = ['Niacinamide', 'vitamin C', 'kojic acid', 'AHA']
textured = ['vitamin A', 'AHA', 'peptides', 'vitamin C']




# ALLERGEN 

# # URL of the page to scrape
# url = 'https://www.fda.gov/cosmetics/cosmetic-ingredients/allergens-cosmetics#common'

# # Fetch the content of the webpage
# response = requests.get(url)
# webpage = response.content

# # Parse the HTML content
# soup = BeautifulSoup(webpage, 'html.parser')

# # Find all the 'panel-body' div elements and take only the first five
# allergen_panels = soup.find_all('div', class_='panel-body')[:5]

# # Predefined titles for the keys
# titles = ['Natural Rubber', 'Fragrance', 'Preservative', 'Dye', 'Metal']

# # Initialize a dictionary to store the allergens with the predefined titles
# allergens_dict = {}

# # Iterate over each of the first five panels to extract allergens
# for title, panel in zip(titles, allergen_panels):
#     allergens_list = [li.text.strip() for li in panel.find_all('li')]
#     allergens_dict[title] = allergens_list

# # Print or process the allergens dictionary as needed
# for title, allergens in allergens_dict.items():
#     print(f"{title}: {allergens}\n")


# def check_ingredient_safety(ingredients_list, harmful_ingrd_dict):
#     # Convert the keys in the harmful_ingrd_dict to lowercase for case-insensitive comparison
#     harmful_ingrd_dict_lower = {k.lower(): v for k, v in harmful_ingrd_dict.items()}

#     results = {}
#     for ingredient in ingredients_list:
#         # Convert the ingredient to lowercase for case-insensitive comparison
#         ingredient_lower = ingredient.lower()
#         if ingredient_lower in harmful_ingrd_dict_lower:
#             results[ingredient] = {'Status': 'Harmful', 'Description': harmful_ingrd_dict_lower[ingredient_lower]}
#         else:
#             results[ingredient] = {'Status': 'Safe', 'Description': 'No known harm information.'}
    
#     return results

# # Example usage
# ingredients_to_check = ['Avobenzone', 'Homosalate', 'Octisalate', 'Octocrylene']
# safety_results = check_ingredient_safety(ingredients_to_check, harmful_ingrd_dict)
# for ingredient, result in safety_results.items():
#     print(f"{ingredient}: {result['Status']} - {result['Description']}")

# def check_ingredient_details(ingredients_list):
#     # Assume all your lists and dictionaries are defined here
    
#     results = {}
#     for ingredient in ingredients_list:
#         ingredient_lower = ingredient.lower().replace(" ", "")
#         details = {"Safety": "Safe", "Benefits": []}
        
#         # Check for safety
#         if ingredient_lower in (i.lower().replace(" ", "") for i in harmful_ingredients):
#             details["Safety"] = harmful_ingrd_dict.get(ingredient, "Harmful ingredient with no specific description available.")
#         if ingredient_lower in (i.lower().replace(" ", "") for i in allergen):
#             details["Safety"] = "Known allergen."
        
#         # Check for benefits
#         for list_name, ingredients in {'Rejuvenate': rejuvenate, 'Hydration': hydration, 'Redness': redness, 'Congested': congested, 'Pigmentation': pigmentation, 'Textured': textured}.items():
#             if ingredient_lower in (i.lower().replace(" ", "") for i in ingredients):
#                 details["Benefits"].append(list_name)
        
#         results[ingredient] = details
    
#     return results


# def print_ingredient_details(details):
#     for ingredient, info in details.items():
#         print(f"Ingredient: {ingredient}")
#         print(f"  Safety: {info['Safety']}")
#         if info['Benefits']:
#             benefits_str = ', '.join(info['Benefits'])
#             print(f"  Benefits: {benefits_str}")
#         else:
#             print("  Benefits: None")
#         print("")  # Add an empty line for better readability between ingredients



# # Example usage
# ingredients_to_check = ['Avobenzone', 'Homosalate', 'Octisalate', 'Octocrylene', 'Niacinamide', 'fhduhf']
# safety_results = check_ingredient_details(ingredients_to_check)
# print_ingredient_details(safety_results)

# Convert the keys in the harmful_ingrd_dict to lowercase for case-insensitive comparison


def check_ingredients(ingredients_list):
    # Assuming all relevant lists and dictionaries are defined here
    
    # Initialize results dictionary
    results = {}
    harmful_ingrd_dict_lower = {k.lower(): v for k, v in harmful_ingrd_dict.items()}

    for ingredient in ingredients_list:
        # Normalize ingredient name for comparison
        ingredient_lower = ingredient.lower()
        
        # Check safety
        safety_info = harmful_ingrd_dict_lower.get(ingredient_lower, 'Safe')
        
        # Check benefits
        benefit_categories = []
        for category, ingredients in {'Rejuvenate': rejuvenate, 'Hydration': hydration, 'Redness': redness, 'Congested': congested, 'Pigmentation': pigmentation, 'Textured': textured}.items():
            if ingredient_lower in (i.lower() for i in ingredients):
                benefit_categories.append(category)
        
        # Compile results
        results[ingredient] = {
            'Safety': safety_info,
            'Benefits': benefit_categories if benefit_categories else ['No specific benefit identified']
        }
    
    # Print formatted results
    for ingredient, info in results.items():
        print(f"Ingredient: {ingredient}")
        print(f"  Safety: {info['Safety']}")
        benefits_str = ', '.join(info['Benefits'])
        print(f"  Benefits: {benefits_str}\n")

def count_harmful_ingredients(ingredients_list):
    # Normalize the harmful_ingredients list for case-insensitive comparison
    harmful_ingredients_lower = [ingredient.lower() for ingredient in harmful_ingredients]
    
    # Count harmful ingredients
    harmful_count = sum(1 for ingredient in ingredients_list if ingredient.lower() in harmful_ingredients_lower)
    
    print(f"Top 20 harmful ingredients count: {harmful_count} \n")

def count_allergen_ingredients(ingredients_list):
    # Normalize the harmful_ingredients list for case-insensitive comparison
    allergen_lower = [ingredient.lower() for ingredient in allergen]
    
    # Count harmful ingredients
    harmful_count = sum(1 for ingredient in ingredients_list if ingredient.lower() in allergen_lower)
    
    print(f"FDA compiled common allergen count: {harmful_count} \n")


# Example usage with a combined approach
# ingredients_to_check = ['Avobenzone', 'Homosalate', 'Octisalate', 'Octocrylene', 'Niacinamide', 'fhsjdfns']
# count_allergen_ingredients(ingredients_to_check)
# count_harmful_ingredients(ingredients_to_check)
# check_ingredients(ingredients_to_check)
