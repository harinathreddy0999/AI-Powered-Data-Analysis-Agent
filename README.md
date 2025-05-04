# AI-Powered Natural Language Data Analysis Agent

A sophisticated AI-powered web application that enables non-technical users to analyze tabular data using natural language queries. This tool bridges the gap between data and insights without requiring SQL knowledge or programming skills.

## Features

- **Intuitive File Upload**: Support for CSV and Excel files with automatic schema inference
- **Natural Language Queries**: Ask questions about your data in plain English
- **Intelligent Data Analysis**: Advanced querying with aggregations, filtering, and sorting
- **Interactive Visualizations**: Automatically generated charts based on query results
- **Statistical Insights**: Quick access to descriptive statistics and data summaries

## Quick Start

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
4. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage Example

1. Upload your CSV or Excel file
2. Ask questions in natural language:
   - "What is the average revenue by product category?"
   - "Show me the top 5 customers by total purchases"
   - "Plot monthly sales for the last year as a line chart"

## Project Structure

```
/data          # Sample datasets for testing
/src
  /components  # Streamlit UI components
  /core        # Core business logic
    /db        # DuckDB integration
    /nlp       # NL→SQL conversion
    /viz       # Visualization generation
  /utils       # Helper functions
/tests         # Test cases
/configs       # Configuration files
```

## Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: DuckDB, Pandas
- **Natural Language Processing**: OpenAI API (GPT models)
- **Visualization**: Plotly

## License

MIT 