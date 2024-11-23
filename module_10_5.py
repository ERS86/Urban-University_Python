import datetime
import multiprocessing


def read_info(name):
    all_data = []
    for i in name:
        file = i.strip('./')
        file_open = open(file, 'r')
        file_open.read()
        new_line = file_open.readline()
        all_data.append(new_line)
        file_open.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time1 = datetime.datetime.now()
read_info(filenames)
time2 = datetime.datetime.now()
line_time = time2 - time1
print(f'{line_time} (линейный)')

if __name__ == '__main__':
    time3 = datetime.datetime.now()
    multiprocessing.Process(target=read_info, args=(filenames,)).start()
    time4 = datetime.datetime.now()
    multipr_time = time4 - time3
    print(f'{multipr_time} (многопроцессорный)')
