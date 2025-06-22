import tokenize



def remove_comments_from_file(input_path, output_path):

    with open(input_path, 'r', encoding='utf-8') as f:

        code = f.read()



    result = []

    from io import StringIO

    g = tokenize.generate_tokens(StringIO(code).readline)

    prev_end = (1, 0)

    for toknum, tokval, start, end, line in g:

        if toknum == tokenize.COMMENT:

            continue              

        if toknum == tokenize.NL:

            result.append('\n')

        else:



            srow, scol = start

            prow, pcol = prev_end

            if srow == prow:

                result.append(' ' * (scol - pcol))

            else:

                result.append('\n' * (srow - prow))

                result.append(' ' * scol)

            result.append(tokval)

            prev_end = end



    with open(output_path, 'w', encoding='utf-8') as f:

        f.write(''.join(result))









if __name__ == "__main__":

    file_path = input("주석을 제거할 파이썬 파일의 절대경로를 입력하세요: ").strip().strip('"').strip("'")

    import os

    if not os.path.isfile(file_path):

        print("파일이 존재하지 않습니다.")

    else:

        base, ext = os.path.splitext(file_path)

        new_path = base + '_no_comment' + ext

        remove_comments_from_file(file_path, new_path)

        print(f"주석이 제거된 파일이 생성되었습니다: {new_path}")
