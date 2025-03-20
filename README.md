# GeminiProject
# Gemini - Vision - Pro Application
# Multimodal QA System using Gemini-Pro-Vision

## Overview
This project implements a **Multimodal Question-Answering (QA) System** using **Google's Gemini-Pro-Vision**. The system allows users to upload an image and input a text query related to the image. It then processes both inputs and generates a meaningful response using **Google Gemini AI**.

## Features
- **Image Upload Support**: Accepts PNG and JPG images.
- **Multimodal Processing**: Combines image and text inputs for accurate responses.
- **Google Gemini-Pro-Vision**: Utilizes state-of-the-art AI for processing.
- **Streamlit UI**: Simple and interactive user interface.
- **Reset Functionality**: Allows users to reset the session state.

## Technologies Used
- **Python**
- **Streamlit** (for the web application)
- **Google Gemini-Pro-Vision API**
- **PIL (Pillow)** (for image processing)
- **Dotenv** (for API key management)

## Prerequisites
- Python 3.x installed
- A **Google API Key** for Gemini-Pro-Vision
- Required Python dependencies installed:
  ```sh
  pip install streamlit google-generativeai pillow python-dotenv
  ```

## Setup Instructions
1. **Clone this repository:**
   ```sh
   git clone https://github.com/your-repo/multimodal-qa-system.git
   cd multimodal-qa-system
   ```
2. **Set up the API Key:**
   - Create a `.env` file in the project root and add your Google API Key:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
3. **Run the Streamlit App:**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Upload a PNG or JPG image.
2. Enter a relevant query in the text input box.
3. Click the **Submit** button to generate a response.
4. Click the **Reset** button to clear inputs and start fresh.

## Example Workflow
1. **Upload an Image:** A screenshot, document, or any relevant image.
2. **Enter a Query:** Example: "What text is written in this image?"
3. **Response:** The system will analyze the image and provide an appropriate answer.

## Future Enhancements
- Improve the model by integrating **OCR for text extraction**.
- Enhance UI with **better styling and animations**.
- Support for **multiple images** at once.

## License
This project is licensed under the **MIT License**. You are free to use and modify it.

## Contact
For any queries, reach out to **[Your Name]** at **[your-email@example.com]**.



![screencapture-localhost-8501-2024-07-16-23_10_21](https://github.com/user-attachments/assets/63b66ff7-d322-4293-b8c7-ca9b4d5a3da4)
