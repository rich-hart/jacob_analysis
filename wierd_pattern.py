import matplotlib.pyplot as plt

DATA_FILE_PATH = './Bimodal_Data.csv'


with open(DATA_FILE_PATH) as file:
    data = []
    for line in file:
        entries = line.split(',')
        first_entry = entries[0]
        try:
            value = float(first_entry)
        except ValueError:
            value = None
        if value is not None:
            data.append(value)


data.sort()
data_copy = data[:]

diff = []
value_a = data.pop(0)

while data:
    value_b = data.pop(0)
    diff.append(abs((float(value_b)-float(value_a))))
    value_a=value_b

plt.ylim(0,.2)    
plt.plot(diff,'bo')

plt.show()

