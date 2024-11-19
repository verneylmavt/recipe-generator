# Recipe Generator 🍳

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Table of Contents

- [About The Project](#about-the-project)
  - [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project

Transform your available ingredients into delicious and creative recipes with the **Recipe Generator**! Whether you're a seasoned chef or a beginner in the kitchen, this Flask-based web application helps you discover new dishes based on what you have on hand.

![Recipe Generator Screenshot](static/assets/images/screenshot.png)

### Features

- **Ingredient Input**: Manually enter a list of ingredients to generate matching recipes.
- **Image Upload**: Upload a photo of your ingredients, and the app recognizes them to suggest recipes.
- **Nutritional Information**: Get detailed nutritional breakdowns for each recipe.
- **Responsive Design**: Enjoy a seamless experience across desktops, tablets, and mobile devices.
- **Interactive UI**: Modern and clean interface with smooth animations and transitions.

## Demo

*Coming Soon!* (If you have a live demo deployed, include the link here.)

## Technologies Used

- **Frontend**:
  - [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - [Bootstrap 5](https://getbootstrap.com/)
  - [JavaScript & jQuery](https://jquery.com/)
  - [Font Awesome](https://fontawesome.com/)
  
- **Backend**:
  - [Python 3.8+](https://www.python.org/)
  - [Flask](https://flask.palletsprojects.com/)
  - [Pandas](https://pandas.pydata.org/)
  - [TensorFlow](https://www.tensorflow.org/)
  - [NLTK](https://www.nltk.org/)
  - [SpaCy](https://spacy.io/)
  - [Requests](https://docs.python-requests.org/)
  
- **APIs**:
  - [Nutritionix API](https://www.nutritionix.com/business/api) (for nutritional information)
  
- **Version Control**:
  - [Git](https://git-scm.com/)
  - [GitHub](https://github.com/)

## Installation

### Prerequisites

Before setting up the project, ensure you have the following installed on your machine:

- **Python 3.8+**
- **Git**
- **Virtual Environment Tool** (optional but recommended)

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/verneylmavt/recipe-generator.git
    cd recipe-generator
    ```

2. **Create a Virtual Environment**

    It's good practice to use a virtual environment to manage project dependencies.

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On Unix or MacOS:**

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**

    The application requires certain environment variables, especially for API keys. Create a `.env` file in the root directory and add the following:

    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    NUTRITIONIX_APP_ID=your_nutritionix_app_id
    NUTRITIONIX_APP_KEY=your_nutritionix_app_key
    SECRET_KEY=your_flask_secret_key
    ```

    - Replace `your_nutritionix_app_id` and `your_nutritionix_app_key` with your actual Nutritionix API credentials.
    - Replace `your_flask_secret_key` with a secure secret key for Flask sessions.

6. **Download NLP Models**

    The application uses NLTK and SpaCy for natural language processing. Download the required models:

    ```python
    python
    ```

    In the Python shell:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    import spacy
    spacy.cli.download("en_core_web_sm")
    exit()
    ```

7. **Run the Application**

    ```bash
    flask run
    ```

    The application should now be accessible at `http://127.0.0.1:5000/`.

## Usage

1. **Home Page**

    - **Enter Ingredients**: Type in the ingredients you have, separated by commas.
    - **Or Upload Image**: Alternatively, upload an image containing your ingredients.

2. **Generate Recipe**

    - Click on the "Generate Recipe" button.
    - The app will process your input and display a recipe that matches your ingredients, including ingredients list, instructions, and nutritional information.

3. **Navigate**

    - Use the "Back" button on the recipe page to generate another recipe.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork the Project**

    Click the "Fork" button at the top right of the repository page.

2. **Create Your Feature Branch**

    ```bash
    git checkout -b feature/AmazingFeature
    ```

3. **Commit Your Changes**

    ```bash
    git commit -m "Add some AmazingFeature"
    ```

4. **Push to the Branch**

    ```bash
    git push origin feature/AmazingFeature
    ```

5. **Open a Pull Request**

    Go to your forked repository on GitHub and click the "New Pull Request" button.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Verney Mavt - [verney.mavt@example.com](mailto:verney.mavt@example.com)

Project Link: [https://github.com/verneylmavt/recipe-generator.git](https://github.com/verneylmavt/recipe-generator.git)

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Nutritionix API](https://www.nutritionix.com/business/api)
- [Font Awesome](https://fontawesome.com/)
- [Unsplash](https://unsplash.com/) for free images (if used)
- [Stack Overflow](https://stackoverflow.com/) for community support

