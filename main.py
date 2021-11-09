# This is the main file for the MAS417 Project

from Weather import Weather
from STLGenerator import STLGenerator


def main():

    # Ask for a location
    location = input("Enter Location: ")

    # Initiate PictureProcessing as processor
    generator = STLGenerator()

    # Initiate weather and save the location in the weather class
    weather = Weather(location)

    # Check if the location exists
    for attempt in range(5):
        location_retrieved = weather.check_location()
        if location_retrieved:
            # The location has been retrieved!
            break
        else:
            print("Try Again!")
            weather.set_location()
    else:
        print('No more tries.\n Goodbye!')
        return

    print(weather.get_weather())
    weather_symbol = f'./weathericon/{weather.symbol}.png'
    generator.generate_stl(weather_symbol)


if __name__ == "__main__":
    main()

# End of file