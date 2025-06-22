import tokenize
from io import StringIO
import os

def remove_comments_from_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        code = f.read()

    result = []
    tokens = tokenize.generate_tokens(StringIO(code).readline)
    prev_end = (1, 0)

    for token_type, token_value, start, end, line in tokens:
        if token_type == tokenize.COMMENT:
            continue
        if token_type == tokenize.NL:
            result.append('\n')
        else:
            start_row, start_col = start
            prev_row, prev_col = prev_end
            if start_row == prev_row:
                result.append(' ' * (start_col - prev_col))
            else:
                result.append('\n' * (start_row - prev_row))
                result.append(' ' * start_col)
            result.append(token_value)
            prev_end = end

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

if __name__ == "__main__":
    file_path = input("Enter the absolute path of the Python file to remove comments from: ").strip().strip('"').strip("'")
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
    else:
        base_name, ext = os.path.splitext(file_path)
        new_path = base_name + '_no_comments' + ext
        remove_comments_from_file(file_path, new_path)
        print(f"A file with comments removed has been created: {new_path}")
