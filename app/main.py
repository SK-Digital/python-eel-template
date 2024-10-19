import eel

eel.init('app')

@eel.expose
def python_function():
    return "Hello from Python!"

eel.start('index.html', size=(800, 600))
