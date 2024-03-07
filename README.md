# Simple Internet Browser

## Overview
This project is a simple internet browser application that allows users to query Wikipedia directly from a streamlined web interface. Built with Python, Streamlit, and leveraging the power of Langchain and OpenAI, this application offers an easy-to-use platform for accessing information quickly.

## Features
- **User-Friendly Interface**: Built with Streamlit for an interactive user experience.
- **Secure API Key Input**: Users can input their own OpenAI API key securely.
- **Wikipedia Searches**: Leverages Langchain to perform natural language searches on Wikipedia.

## Installation

Before you can run the application, make sure you have Python installed on your machine. This project was developed with Python 3.8+, but it should work with newer versions as well.

### Steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-internet-browser.git
   cd simple-internet-browser

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set-up your `.env` file
   -Create a `.env` file in the root directory of the project and add your openAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here

## Running the Application

To run the application, execute the following command in the terminal:
```bash
streamlit run main.py
```

Navigate to the URL provided by Streamlit in your browser to interact with the application.

## Usage
1. Once the application is running, you'll see a sidebar where you can input your query and OpenAI API key.
2. Enter your query in the "Ask Wikipedia" text area.
3. For security, the OpenAI API key field is masked. Enter your API key here.
4. Click the "Submit" button to perform the search. The results will be displayed on the main page.

## Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or create a pull request.


## License
This project is licensed under the MIT License - see the LICENSE file for details.


Just make sure to replace `https://github.com/yourusername/simple-internet-browser.git` with the actual URL to your GitHub repository. If you add a LICENSE file to your repository, GitHub will automatically link to it when you mention it in the README. This README.md provides a comprehensive overview of your project, instructions for setup and usage, as well as guidelines for contribution, making it easy for users to get started with your application.
