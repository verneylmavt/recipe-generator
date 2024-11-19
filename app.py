# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from utils.recipe_generator import RecipeGenerator
from utils.nutrition_analyzer import NutritionAnalyzer
from utils.image_recognition import ImageRecognizer
import os
from werkzeug.utils import secure_filename
import re

app = Flask(__name__)
app.secret_key = 'your_secure_secret_key'

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

rg = RecipeGenerator('data/ingredients.csv')
na = NutritionAnalyzer(app_id='b96de32c', app_key='af54aba71c0826ab39952ca4fb2e489a')
ir = ImageRecognizer()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def sanitize_input(ingredients_input):
    pattern = re.compile(r'^[a-zA-Z0-9 ,\'-]+$')
    return pattern.match(ingredients_input)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = []
        if 'image' in request.files and request.files['image'].filename != '':
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                try:
                    file.save(filepath)
                except Exception as e:
                    flash('Failed to save uploaded image.', 'danger')
                    return redirect(url_for('index'))
                recognized_ingredients = ir.recognize_image(filepath)
                if recognized_ingredients:
                    ingredients.extend(recognized_ingredients)
                else:
                    flash('Could not recognize ingredients from the image.', 'danger')
            else:
                flash('Invalid image file. Allowed types are png, jpg, jpeg, gif.', 'danger')
        
        ingredients_input = request.form.get('ingredients', '')
        if ingredients_input:
            if not sanitize_input(ingredients_input):
                flash('Invalid characters in ingredients input.', 'danger')
                return redirect(url_for('index'))
            user_ingredients = [ing.strip().lower() for ing in ingredients_input.split(',') if ing.strip()]
            ingredients.extend(user_ingredients)
        
        ingredients = list(set(ingredients))
        
        if not ingredients:
            flash('Please provide at least one ingredient.', 'warning')
            return redirect(url_for('index'))

        try:
            recipe = rg.find_recipe(ingredients)
        except Exception as e:
            flash('An error occurred while finding the recipe.', 'danger')
            return redirect(url_for('index'))
        
        if not recipe:
            flash('No recipe found with the given ingredients.', 'danger')
            return redirect(url_for('index'))
        
        recipe_name, recipe_ingredients, recipe_steps, total_time = recipe
        try:
            nutrition_data = na.get_nutrition(recipe_ingredients)
            nutrition_summary = na.parse_nutrition(nutrition_data) if nutrition_data else {}
        except Exception as e:
            flash('An error occurred while fetching nutritional information.', 'danger')
            nutrition_summary = {}
        
        return render_template('recipe.html',
                               name=recipe_name,
                               ingredients=recipe_ingredients,
                               steps=recipe_steps,
                               total_time=total_time,
                               nutrition=nutrition_summary)
    return render_template('index.html')

@app.route('/api/ingredients', methods=['GET'])
def get_ingredients():
    unique_ingredients = set()
    for ingredients_list in rg.df['ingredients']:
        unique_ingredients.update(ingredients_list)
    return jsonify(sorted(list(unique_ingredients)))

if __name__ == '__main__':
    app.run(debug=True)