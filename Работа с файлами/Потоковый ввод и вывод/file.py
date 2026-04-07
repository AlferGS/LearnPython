import sys

data = []
for line in sys.stdin:
    data.append(int(line))
    
if all([(data[i]-data[i-1]) == data[1]-data[0] for i in range(1, len(data))]):
    print('Арифметическая прогрессия')
elif all([(data[i]/data[i-1]) == data[1]/data[0] for i in range(1, len(data))]):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')    
