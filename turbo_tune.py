import pandas as pd
import json
import sys
import os

def process_csv_file(input_file):
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"文件 {input_file} 不存在。")
        return

    # Load the CSV file
    df = pd.read_csv(input_file)

    # 检查是否所有必要列都存在
    required_columns = ['system', 'user', 'assistant']
    if not all(column in df.columns for column in required_columns):
        print("CSV文件必须包含'system', 'user', 和 'assistant'这三列。")
        return

    # Identify duplicates in 'user'
    duplicates = df[df.duplicated(subset=['user'], keep=False)]
    if not duplicates.empty:
        print("First 10 duplicates based on 'user':")
        print(duplicates.head(10))

        # 显示删除的重复数据数量
        print(f"Removing {len(duplicates) - len(duplicates.drop_duplicates(subset=['user']))} duplicate rows.")

    # Remove duplicates in 'user'
    df = df.drop_duplicates(subset=['user'])

    # Check if data has at least 100 rows
    if len(df) < 100:
        print("The dataset should contain at least 100 rows.")
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

    print(f"JSONL file '{output_file}' has been created.")

def print_help():
    print("Assists in Preparing JSONL Files for Fine-Tuning GPT-3.5-turbo and Newer Models.")
    print("-f [filename.csv]: Specify the source CSV file.")
    print("-h: Display help.")

def main():
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == "-h":
        print_help()
        return

    if args[0] == "-f" and len(args) == 2:
        process_csv_file(args[1])
    else:
        print("Invalid arguments.")
        print_help()

if __name__ == "__main__":
    main()