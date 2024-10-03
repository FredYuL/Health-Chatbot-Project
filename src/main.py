from flask import Flask, request, jsonify
from nlp_processing import process_input
from calorie_query import query_calorie
from plan_generator import generate_plan

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    intent, entities = process_input(user_input)
    
    if intent == 'calorie_query':
        food_item = entities.get('food_item')
        calories = query_calorie(food_item)
        response = f"{food_item}的热量是{calories}千卡。"
    elif intent == 'plan_request':
        goal = entities.get('goal')
        plan = generate_plan(goal)
        response = plan
    else:
        response = "抱歉，我无法理解您的请求。请您尝试询问食物热量或请求减肥/增肌计划。"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
