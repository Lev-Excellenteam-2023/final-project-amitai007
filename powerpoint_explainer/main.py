import argparse
import json
from helpers.pptx_helper import parse_presentation, extract_text
from helpers.gpt_helper import generate_explanation
from utils import save_json


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
