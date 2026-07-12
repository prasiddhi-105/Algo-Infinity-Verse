from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FlaskModule(db.Model):
    __tablename__ = 'flask_modules'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0)
    
    # Relationship to get all topics under this module
    topics = db.relationship('FlaskTopic', backref='module', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Module {self.title}>'

class FlaskTopic(db.Model):
    __tablename__ = 'flask_topics'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('flask_modules.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(50), default='Medium')
    order = db.Column(db.Integer, default=0)
    
    # Relationship to get all quiz questions under this topic
    quizzes = db.relationship('FlaskQuizQuestion', backref='topic', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Topic {self.title}>'

class FlaskQuizQuestion(db.Model):
    __tablename__ = 'flask_quiz_questions'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('flask_topics.id'), nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False) # Store 'A', 'B', 'C', or 'D'

    def __repr__(self):
        return f'<QuizQuestion {self.id}>'