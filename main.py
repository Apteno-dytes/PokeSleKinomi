import csv
import kinomi

def main():
    with open('kinomi.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            row[1] = int(row[1])
            row[3] = float(row[3])
            row[4] = int(row[4])
            row[5] = True if row[5] == "True" else False
            point = kinomi.get_energy_point(row[1], row[2], row[3], row[4], row[5])
            print(row[0]+":\t"+str(point))

if __name__ == "__main__":
    main()
