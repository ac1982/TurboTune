import pandas as pd
import json
import sys
import os
from colorama import Fore, Style

def process_csv_file(input_file):
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"{Fore.RED}文件 {input_file} 不存在。{Style.RESET_ALL}")
        return

    # Load the CSV file
    df = pd.read_csv(input_file)

    # Check if all necessary columns exist
    required_columns = ['system', 'user', 'assistant']
    if not all(column in df.columns for column in required_columns):
        print(f"{Fore.YELLOW}CSV文件必须包含'system', 'user', 和 'assistant'这三列。{Style.RESET_ALL}")
        return

    # Identify duplicates in 'user'
    duplicates = df[df.duplicated(subset=['user'], keep=False)]
    if not duplicates.empty:
        print(f"{Fore.CYAN}First 10 duplicates based on 'user':{Style.RESET_ALL}")
        print(duplicates.head(10).to_string(index=False))  # Using to_string for better formatting

        # Display the number of duplicate rows to be removed
        print(f"{Fore.MAGENTA}Removing {len(duplicates) - len(duplicates.drop_duplicates(subset=['user']))} duplicate rows.{Style.RESET_ALL}")

    # Remove duplicates in 'user'
    df = df.drop_duplicates(subset=['user'])

    # Check if data has at least 100 rows
    if len(df) < 100:
        print(f"{Fore.RED}The dataset should contain at least 100 rows.{Style.RESET_ALL}")
        return

    # Ensure "assistant" ends with '\n'
    df['assistant'] = df['assistant'].apply(lambda x: x if x.endswith('\n') else x + '\n')

    # Convert to JSONL format
    def row_to_json(row):
        return {
            "messages": [
                {"role": "system", "content": row['system']},
                {"role": "user", "content": row['user']},
                {"role": "assistant", "content": row['assistant']}
            ]
        }

    # Apply the function to each row
    jsonl_data = df.apply(row_to_json, axis=1)

    # Output file name
    output_file = input_file.replace('.csv', '_prepared.jsonl')

    # Write to JSONL file
    with open(output_file, 'w') as file:
        for entry in jsonl_data:
            file.write(json.dumps(entry) + '\n')

    print(f"{Fore.GREEN}JSONL file '{output_file}' has been created.{Style.RESET_ALL}")

def validate_jsonl(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"{Fore.RED}Invalid JSON at line {line_number}: {e}{Style.RESET_ALL}")
                    return False
        return True
    except FileNotFoundError:
        print(f"{Fore.RED}File not found: {file_path}{Style.RESET_ALL}")
        return False

def print_help():
    print("Assists in Preparing JSONL Files for Fine-Tuning GPT-3.5-turbo and Newer Models.")
    print("-f [filename.csv]: Specify the source CSV file.")
    print("-v [filename.jsonl]: Validate the JSONL file.")
    print("-h: Display help.")

def main():
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == "-h":
        print_help()
        return

    if args[0] == "-f" and len(args) == 2:
        process_csv_file(args[1])
    elif args[0] == "-v" and len(args) == 2:
        if validate_jsonl(args[1]):
            print(f"{Fore.GREEN}The JSONL file is valid.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}The JSONL file is not valid.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Invalid arguments.{Style.RESET_ALL}")
        print_help()

if __name__ == "__main__":
    main()