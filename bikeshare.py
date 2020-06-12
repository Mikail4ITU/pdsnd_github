import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    #CITY_DATA = {'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv'}
    
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  
              

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_names = ['chicago', 'new york city', 'washington']
    city = input("\nWhat is the name of the city to analyze data? (E.g. Input either chicago, new york city, washington)\n").lower()
    while True:
        if city in city_names:
            #We were able to get the name of the city to analyze data.
            print("\nWe will be analyzing data from {} city.".format(city.upper()))
            break
        else:
            #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the city to analyze data, Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWhat is the name of the month to filter data? (E.g. Input either 'all' to apply no month filter or january, february, ... , june)\n")
        if month_name.lower() in MONTH_DATA:
            #We were able to get the name of the month to analyze data.
            month = month_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the month to filter data, Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... sunday)\n")
        if day_name.lower() in DAY_DATA:
            #We were able to get the name of the month to analyze data.
            day = day_name.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the day to filter data, Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n")

    print('-'*40)
    return city, month, day
        
           
             
       
            
        
        

       

def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



    



 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(common_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(most_common_start)
    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(most_common_end)
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination'].mode()[0]
    print(most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_trip_travel = df['Trip Duration'].sum()
    print(total_trip_travel)
    # TO DO: display mean travel time
    mean_trip_travel = df['Trip Duration'].mean()
    print(mean_trip_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
    
    except:UnboundLocalError
    print ("The earliest birth year is: {}".format(earliest_birth_year))
    print ("The most recent birth year is: {}".format(most_recent_birth_year))
    print ("The most common birth year is: {}".format(most_common_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No.").lower()
           
        elif answer == 'yes':
            raw_data += 5
        print(df.iloc[raw_data : raw_data + 5])
        again = input("Do you want to see more? Yes or No").lower()
        if again == 'no':
            break
        elif answer == 'no':
            return
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

