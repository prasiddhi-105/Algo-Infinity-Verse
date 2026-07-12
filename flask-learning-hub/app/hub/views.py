from flask import Blueprint, render_template, abort
from app.models import FlaskModule, FlaskTopic

hub_bp = Blueprint('hub', __name__, template_folder='templates')

@hub_bp.route('/')
def module_list():
    # Fetch all modules ordered by their sequence field
    modules = FlaskModule.query.order_by(FlaskModule.order).all()
    return render_template('hub/module_list.html', modules=modules)

@hub_bp.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    topic = FlaskTopic.query.get_or_404(topic_id)
    # Fetch all other topics in the same module to render sidebar navigation elements
    sidebar_topics = FlaskTopic.query.filter_by(module_id=topic.module_id).order_by(FlaskTopic.order).all()
    
    return render_template('hub/topic_detail.html', 
                           topic=topic, 
                           sidebar_topics=sidebar_topics, 
                           quizzes=topic.quizzes)