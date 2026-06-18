# Brenton's JR Rail Pass Optimizer (WIP)
### Introduction
A script written in Python that automatically finds the most suitable JR pass for any trip given an itinerary.
### Program Flow
The script receives user input via file input. Then, it proceeds to launch https requests to Yahoo!Transit by translating the English station names to Japanese characters and sending it to Yahoo!Transit. BeautifulSoup then parses the content and extracts the fares for calculations. A maximum cost and minimum cost is calcualted for each itinerary (may not be 100% accurate as it is not viable for a person to buy a JR pass and use local trains for every trip, just for reference)
The script then iterates over all available JR passes and finds the most suitable one by maximizing the difference between the pass cost and the maximum cost. Multiple passes may be used to cover a trip (Not sure how to implement unfortunately)
### Libraries/Modules used
- Pandas
- BeautifulSoup
### Data
Data is taken from StationAPI at [Github repository of StationAPI](https://github.com/TrainLCD/StationAPI)
