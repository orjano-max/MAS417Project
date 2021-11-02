# This is the main file for the MAS417 Project

# import STLGenerator as generator
from Weather import Weather
from PictureProcessing import PictureProcessing



def main():

    # --------------------------------------------------------------------
    # This part is used to test the weather class. Currently commented out

    # Ask for a location
    location = input("Enter Location: ")

    # Initiate PictureProcessing as processor
    processor = PictureProcessing()

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


    processor.segment_image(weather_symbol)

    # ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
