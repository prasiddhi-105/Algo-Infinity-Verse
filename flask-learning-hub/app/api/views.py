from flask import Blueprint, jsonify
from app.models import FlaskTopic

api_bp = Blueprint('api', __name__)

@api_bp.route('/topics')
def get_topics():
    # Query all topics along with their preloaded relationships
    topics = FlaskTopic.query.order_by(FlaskTopic.order).all()
    
    api_data = []
    for t in topics:
        # Format the nested quiz questions associated with this specific topic
        quiz_list = []
        for q in t.quizzes:
            quiz_list.append({
                "id": q.id,
                "question_text": q.question_text,
                "option_a": q.option_a,
                "option_b": q.option_b,
                "option_c": q.option_c,
                "option_d": q.option_d
            })
            
        # Assemble the full JSON payload object for the topic
        api_data.append({
            "id": t.id,
            "title": t.title,
            "content": t.content,
            "difficulty": t.difficulty,
            "quizzes": quiz_list
        })
        
    return jsonify(api_data)