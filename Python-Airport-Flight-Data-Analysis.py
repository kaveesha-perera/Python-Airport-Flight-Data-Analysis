"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: UOW user name- w2182464 / IIT ID- 20250778 
 4. Date: 2025 - 11 - 24
****************************************************************************

"""
from graphics import *
import csv
import math

# global variable
data_list = []   # data_list An empty list to load and hold data from csv file
Rain_Hours = []  # Rain_Hours an empty list for load and hold rains hours from csv file
min_airports = [] # store airports with min flights count
Valid_city_code =["LHR","MAD","CDG","IST","AMS","LIS","FRA","FCO","MUC","BCN"] #All airport codes used in the survey from CW Taable 2
Airport_name = {"LHR":"London Heathrow", "MAD":"Madrid Adolfo Suárez-Barajas","CDG":"Charles De Gaulle International", "IST":"Istanbul Airport International",
                    "AMS":"Amsterdam Schiphol", "LIS":"Lisbon Portela", "FRA":"Frankfurt Main","FCO":"Rome Fiumicino", "MUC":"Munich International",
                    "BCN":"Barcelona International"} #airport codes' full names

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader) # skip header row
        for row in csvreader:
            data_list.append(row)


# Histogram
def draw_histogram(airline_code, airline_name, airport_name, year, hourly_counts):
    win = GraphWin("Histogram", 900, 600) # create a graphic window
    win.setBackground("beige")

    # create title
    title_text = f"Departures by hour for {airline_name} from {airport_name} {year}"
    title = Text(Point(450, 30), title_text)
    title.setSize(16)
    title.setStyle("bold")
    title.draw(win)

    # layout settings for bars
    left_margin = 150
    top_margin = 80
    bar_height = 30
    gap = 10

    # find largest bar for scaling
    max_count = max(hourly_counts)
    if max_count == 0:
        max_count = 1 # it avoid division by Zero

    # Draw each bar 
    for hour in range(12):
        y = top_margin + hour * (bar_height + gap)

        # Hours(Y-axis)
        hour_label = Text(Point(90, y + bar_height/2), f"{hour:02d}:00") # 2 digits with leading zeros 0 - "00", 5 - "05", 13 - "13" AND add ":00"
        hour_label.setSize(12)
        hour_label.draw(win) #draw the rectangle in graphic window

        # Scaled bar width comparing with max count
        bar_width = (hourly_counts[hour] / max_count) * 500
        # draw the rectangle bars
        bar = Rectangle(Point(left_margin, y),
                        Point(left_margin + bar_width, y + bar_height))
        bar.setFill("light pink")
        bar.setOutline("dark red")
        bar.draw(win)

        # Numeric label on bar
        count_text = Text(Point(left_margin + bar_width + 25, y + bar_height/2), str(hourly_counts[hour]))
        count_text.setSize(12)
        count_text.draw(win)
        
    try:
        win.getMouse()  #Wait until the user clicks inside the graphics window
    except GraphicsError:
        pass  # window's close button error handling
    win.close()

def generate_histogram(Year, Airport_Full_Name):
    Valid_airline_codes = {"BA":"British Airways", "AF":"Air France" , "AY":"Finnair" , "KL":"KLM" , "SK":"Scandinavian Airlines" , "TP":"TAP Air Portugal" ,
                      "TK":"Turkish Airlines" , "W6":"Wizz Air" , "U2":"easyJet" , "FR":"Ryanair" , "A3": "Aegean Airlines" , "SN":"Brussels Airlines" ,
                      "EK":"Emirates" , "QR":"Qatar Airways" , "IB":"Iberia" , "LH":"Lufthansa"} # Valid airline codes from Table 3 cw
    

    #airline code for validation
    while True:
        Airline_code = input("Enter a two-character Airline code to plot a histogram: ").upper()
        if Airline_code in Valid_airline_codes:
            break
        print("Unavailable Airline code please try again.")


    # hourly_counts for histogram(0 - 11)
    hourly_counts = [0] * 12    #0 = 00:00 [0,0,0,0,0,0,0,0,0,0,0,0]
    
    # count flight per hour from data list
    for row in data_list:
        airline = row[1][:2]                 # first 2 letters of flight number (Airline code)
        hour = int(row[3].split(":")[0])     # actual departure hour

        if airline == Airline_code and 0 <= hour < 12:
            hourly_counts[hour] += 1
        
    # Call the histogram
    airline_name = Valid_airline_codes[Airline_code]
    draw_histogram(Airline_code, airline_name, Airport_Full_Name, Year, hourly_counts)

def load_airport_info():
    #defines
    LHR_count = 0
    MAD_count = 0
    CDG_count = 0
    IST_count = 0
    AMS_count = 0
    LIS_count = 0
    FRA_count = 0
    FCO_count = 0
    MUC_count = 0
    BCN_count = 0

    Terminal_num2_count = 0
    Under_600miles_count = 0
    departure_flights_AF_count = 0
    flight_departing_below_15C_count = 0
    departure_flights_BA_count = 0
    delayed_departure_flight_AF_count = 0

    Airport_code = input("please enter a three-letter city code:").upper()

    #Validation for airport code
    while len(Airport_code) !=3 or Airport_code not in Valid_city_code: #this runs when Airport code is invalid 
        if len(Airport_code) !=3:
            print("Wrong code length - please enter a three-letter city code.")
        else:
            print("Unavailable city code - please enter a valid city code.")
            print(f"Valid City Codes are {Valid_city_code}")
        Airport_code = input("Please enter a three-letter valid city code: ").upper()
            
    print(f"Your City Code is: {Airport_code}")

    #Validation for year
    while True:
        try:
            Year = int(input("Please enter the year required in the format YYYY:"))
            if len(str(Year)) != 4:
                print("Wrong data type - please enter a four-digit year value")
                continue
            if 2000 <= Year <= 2025:
                break
            else:
                print("Out of range – please enter a value from 2000 to 2025.")
        except ValueError:
            print("Wrong data type – please enter a four-digit year value.")

    #create a file name
    selected_data_file = Airport_code + str(Year) + ".CSV"
    print(f"File name is: {selected_data_file}")

    Airport_Full_Name = Airport_name [Airport_code] # get full name of airport code

    print("******************************************************************************")
    print(f"{selected_data_file}  selected - Planes departing {Airport_Full_Name} {Year}" )
    print("******************************************************************************")

    load_csv(selected_data_file)     #calls the function "load_csv" sending the variable 'selected_data_file" as a parameter

    Total_flight = len(data_list)
    print(f"The total number of flights from this airport was {Total_flight}")

    # convert hours to minutes
    def Convert_To_Minutes(Time_Now):
        Hours , Minutes = Time_Now.split(':')
        return int(Hours)* 60 + int(Minutes)

    for row in data_list:
        if row[8] == '2': # row[8] is Departure Terminal
            Terminal_num2_count += 1
        if int(row[5]) < 600: # row[5] is Distance miles
            Under_600miles_count += 1
        if row[1][:2] == 'AF': # row[1] is Flight num
            departure_flights_AF_count +=1
        if int(row[10].split("°")[0]) < 15: # row[10] is Weather Conditions
            flight_departing_below_15C_count +=1
        if row[1][:2] == 'BA': 
            departure_flights_BA_count +=1
        if row[1][:2] == 'AF' and Convert_To_Minutes(row[2]) < Convert_To_Minutes(row[3]):
            delayed_departure_flight_AF_count +=1
        if 'rain' in row [10]:
            Hour = row[3].split(':')[0]
            if Hour not in Rain_Hours :
                Rain_Hours.append(Hour)
        # row[4] is Destination         
        if Valid_city_code[0] in row[4]:
            LHR_count +=1
        if Valid_city_code[1] in row[4]:
            MAD_count +=1
        if Valid_city_code[2] in row[4]:
            CDG_count +=1
        if Valid_city_code[3] in row[4]:                                 
            IST_count +=1
        if Valid_city_code[4] in row[4]:
            AMS_count +=1
        if Valid_city_code[5] in row[4]:
            LIS_count +=1
        if Valid_city_code[6] in row[4]:
            FRA_count +=1
        if Valid_city_code[7] in row[4]:
            FCO_count +=1
        if Valid_city_code[8] in row[4]:
            MUC_count +=1
        if Valid_city_code[9] in row[4]:
            BCN_count +=1
    # find least common destination
    Counts = {"London Heathrow":LHR_count, "Madrid Adolfo Suárez-Barajas":MAD_count,"Charles De Gaulle International":CDG_count, "Istanbul Airport International":IST_count,
            "Amsterdam Schiphol":AMS_count, "Lisbon Portela":LIS_count, "Frankfurt Main":FRA_count,"Rome Fiumicino":FCO_count, "Munich International":MUC_count,
            "Barcelona International":BCN_count}
    min_value = min(Counts.values())
    for airport,count in Counts.items(): # airport = key , count = value
        if count == min_value:
            min_airports.append(airport)


    Average_number_of_British_Airways_per_hour = round(departure_flights_BA_count / 12,2) 
    Percentage_of_total_departures_that_are_British_Airways_aircraft = round((departure_flights_BA_count / Total_flight)*100,2)
    percentage_of_Air_France_flights_with_a_delayed_departure = round((delayed_departure_flight_AF_count / departure_flights_AF_count)*100,2)
    total_number_of_hours_of_rain_in_the_twelve_hours = len(Rain_Hours)

        
    print(f"The total number of flights departing Terminal Two was {Terminal_num2_count}")
    print(f"The total number of departures on flights under 600 miles was {Under_600miles_count}")
    print(f"There were {departure_flights_AF_count} Air France flights from this airport" )
    print(f"There were {flight_departing_below_15C_count} flights departing in temperatures below 15°C degrees" )
    print(f"There was an average of {Average_number_of_British_Airways_per_hour} British Airways flights per hour from this airport")
    print(f"British Airways planes made up {Percentage_of_total_departures_that_are_British_Airways_aircraft}% of all departures")
    print(f"{percentage_of_Air_France_flights_with_a_delayed_departure}% of Air France departures were delayed")
    print(f"There were {total_number_of_hours_of_rain_in_the_twelve_hours} hours in which rain fell")
    print(f"The least common destinations are {min_airports}")

    # save prints in results.txt file
    with open("results.txt",'a') as file:
        file.write("******************************************************************************\n")
        file.write(f"{selected_data_file}  selected - Planes departing {Airport_Full_Name} {Year}\n")
        file.write("******************************************************************************\n")    
        file.write(f"The total number of flights from this airport was {Total_flight}\n")
        file.write(f"The total number of flights departing Terminal Two was {Terminal_num2_count}\n")
        file.write(f"The total number of departures on flights under 600 miles was {Under_600miles_count}\n")
        file.write(f"There were {departure_flights_AF_count} Air France flights from this airport\n")
        file.write(f"There were {flight_departing_below_15C_count} flights departing in temperatures below 15°C degrees\n")
        file.write(f"There was an average of {Average_number_of_British_Airways_per_hour} British Airways flights per hour from this airport\n")
        file.write(f"British Airways planes made up {Percentage_of_total_departures_that_are_British_Airways_aircraft}% of all departures\n")
        file.write(f"{percentage_of_Air_France_flights_with_a_delayed_departure}% of Air France departures were delayed\n")
        file.write(f"There were {total_number_of_hours_of_rain_in_the_twelve_hours} hours in which rain fell\n")
        file.write(f"The least common destinations are {min_airports}\n")
        file.write("\n\n")
    # generate histrogram
    generate_histogram(Year, Airport_Full_Name)
    return Year, Airport_Full_Name, selected_data_file

# main loop    
while True:
    # load airport info and process data
    Year, Airport_Full_Name, selected_data_file = load_airport_info()
    # ask user if they want to load a new file
    while True: 
        user_input = input("Do you want to select a new data file? Y/N: ").upper()
        if user_input in ['Y', 'N']:
            break # break and its go to next if loop
        print("Invalid input. Please enter Y or N.")

    if user_input == 'N':
        print("Thank you. End of run")
        break
    else:  # if user_input == 'Y'
        # Clear previous data before next file
        data_list.clear() 
        Rain_Hours.clear()
        min_airports.clear()









  






