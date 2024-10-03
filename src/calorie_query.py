import pandas as pd

def query_calorie(food_item):
    df = pd.read_csv('data/food_nutrition.csv')
    result = df[df['食物'] == food_item]
    if not result.empty:
        calories = result.iloc[0]['热量（千卡）']
        return calories
    else:
        return "未知"
