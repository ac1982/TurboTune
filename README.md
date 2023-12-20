# TurboTune

TurboTune is a Python utility designed to prepare datasets for fine-tuning OpenAI's GPT-3.5-turbo models. It processes conversation data from CSV files and converts them into JSONL format, adhering to the specific structure required for training these advanced language models.

## Features

- Processes CSV files to format conversation data for GPT-3.5-turbo.
- Removes duplicate entries based on user inputs.
- Validates the minimum data requirement (100 rows).
- Ensures the proper formatting of assistant responses.
- Outputs the data in JSONL format, ready for model fine-tuning.

## Prerequisites

- Python 3.x
- Pandas library

## Installation

1. Clone the repository:

```
git clone https://github.com/ac1982/TurboTune.git
```

2. Navigate to the TurboTune directory:
```
cd turbotune
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```


## Usage

Run `turbo_tune.py` with the path to your CSV file:

```
python turbo_tune.py -f path/to/your/file.csv
```


The script will generate a `file_prepared.jsonl` in the same directory, where `file.csv` is the name of your input file.

## Input File Format

The input CSV file should contain three columns:
- `system`: Descriptions or system messages.
- `user`: Simulated user queries or statements.
- `assistant`: Ideal responses from the assistant.

## Contributing

Contributions to TurboTune are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the [MIT License](LICENSE).

## Questions and Support

For questions and support, please open an issue in the [GitHub repository](https://github.com/ac1982/TurboTune/turbotune/issues).

