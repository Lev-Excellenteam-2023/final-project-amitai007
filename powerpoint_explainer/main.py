import argparse
import logging
import json
from Helpers import parse_presentation, extract_text
from Helpers import generate_explanation
from utils import save_json, clean_text

logging.basicConfig(level=logging.INFO)


def process_presentation(pptx_path, output_path):
    """
    Process the PowerPoint presentation file and save explanations to the output file.

    Args:
        pptx_path (str): Path to the PowerPoint presentation (.pptx) file.
        output_path (str): Path to the output JSON file.

    Returns:
        None
    """
    slides = parse_presentation(pptx_path)
    explanations = []

    for slide_number, slide in enumerate(slides, start=1):  # Enumerate to track slide numbers
        text = extract_text(slide)
        if text:
            prompt = "\n".join(text)
            explanation = generate_explanation(clean_text(prompt), slide_number)  # Clean text before generating
            # Insert line breaks after each dot
            explanation_with_line_breaks = explanation.replace('.\n\n', '.')

            explanations.append(explanation_with_line_breaks)
        else:
            explanations.append(None)

    save_json(output_path, explanations)
    print(f"Explanations saved to {output_path}")


def main():
    """
    Main entry point of the application. Parses command-line arguments and processes the presentation.
    """
    # Create argument parser
    parser = argparse.ArgumentParser(description="PowerPoint Presentation Explainer")
    parser.add_argument("pptx_file", help="Path to the .pptx file")
    parser.add_argument("output_file", help="Path to the output JSON file")
    args = parser.parse_args()

    # Extract file paths from command-line arguments
    pptx_path = args.pptx_file
    output_path = args.output_file

    # Process the presentation and save explanations
    process_presentation(pptx_path, output_path)


if __name__ == "__main__":
    main()
