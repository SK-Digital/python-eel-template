import eel
import os
from app.python.logic import python_function

# Get the absolute path to the 'app' directory
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')

# Initialize Eel with the correct base directory
eel.init(app_dir)

# Expose the Python function
eel.expose(python_function)

# Start the Eel application
eel.start('index.html', size=(800, 600))
