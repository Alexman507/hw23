from app import create_app

if name == '__main__':
    app = create_app()
    app.run(port=25000)