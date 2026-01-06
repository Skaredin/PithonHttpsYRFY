import sys
def decrypt(text: str) -> str:
    result = []
    i = 0

    while i < len(text):
        if text[i] == ".":
            # одиночная точка — просто пропускаем
            i += 1
        elif i + 1 < len(text) and text[i + 1] == ".":
            # две точки после символа → удалить предыдущий
            if result:
                result.pop()
            i += 2
        else:
            result.append(text[i])
            i += 1

    return "".join(result)
c
if __name__ == "__main__":
    input_text = sys.stdin.read().rstrip("\n")
    print(decrypt(input_text))
