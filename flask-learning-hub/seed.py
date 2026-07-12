from app import create_app
from app.models import db, FlaskModule, FlaskTopic, FlaskQuizQuestion

app = create_app()

with app.app_context():
    # Clear existing data to avoid duplicates
    db.drop_all()
    db.create_all()

    # 1. Add a Module
    mod1 = FlaskModule(
        title="Flask Basics & Routing",
        description="Learn the fundamentals of building lightweight apps, setting up routes, and dynamic URL handling.",
        order=1
    )
    db.session.add(mod1)
    db.session.commit() # Commit to generate the module ID for the foreign key

    # 2. Add a Topic
    topic1 = FlaskTopic(
        module_id=mod1.id,
        title="Understanding Flask Routing",
        content=(
            "Flask is a micro-framework because it does not require particular tools or libraries. "
            "At its core, routing maps web requests directly to Python functions using decorators.\n\n"
            "Here is how a standard Flask route operates:\n"
            "1. The Decorator: By prefixing a function with `@app.route('/path')`, you instruct Flask what URL path triggers the code.\n"
            "2. View Function: The function sitting directly underneath the decorator executes whenever the URL matches.\n"
            "3. Return Value: The view function must return a string, response object, or rendered template back to the user's browser."
        ),
        difficulty="Easy",
        order=1
    )
    db.session.add(topic1)
    db.session.commit()

    # 3. Add a Quiz Question
    quiz1 = FlaskQuizQuestion(
        topic_id=topic1.id,
        question_text="Which Python decorator is used to map a URL path to a view function in Flask?",
        option_a="@app.route()",
        option_b="@app.view()",
        option_c="@app.map()",
        option_d="@app.url()",
        correct_option="A"
    )
    db.session.add(quiz1)
    db.session.commit()

    print("🌱 Database seeded successfully with Flask basics!")