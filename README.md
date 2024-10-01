# Image Captioning App

This is a Python application that uses the OpenRouter API and the Meta-Llama model to generate detailed captions for uploaded images.

## Features

- Upload images through a user-friendly Gradio interface
- Generate detailed, accurate, and concise descriptions of uploaded images
- Utilizes the advanced Meta-Llama 3.2 90B Vision Instruct model
- Error handling and logging for better debugging

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An OpenRouter API key
- The following Python libraries: gradio, requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/image-captioning-app.git
   cd image-captioning-app
   ```

2. Install the required packages:
   ```
   pip install gradio requests
   ```

3. Set up your environment variables:
   - On Windows:
     ```
     setx OPENROUTER_API_KEY "your_api_key_here"
     setx YOUR_SITE_URL "https://your-actual-site-url.com"
     setx YOUR_APP_NAME "Your Actual App Name"
     ```
   - On Unix-based systems:
     ```
     export OPENROUTER_API_KEY="your_api_key_here"
     export YOUR_SITE_URL="https://your-actual-site-url.com"
     export YOUR_APP_NAME="Your Actual App Name"
     ```

   Note: After setting these environment variables, you'll need to restart your command prompt or terminal for the changes to take effect.

## Usage

To run the application:

```
python ImageCaption.py
```

This will start the Gradio interface. You can then upload an image, and the app will generate a detailed description of the image.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenRouter for providing the API
- Meta for the Llama model
- Gradio for the easy-to-use interface building tools
