def average(arr):
    return sum(arr)/len(arr)

def qtd_above_average(arr):
    avg = average(arr)
    return sum(x>avg for x in arr)

if __name__ == "__main__":
    day_temps = []
    qtd = int(input("\nHow many day´s: "))
    i = 0
    for i in range(qtd): 
        day_temps.append(float(input(f"Day {i+1}´s hight temp: ")))

    print(f"\nAverage = {average(day_temps)}")
    print(f"\nDays above average: {qtd_above_average(day_temps)}")