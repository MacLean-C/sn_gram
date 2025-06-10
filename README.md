# SNGramParser

A simple string parser that returns a list containing BoW-style n-grams. The particularity of these n-grams is that they contain syntactic neighbors of noun/verb heads in order to increase the pertinence of generated n-grams and reduce the size of the BoW. This parser is currently used to preprocess text corpora for topic modeling using BoW-based topic models.

## Installation

To use `SNGramParser`, you need to have `spaCy` installed. `spaCy` models can be installed via the command line. Follow the steps below to set up your environment.

### Step 1: Install spaCy

First, install `spaCy` using pip:

```sh
pip install spacy
```

### Step 2: Download a spaCy Model

Download the `en_core_web_sm` model (or any other model you prefer) using the following command:

```sh
python -m spacy download en_core_web_sm
```

### Step 3: Install SNGramParser

Clone this repository and install the package:

```sh
git clone https://github.com/MacLean-C/sn_gram.git
cd sn_gram
pip install .
```

## Usage

To use the `SNGramParser`, you need to load a `spaCy` model and pass a `spaCy` `Doc` object to the parser. Below is an example of how to use the `SNGramParser`.

### Example

```python
import spacy
from sn_gram.sn_gram import SNGramParser

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

#Initialize a doc object using a test string
test_string = "The quick brown fox jumped over the large lazy dog."

doc = nlp(test_string)

# Initialize the SNGramParser with the spaCy Doc object
sn_bow = SNGramParser(doc)

# Generate n-grams
sn_bow.extract_sn_grams()

#form list from iterable
print(list(sn_bow.sn_gram_bow()))

#access sn_bow list directly
print(sn_bow.sn_grams)
```

### Detailed Steps

1. **Load the spaCy Model**

    ```python
    import spacy
    nlp = spacy.load("en_core_web_sm")
    ```

2. **Process a Sentence with spaCy**

    ```python
    doc = nlp("The quick brown fox jumped over the large lazy dog.")
    ```

3. **Initialize the SNGramParser**

    ```python
    from sn_gram.sn_gram import SNGramParser
    parser = SNGramParser(doc)
    ```

4. **Generate N-Grams**

    ```python
    parser.extract_sn_grams()
    print(parser.sn_grams)
    ```

## Additional Notes

- **spaCy Models**: You can use different `spaCy` models depending on your language and the size of the model you need. For example, you can use `en_core_web_md` or `en_core_web_lg` for larger models.
- **Customization**: The `SNGramParser` can be customized to fit your specific needs. You can modify the `extract_sn_grams` method to change how n-grams are generated.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

