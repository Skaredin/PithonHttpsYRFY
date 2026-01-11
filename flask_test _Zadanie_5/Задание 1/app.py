import subprocess
import os
import signal
import time
def get_pid_by_port(port: int) -> int | None:
    """
    Возвращает PID процесса, занимающего порт
    (Linux, через lsof)
    """
    result = subprocess.run(
        ["lsof", "-i", f":{port}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    lines = result.stdout.splitlines()
    if len(lines) < 2:
        return None
    return int(lines[1].split()[1])
def run_server(port: int):
    """
    Запускает сервер.
    Если порт занят — освобождает его и запускает снова.
    """
    while True:
        try:
            print(f"Запуск сервера на порту {port}")
            subprocess.run(
                ["python3", "-m", "http.server", str(port)],
                check=True
            )
            break
        except subprocess.CalledProcessError:
            print(f"Порт {port} занят")
            pid = get_pid_by_port(port)
            if pid is None:
                print("Не удалось найти процесс")
                return
            print(f"Завершаем процесс PID={pid}")
            os.kill(pid, signal.SIGTERM)
            time.sleep(1)
            print("Повторная попытка...\n")

if __name__ == "__main__":
    run_server(5000)
