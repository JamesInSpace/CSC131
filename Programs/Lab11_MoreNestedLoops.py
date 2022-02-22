# Name: James R. Laurita
# Date: 2.22.2022
# Lab10: More Nested Loops
# Description: Create a table of numbers for wind chill.

def main():

    print(format('Wind chill Factors("Feels Like")', "^97s"))
    print(format('Temperature', "^97s"))

    print("Wind", end=" |")
    for x in range(40, -50, -5):
        print(format(x, "5d"), end = "")
    print()
    print("-" * 97)

    for y in range(5, 65, 5):
        print(format(y, "4d"), end = " |")
        for x in range(40, -50, -5):
            windChill = float(35.74 + 0.6215 * x - 35.75 * y**0.16 + 0.4275 * x * y**0.16)
            print(format(windChill, "5.0f"), end = "")
        print()




if __name__ == "__main__":
    main()

    # print( ddd, end = "")