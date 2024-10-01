import gradio as gr
import requests
import json
import os
import base64
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "meta-llama/llama-3.2-90b-vision-instruct"

# Environment variables
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
YOUR_SITE_URL = os.environ.get("YOUR_SITE_URL", "https://your-site-url.com")
YOUR_APP_NAME = os.environ.get("YOUR_APP_NAME", "Image Captioning App")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set. Please set it using the 'setx' command.")

def make_api_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Make an API request to OpenRouter."""
    try:
        response = requests.post(
            url=API_ENDPOINT,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": YOUR_SITE_URL,
                "X-Title": YOUR_APP_NAME,
            },
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request: {str(e)}")
        raise

def caption_image(image: str, caption_length: str) -> str:
    """Generate a caption for the given image."""
    try:
        # Convert image to base64
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        image_url = f"data:image/jpeg;base64,{encoded_string}"

        system_message = "You are an advanced AI capable of analyzing images. "
        user_message = ""

        if caption_length == "Short":
            system_message += "Your task is to provide brief, concise descriptions of the images presented to you. Focus on the main elements and overall composition in a sentence or two."
            user_message = "Please describe this image briefly."
        else:  # Long caption
            system_message += "Your task is to provide detailed, accurate, and comprehensive descriptions of the images presented to you. Focus on the main elements, colors, actions, overall composition, and any notable or unusual aspects."
            user_message = "Please describe this image in detail."

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_message
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ]
        }

        result = make_api_request(payload)
        
        if 'choices' in result and len(result['choices']) > 0:
            caption = result['choices'][0]['message']['content']
            return caption
        else:
            logger.error(f"Unexpected response format: {json.dumps(result, indent=2)}")
            return "Error: Unexpected response format from the API."
    
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response: {str(e)}")
        return "Error: Unable to process the API response."
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return f"An unexpected error occurred: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=[
        gr.Image(type="filepath", label="Upload Image"),
        gr.Radio(["Short", "Long"], label="Caption Length", value="Long")
    ],
    outputs="text",
    title="Image Captioning",
    description="Upload an image and choose caption length to get a description."
)

# Launch the app
if __name__ == "__main__":
    iface.launch(share=True)
