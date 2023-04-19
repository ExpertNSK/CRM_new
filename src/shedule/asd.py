lst = {
    '01/04/2023': {'start': '10:00', 'end': '20:00'},
    '02/04/2023': {'start': '11:00', 'end': '21:00'}
}
dates = ['01/04/2023', '02/04/2023']
start_times = ['10:00', '20:00']
end_times = ['11:00', '21:00']

shd = {}

for i in range(len(dates)):
    shd[dates[i]] = {'start': start_times[i], 'end': end_times[i]}

print(shd[0])