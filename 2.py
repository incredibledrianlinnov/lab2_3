import time


def main():
    work_buffer = ""
    MAX_WORK_BUFFER_LEN = 1024 * 1024  # 1Gb
    CHUNK_SIZE = 1024
    alphabet = {'0': 'ноль', '2': 'два', '4': 'четыре', '6': 'шесть', '8': 'восемь'}
    ends = {'!', '?', '.'}
    digit_count = 0
    point_count = 0
    is_end = False
    try:
        with open("text.txt", "r", encoding="utf-8") as file:
            while True:
                read_buffer = file.read(CHUNK_SIZE)
                i = 0
                if not read_buffer:
                    if digit_count != 0:
                        print(work_buffer)
                    break

                while i < len(read_buffer):
                    if read_buffer[i].isdigit():
                        digit_count += 1
                        if digit_count % 2 == 0 and read_buffer[i] in alphabet:
                            work_buffer += alphabet[read_buffer[i]]
                        else:
                            work_buffer += read_buffer[i]
                    elif work_buffer or not read_buffer[i].isspace():
                        work_buffer += read_buffer[i]

                    if len(work_buffer) > MAX_WORK_BUFFER_LEN:
                        print("Достигнут лимит рабочего буффера")
                        exit()

                    if is_end:
                        if point_count == 0:
                            if read_buffer[i] == "!":
                                print(work_buffer)
                                digit_count = 0
                                is_end = False
                                work_buffer = ""
                            else:
                                print(work_buffer[:-1])
                                digit_count = 0
                                is_end = False
                                if work_buffer[-1].isspace() or work_buffer[-1] in ends:
                                    work_buffer = ""
                                else:
                                    work_buffer = work_buffer[-1]
                                    if work_buffer.isdigit():
                                        digit_count += 1
                        else:
                            if read_buffer[i] == ".":
                                point_count += 1
                            else:
                                print(work_buffer[:-point_count])
                                digit_count = 0
                                is_end = False
                                point_count = 0
                                if work_buffer[-1].isspace() or work_buffer[-1] in ends:
                                    work_buffer = ""
                                else:
                                    work_buffer = work_buffer[-1]
                                    if work_buffer.isdigit():
                                        digit_count += 1
                            if point_count == 3:
                                print(work_buffer)
                                digit_count = 0
                                is_end = False
                                work_buffer = ""
                                point_count = 0
                    elif read_buffer[i] in ends:
                        is_end = True
                        if read_buffer[i] == "!":
                            if digit_count != 0:
                                print(work_buffer)
                            digit_count = 0

                        if read_buffer[i] == ".":
                            point_count = 1

                        if digit_count == 0:
                            work_buffer = ""
                            is_end = False
                            point_count = 0




                    i += 1
    except FileNotFoundError:
        print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nProgram time: " + str(time.time() - start) + " seconds.")