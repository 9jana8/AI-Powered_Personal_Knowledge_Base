from flaskapp import create_app

# Create app
app = create_app()

# Run app
if __name__ == '__main__':
    app.run(debug=True)
