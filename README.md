# Simple Text Summarization Tool

This project provides a simple tool for summarizing text using Python's Natural Language Toolkit (NLTK). The summarization is based on word frequency analysis, where the most significant sentences are selected to create a summary.

## Features

- **Word Frequency-Based Summarization**: 
  - The tool scores sentences based on the frequency of important words and selects the top sentences to generate a summary.
- **Dynamic Summary Length**:
  - The length of the summary is automatically adjusted based on the length of the input text.

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `nltk`
  - `string`
  - `heapq`

## Installation

1. **Install Python**:
   - Make sure Python 3.7 or higher is installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the Required Libraries**:
   - If you haven't already, you'll need to install NLTK. Open a terminal or command prompt and run:
     ```bash
     pip install nltk
     ```
   - The `string` and `heapq` modules are part of the Python standard library, so no additional installation is needed for them.

3. **Download Necessary NLTK Data**:
   - The summarization tool requires some datasets from NLTK. Run the following code in a Python environment:
     ```python
     import nltk
     nltk.download('stopwords')
     nltk.download('punkt')
     ```

## Usage

1. **Run the Summarization Script**:
   - Save the provided code in a file named, for example, `summarizer.py`.
   - Open your terminal, navigate to the directory containing `summarizer.py`, and run:
     ```bash
     python summarizer.py
     ```

2. **Input Text**:
   - The script will prompt you to enter the text you want to summarize. You can either type the text directly or paste it.

3. **View Summary**:
   - After entering the text, the script will process it and print out a summary.

## Example

Suppose you input the following text:

```text
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.

Summary:
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.

