# This is the main file for the MAS417 Project

# import STLGenerator as generator
from Weather import Weather
# import PictureProcessing
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():

    # --------------------------------------------------------------------
    # This part is used to test the weather class. Currently commented out

    # Ask for a location
    location = input("Enter Location: ")

    # Initiate weather and save the location in the weather class
    weather = Weather(location)

    # Check if the location exists
    for attempt in range(5):
        location_exists = weather.check_location()
        if location_exists:
            # The location exists!
            break
        else:
            print("This location does not exist.\n Try Again!")
            weather.set_location()
    else:
        print('No more tries.\n Goodbye!')
        return

    print(weather.get_weather())
    weather_symbol = f'weathericon\{weather.symbol}.png'

    weather_symbol = f'weathericon\{weather.symbol}.png'

    img = mpimg.imread(weather_symbol)
    imgplot = plt.imshow(img)
    plt.show()
    # ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
