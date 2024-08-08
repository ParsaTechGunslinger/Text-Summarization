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

To use the summarization tool, follow these steps:

1. **Save the Code**:
   - Create a file named `summarizer.py` and paste the following code into it:

   ```python
   import nltk
   import string
   from heapq import nlargest

   # Ensure necessary NLTK data is downloaded
   # nltk.download('stopwords')
   # nltk.download('punkt')

   def summarize_text(text):
       # Determine the number of sentences for the summary
       sentence_count = text.count(". ")
       length = int(round(sentence_count / 10, 0)) if sentence_count > 20 else 1

       # Remove punctuation from the text
       nopuch = ''.join([char for char in text if char not in string.punctuation])

       # Tokenize the text into words and remove stopwords
       stopwords = set(nltk.corpus.stopwords.words('english'))
       words = [word for word in nopuch.split() if word.lower() not in stopwords]

       # Calculate word frequencies
       word_freq = {}
       for word in words:
           if word not in word_freq:
               word_freq[word] = 1
           else:
               word_freq[word] += 1

       max_freq = max(word_freq.values())
       for word in word_freq:
           word_freq[word] /= max_freq

       # Tokenize the text into sentences
       sent_list = nltk.sent_tokenize(text)

       # Score each sentence based on word frequencies
       sent_score = {}
       for sent in sent_list:
           for word in nltk.word_tokenize(sent.lower()):
               if word in word_freq:
                   if sent not in sent_score:
                       sent_score[sent] = word_freq[word]
                   else:
                       sent_score[sent] += word_freq[word]

       # Select the top sentences to form the summary
       summary_sents = nlargest(length, sent_score, key=sent_score.get)
       summary = ' '.join(summary_sents)

       return summary

   # Get input from the user
   user_text = input("Enter text to summarize: ")

   # Summarize the text
   summary = summarize_text(user_text)

   # Print the summary
   print("Summary:")
   print(summary)


```text
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.

Summary:
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.

