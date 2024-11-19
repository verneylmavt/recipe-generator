# utils/recipe_generator.py
import pandas as pd

class RecipeGenerator:
    def __init__(self, ingredients_file):
        self.df = pd.read_csv(ingredients_file)
        required_columns = {'name', 'ingredients', 'steps', 'total_time'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            raise ValueError(f"Missing columns in dataset: {missing}")
        
        self.df['ingredients'] = self.df['ingredients'].apply(eval)
        self.df['ingredients'] = self.df['ingredients'].apply(lambda x: [ing.lower() for ing in x if isinstance(ing, str)])
        self.df['ingredients'] = self.df['ingredients'].apply(lambda x: list(set(x)))
        self.df['steps'] = self.df['steps'].astype(str)
        self.df['steps'] = self.df['steps'].apply(lambda x: [step.strip() for step in x.split('.**') if step.strip()])
        self.df['total_time'] = self.df['total_time'].astype(str)

    def find_recipe(self, available_ingredients):
        available_ingredients = set([ing.lower() for ing in available_ingredients])

        def match_count(recipe_ingredients):
            return len(set(recipe_ingredients).intersection(available_ingredients))

        self.df['match_count'] = self.df['ingredients'].apply(match_count)
        filtered_df = self.df[self.df['match_count'] > 0]

        if filtered_df.empty:
            return None

        best_match = filtered_df.sort_values(by='match_count', ascending=False).iloc[0]

        recipe_name = best_match['name']
        recipe_ingredients = best_match['ingredients']
        recipe_steps = best_match['steps']
        total_time = best_match['total_time']

        return recipe_name, recipe_ingredients, recipe_steps, total_time