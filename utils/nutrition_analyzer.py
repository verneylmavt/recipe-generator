# utils/nutrition_analyzer.py
import requests

class NutritionAnalyzer:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    
    def get_nutrition(self, ingredients):
        headers = {
            'x-app-id': self.app_id,
            'x-app-key': self.app_key,
            'Content-Type': 'application/json'
        }
        data = {
            'query': ', '.join(ingredients),
            'timezone': 'US/Eastern'
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception: {req_err}")
            return None
    
    def parse_nutrition(self, nutrition_data):
        if not nutrition_data or 'foods' not in nutrition_data:
            return {}
        total = {'calories': 0, 'protein': 0, 'fat': 0, 'carbohydrates': 0}
        for item in nutrition_data.get('foods', []):
            total['calories'] += item.get('nf_calories', 0)
            total['protein'] += item.get('nf_protein', 0)
            total['fat'] += item.get('nf_total_fat', 0)
            total['carbohydrates'] += item.get('nf_total_carbohydrate', 0)
        return total