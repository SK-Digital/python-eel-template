# Python Eel-Tailwind Template

A simple template for creating desktop applications with Python Eel and Tailwind CSS.

## Features

- Python backend with Eel for desktop app creation
- Tailwind CSS for styling
- Simple structure for easy customization

## Prerequisites

- Python 3.6+
- Node.js and npm

## Setup

1. Clone this repository:   ```
   git clone https://github.com/yourusername/python-eel-tailwind-template.git
   cd python-eel-tailwind-template   ```

2. Create and activate a virtual environment:   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`   ```

3. Install Python dependencies:   ```
   pip install -r requirements.txt   ```

4. Install Node.js dependencies:   ```
   npm install   ```

5. Build Tailwind CSS:   ```
   npm run build-css   ```

## Running the Application

To run the application in development mode:

```
python main.py

```

## Customizing the Application

- Edit `app/index.html` to modify the HTML structure
- Edit `app/static/css/tailwind.css` to add custom CSS
- Edit `app/static/js/main.js` to add custom JavaScript
- Edit `app/python/logic.py` to add Python functions
- Expose Python functions in `main.py` using the `@eel.expose` decorator

## Building a Standalone Application

To create a standalone executable using PyInstaller:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --name=YourAppName --add-data="app:app" --windowed main.py
   ```

3. The executable will be created in the `dist/YourAppName` directory.

## Notes

- Make sure to rebuild the Tailwind CSS file (`npm run build-css`) after making changes to the HTML or Tailwind classes.
- When adding new Python files or functions, remember to expose them using `@eel.expose` and import them in `main.py`.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are installed correctly.
2. Check the console for any error messages.
3. Make sure the file paths in `main.py` are correct for your system.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Eel](https://github.com/ChrisKnott/Eel)
- [Tailwind CSS](https://tailwindcss.com/)
- [PyInstaller](https://www.pyinstaller.org/)
