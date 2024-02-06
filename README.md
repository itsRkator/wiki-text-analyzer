# Wikipedia API

The Wikipedia API allows users to perform text analysis tasks on Wikipedia articles. It provides two primary endpoints:

1. Word Frequency Analysis Endpoint
2. Search History Endpoint

## Table of Contents

1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)
3. [Endpoint Usage](#endpoint-usage)
   - [Word Frequency Analysis Endpoint](#word-frequency-analysis-endpoint)
   - [Search History Endpoint](#search-history-endpoint)
4. [Examples](#examples)
   - [Word Frequency Analysis Endpoint](#examples-word-frequency-analysis-endpoint)
   - [Search History Endpoint](#examples-search-history-endpoint)
5. [Testing](#testing)

## Introduction

The Wikipedia API allows users to analyze Wikipedia articles by providing insights into word frequency and search history.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/itsRkator/wiki-text-analyzer.git
   cd wikipedia_api
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**

   ```bash
   python app.py
   ```

6. **Access the API:**
   The API will be running at `http://127.0.0.1:5000/`. Use this base URL for making requests.

## Endpoint Usage

### Word Frequency Analysis Endpoint

- **URL:** `/word_frequency`
- **Method:** POST
- **Parameters:**
  - `topic` (string): Subject of the Wikipedia article.
  - `n` (integer): Number of top frequent words to return.

#### Request

```json
{
  "topic": "Python",
  "n": 5
}
```

#### Response

```json
{
  "topic": "Python",
  "top_words": [
    { "word": "python", "frequency": 10 },
    { "word": "language", "frequency": 5 }
    // ...
  ]
}
```

### Search History Endpoint

- **URL:** `/search_history`
- **Method:** GET

#### Response

```json
[
  {
    "topic": "Python",
    "top_words": [
      { "word": "python", "frequency": 10 },
      { "word": "language", "frequency": 5 }
      // ...
    ]
  }
  // ...
]
```

## Examples

### Examples: Word Frequency Analysis Endpoint

**Example 1: Successful Request**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"topic": "Python", "n": 5}' http://127.0.0.1:5000/word_frequency
```

**Example 2: Missing Parameter in Request**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"n": 5}' http://127.0.0.1:5000/word_frequency
```

### Examples: Search History Endpoint

**Example: Retrieve Search History**

```bash
curl http://127.0.0.1:5000/search_history
```

## Testing

To run unit tests, use the following command:

```bash
python test_app.py
