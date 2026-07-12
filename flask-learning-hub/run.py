from app import create_app

app = create_app()

if __name__ == '__main__':
    # Running local server on debug mode for automatic template reload
    app.run(debug=True, port=5000)