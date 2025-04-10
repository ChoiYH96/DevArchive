def window_count(window,traffic):
    return 1 if window[0] <= traffic[0] < window[1] or window[0] <= traffic[1] < window[1] or traffic[0]<=window[0]<window[1]<=traffic[1] else 0

def convert_time(traffics):
    traffics = [x.split()[1:] for x in traffics]
    convert_times = []

    for i in traffics:
        hour, minute, second = i[0].split(":")
        time = int(hour) * 3600 + int(minute) * 60 + float(second)
        convert_times += [[round(time - (float(i[1][:-1]) - 0.001), 3), time]]
    return convert_times

def solution(lines):
    time_stamp = convert_time(lines)
    answer = 0

    for i in range(len(time_stamp)):
        start, end = 0,0
        window = [[time_stamp[i][0],time_stamp[i][0]+1],[time_stamp[i][1],time_stamp[i][1]+1]]
        for j in range(len(time_stamp)):
            start += window_count(window[0],time_stamp[j])
            end += window_count(window[1],time_stamp[j])
        answer = max(answer, start, end)
    return answer