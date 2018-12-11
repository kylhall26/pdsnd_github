import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("Hello! Let's explore some US bikeshare data!")
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to analyze Chicago, New York City or Washington?  ").lower()
    while city == 'chicago' or 'new york city' or 'washington':
        print("You have selected: ", city)
        break
    else:
        print("Invalid input. Start Over!")

        # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month do you want to analyze?  ').lower()
    while month == 'january' or 'february' or 'march' or 'april' or 'may' or 'june' or 'july' or 'august' or 'september' or 'october' or 'november' or 'december' or 'all':
        print("You would like to analyze: ", month)
        break
    else:
        print("Invalid input. Try again.")

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day of the week are you interested in?  ').lower()
    while day == 'sunday' or 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday' or 'saturday'or 'all':
        print("You are interested in: ", day)
        break
    else:
        print("Invalid input. Try again.")

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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
          df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    print("\nThe most popular month is: ", pop_month)

        # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day is: ", pop_day)

        # TO DO: display the most common start hour
    pop_start_time = df['hour'].mode()[0]
    print("\nThe most popular start time is: ", pop_start_time)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station is: ', pop_start_station)

        # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is: ', pop_end_station)

        # TO DO: display most frequent combination of start station and end station trip
    df['Start and End St'] = df['Start Station'].map(str) + df['End Station']
    pop_start_end = df['Start and End St'].mode()[0]
    print('\nThe most popular combination of stations is', pop_start_end)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print("\nTotal travel time in seconds for this time period is ", total_trip)

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print("\nThe mean travel time for this time period is ", int(mean_trip))

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    if 'User Type' in df.columns:
        print("\nUser types are: ", user_types)
    else:
        print("\nUser types are not present")

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    if 'Gender' in df.columns:
        print("\nThe breakdown of gender is: ", gender)
    else:
        print("\nGender is not in this dataset")

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest_birth=np.nanmin(df['Birth Year'])[0]
    print('\nOldest birth year is', int(oldest_birth))

    youngest_birth=np.nanmax(df['Birth Year'])[0]
    print('\nYoungest birth year is', int(youngest_birth))

    common_birth=df['Birth Year'].mode()[0]
    print('\nMost common birth year is', int(common_birth))

display = input('\nWould you like to view the raw data 5 rows at a time? ').lower()
    if display !='yes':
        break
    else:
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)


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

main()
