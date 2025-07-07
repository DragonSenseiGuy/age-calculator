# Age Calculator

A simple web application built with Flask that calculates a person's age based on their birthdate. The application provides a user-friendly interface to input a birthdate and receive the calculated age in years and months.

## Features

- Input your birthdate using a date picker.
- Calculates age in years and months.
- Responsive design for a better user experience.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

```
age-calculator/
│
├── main.py
├── templates/
│   └── age_calculator.html
└── static/
    └── age_calculator_styles.css
```

### File Descriptions

- `main.py`: The main application file that contains the Flask server and the logic for calculating age.
- `templates/age_calculator.html`: The HTML template for the age calculator interface.
- `static/age_calculator_styles.css`: The CSS file for styling the application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DragonSenseiGuy/age-calculator.git
   cd age-calculator
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Requirements:

   ```bash
   pip3 install requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/age-calculator` to use the application.

## Usage

1. Enter your birth date in the provided input field.
2. Click the "Calculate" button.
3. Your age will be displayed in years and months.

## Error Handling
- If no birthdate is provided, the application will not return anything.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used for this project.
- [Google Fonts](https://fonts.google.com/) - For the custom font used in the application.