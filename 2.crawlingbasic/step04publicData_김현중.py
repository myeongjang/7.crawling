import csv

def read_csv(filename):
    with open(filename+".csv", encoding="CP949") as f:
        return [row for row in csv.reader(f) if row]

if __name__ == "__main__":
    data = read_csv("(2017.05)")

    #missions
    for mission in range(3):
        sum = 0
        for item in data:
            try: sum += int(item[mission+1].strip().replace(",", ""))
            except ValueError: pass
        print("Mission {} value: {}".format(mission+1, sum))