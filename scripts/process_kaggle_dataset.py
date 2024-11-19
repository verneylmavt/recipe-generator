import pandas as pd

input_file = "clean_recipes.csv"
output_file = "../data/ingredients.csv"

df = pd.read_csv(input_file, sep=";")

filtered_df = df[['Recipe Name', 'Ingredients']].rename(columns={
    'Recipe Name': 'name',
    'Ingredients': 'ingredients',
    'Directions': 'steps',
    'Total Time': 'total_time'
})

filtered_df['ingredients'] = filtered_df['ingredients'].apply(
    lambda x: str([ingredient.strip() for ingredient in x.split(',')])
)

filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")