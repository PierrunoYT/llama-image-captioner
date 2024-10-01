# Llama Image Captioner

This Python application leverages the OpenRouter API and the Meta-Llama model to generate detailed captions for uploaded images.

## Features

- User-friendly Gradio interface for image uploads
- Detailed, accurate, and concise image descriptions
- Powered by the advanced Meta-Llama 3.2 90B Vision Instruct model
- Robust error handling and logging for improved debugging

## Prerequisites

Before getting started, make sure you have:

- Python 3.7 or higher installed
- An OpenRouter API key
- The following Python libraries: `gradio`, `requests`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/llama-image-captioner.git
   cd llama-image-captioner
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `requirements.txt` file with the following content:
   ```
   gradio
   requests
   ```

3. Set up your environment variables:
   - On Windows:
     ```
     setx OPENROUTER_API_KEY "your_api_key_here"
     setx YOUR_SITE_URL "https://your-actual-site-url.com"
     setx YOUR_APP_NAME "Llama Image Captioner"
     ```
   - On Unix-based systems:
     ```
     export OPENROUTER_API_KEY="your_api_key_here"
     export YOUR_SITE_URL="https://your-actual-site-url.com"
     export YOUR_APP_NAME="Llama Image Captioner"
     ```

   Note: After setting these environment variables, restart your command prompt or terminal for the changes to take effect.

## Usage

To run the application:

```
python ImageCaption.py
```

This will launch the Gradio interface. You can then upload an image, and the app will generate a detailed description of it.

## How It Works

1. The user uploads an image through the Gradio interface.
2. The image is converted to a base64-encoded string.
3. A request is sent to the OpenRouter API, which uses the Meta-Llama model.
4. The API returns a detailed description of the image.
5. The description is displayed to the user through the Gradio interface.

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 PierrunoYT

## Acknowledgments

- OpenRouter for providing the API
- Meta for the Llama model
- Gradio for the user-friendly interface building tools

## Project Link

[https://github.com/PierrunoYT/llama-image-captioner](https://github.com/PierrunoYT/llama-image-captioner)
