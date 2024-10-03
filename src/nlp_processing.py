import jieba

def process_input(user_input):
    words = list(jieba.cut(user_input))
    intent = None
    entities = {}

    if '热量' in words or '卡路里' in words:
        intent = 'calorie_query'
        # 简单提取食物名称，实际应用中应使用实体识别模型
        food_item = words[0]  # 假设食物名称在句首
        entities['food_item'] = food_item
    elif '减肥' in words:
        intent = 'plan_request'
        entities['goal'] = '减肥'
    elif '增肌' in words:
        intent = 'plan_request'
        entities['goal'] = '增肌'
    else:
        intent = 'unknown'
    
    return intent, entities
