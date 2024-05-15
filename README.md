# AskTube

## AI-Powered Q&A Web Application
This repository hosts the source code for an AI-powered question-answering (Q&A) web application. This application enables users to input a YouTube video URL along with a query, leveraging various AI techniques to transcribe the video's audio, process the query, and generate relevant answers.

### Technologies Used:

##### Programming Languages
1. **Python**: The primary language for development due to its versatility and extensive libraries for AI and web development.
Libraries and Frameworks
2. **Flask**: A lightweight and flexible web framework used to create the API endpoints for the application.
3. **PyTube**: A Python library that interacts with the YouTube API to download video content.
4. **OpenAI API**: Integrated for audio transcription and natural language processing tasks, enabling the application to understand and respond to user queries effectively.
5. **Tkinter**: Used for creating a simple graphical user interface (GUI) for interacting with the web application.
AI and Machine Learning
6. **OpenAI GPT-3**: Utilized for text generation and understanding, enabling the application to provide accurate and contextually relevant responses.
7. **FAISS** (Facebook AI Similarity Search): Implemented for efficient similarity search on transcribed text data, enhancing the application's ability to retrieve relevant answers.

### Code Structure:

The repository consists of several Python scripts, each serving a specific purpose within the application:
1. transcrib.py: Contains functions responsible for downloading a YouTube video's audio, transcribing it using the OpenAI API, and saving the transcription to a text file.
2. rag.py: Implements functions for saving transcriptions as FAISS vectors and retrieving answers using FAISS similarity search.
3. helper.py: Provides a high-level function to orchestrate the entire process, taking a YouTube video URL and a query as input and returning the generated answer.
4. app.py: Defines a Flask web application with an endpoint to receive URL and query parameters and return the generated answer.
5. gui.py: Implements a simple graphical user interface using Tkinter, allowing users to interact with the web application through a user-friendly interface.

### Configuration
Before running the application, ensure you have set up your OpenAI API key. Follow these steps:

1. Obtain an OpenAI API Key: If you haven't already, sign up for an account on the OpenAI platform and obtain your API key. You can do this by visiting the OpenAI website and following the instructions provided.
2. Create a secret.py File: Create a file named secret.py in the root directory of the project. This file will store your sensitive information, including the OpenAI API key.
3. Set the API Key in secret.py: Inside secret.py, assign your API key to a variable named openaiapi:
```
openaiapi = "your-api-key-here"
```
Import the API Key in Your Code: In your main Python scripts (such as transcrib.py, rag.py, etc.), import the API key from secret.py:
```
from secret import openaiapi
```
This ensures that your API key remains secure and separate from your main codebase.

### Usage:

Running the Web Application
To run the web application, follow these steps:

1. Install the required dependencies listed in requirements.txt.
2. Execute the following command in your terminal:

```
python app.py
```
This will start the Flask server, and the application will be accessible at http://127.0.0.1:5000/.

##### Using the GUI:
Alternatively, you can use the provided GUI by running:

```
python gui.py
```
This will open a simple graphical interface where you can input the YouTube URL and your query, and it will display the generated answer.

Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.
