import os
import time

from Powerpoint_explainer.Helpers import parse_presentation, extract_text, generate_explanation
from Powerpoint_explainer.utils import save_json

UPLOAD_FOLDER = '../uploads'
OUTPUT_FOLDER = '../outputs'
SLEEP_INTERVAL = 10  # seconds


def process_uploaded_files():
    while True:
        uploaded_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.pptx')]

        for filename in uploaded_files:
            pptx_path = os.path.join(UPLOAD_FOLDER, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.json"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            slides = parse_presentation(pptx_path)
            explanations = []

            for slide_number, slide in enumerate(slides, start=1):  # Enumerate slides with their numbers
                text = extract_text(slide)
                if text:
                    prompt = "\n".join(text)
                    explanation = generate_explanation(prompt, slide_number)  # Provide slide_number
                    explanations.append(explanation)
                else:
                    explanations.append(None)

            save_json(output_path, explanations)
            print(f"Explanations saved to {output_path}")

            # Remove the processed PowerPoint file from the UPLOAD_FOLDER
            os.remove(pptx_path)

        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    process_uploaded_files()
