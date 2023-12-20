# TurboTune

TurboTune is a Python utility designed to prepare datasets for fine-tuning OpenAI's GPT-3.5 and newer models. It processes conversation data from CSV files and converts them into JSONL format, adhering to the specific structure required for training these advanced language models.

## Features

- Processes CSV files to format conversation data for GPT-3.5 and newer models.
- Removes duplicate entries based on user inputs.
- Validates the minimum data requirement (100 rows).
- Ensures the proper formatting of assistant responses.
- Outputs the data in JSONL format, ready for model fine-tuning.
- Includes a JSONL validation feature to ensure data integrity.

## Important Notes

- When preparing your CSV dataset, please refer to OpenAI's documentation for fine-tuning: [OpenAI Fine-Tuning Guide](https://platform.openai.com/docs/guides/fine-tuning).
- TurboTune is specifically developed for GPT-3.5 and newer models. It addresses the need for a tool that prepares data in the conversational format required for these models. The existing `openai tools fine_tunes.prepare_data` command primarily supports legacy fine-tuning with prompt and completion pairs, which may not be directly applicable for GPT-3.5 and above.

## Prerequisites

- Python 3.x
- Pandas library
- Colorama library (for enhanced output formatting)

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

To validate a JSONL file:
```
python turbo_tune.py -v path/to/your/file.jsonl
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
