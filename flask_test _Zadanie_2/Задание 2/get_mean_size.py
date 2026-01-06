import sys
def get_mean_size(lines) -> str:
    sizes = []
    for line in lines:
        columns = line.split()
        if len(columns) < 9:
            continue
        try:
            size = int(columns[4])  # размер файла в байтах
            sizes.append(size)
        except ValueError:
            continue
    if not sizes:
        return "0 B"
    mean_size = sum(sizes) / len(sizes)
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    unit_index = 0
    while mean_size >= 1024 and unit_index < len(units) - 1:
        mean_size /= 1024
        unit_index += 1
    return f"{mean_size:.2f} {units[unit_index]}"
if __name__ == "__main__":
    # пропускаем первую строку
    lines = sys.stdin.readlines()[1:]  
    result = get_mean_size(lines)
    print(result)
