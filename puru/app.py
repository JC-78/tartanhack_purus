from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

from text_extraction import extract_image_to_text
from summarize import summarize
from processing import count_allergen_ingredients, count_harmful_ingredients, check_ingredients
import db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html', caption='', description='')

@app.route('/display_image/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def get_dynamic_img_path(image_filename):
    return os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

@app.route('/query/<ingredient>', methods=['GET'])
def query(ingredient):
    ingredient = ingredient.lower()
    return {
        "harmful_level": int(db.harmful_level(ingredient)),
        "comment": db.comment(ingredient),
        "benefit": db.benefit(ingredient),
        "url": db.url(ingredient)
    }

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        image_file = request.files['file']

        if image_file.filename == '':
            return redirect(request.url)

        # Process the image file
        image_filename = secure_filename(image_file.filename)
        image_file.save(get_dynamic_img_path(image_filename))
        print("image file saved")
        # Use the dynamically generated img_path
        img_path = get_dynamic_img_path(image_filename)
        extract_image_to_text(img_path) 
        print("written to output.txt")
        ingredients = summarize()
        print(">>>>>>>>>>>>>>ingredients")
        print(ingredients)
        allergen=count_allergen_ingredients(ingredients)
        harmful=count_harmful_ingredients(ingredients)
        ingredients=check_ingredients(ingredients)
        # print("ingredient result",ingredients)
        image=""
        for i in ingredients:
            image+=i
        return render_template('index.html', caption=harmful, description=allergen, image=image)
    else:
        caption = 'Unexpected response from the server'
        return render_template('index.html', caption=caption, description='', image='')


if __name__ == '__main__':
    app.run(debug=True)
