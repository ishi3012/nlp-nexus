
### `docs/text-summarization.md`

```markdown
# Text Summarization

Text Summarization involves generating a concise and coherent summary of a given text.

## Getting Started

To perform text summarization:

1. **Install Dependencies**: Ensure you have all required packages.
2. **Prepare Text**: Provide the text you want to summarize.
3. **Run Summarization**: Use the available methods to generate a summary.

## Example

Here’s an example of summarizing text:

```python
from nlp_nexus import text_summarization

text = "Natural language processing (NLP) is a field of artificial intelligence that enables computers to understand, interpret, and generate human language."
summary = text_summarization.summarize(text)
print(summary)