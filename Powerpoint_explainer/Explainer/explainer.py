import os
import time
from Powerpoint_explainer.Helpers.pptx_helper import parse_presentation, extract_text
from Powerpoint_explainer.Helpers.gpt_helper import generate_explanation
from Powerpoint_explainer.utils import save_json

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
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

            for slide in slides:
                text = extract_text(slide)
                if text:
                    prompt = "\n".join(text)
                    explanation = generate_explanation(prompt)
                    explanations.append(explanation)
                else:
                    explanations.append(None)

            save_json(output_path, explanations)
            print(f"Explanations saved to {output_path}")
            os.remove(pptx_path)  # Remove processed file

        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    process_uploaded_files()
