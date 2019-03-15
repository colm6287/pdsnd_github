import pdb
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
       
    # get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york', 'washington']
    while True:
      city = input('Would you like to filter the data for Chicago, New York or Washington? \n').lower()
      if city not in valid_cities:
        print('Selection error! Please choose a vaild city \n')
        continue
      else:
        break

    # get user input for month (all, january, february, ... , june)
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'none']
    while True:
      month = input('Would like to filter data by month? Type e.g. "May" for month, or "none" for no month filter \n').lower()
      if month not in valid_months:
        print('Selection error! Please enter a valid month or "none" for no month filter. \n')
        continue
      else:
        break
  
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'none']
    while True:
      day = input('Which day? Please type a day, e.g. "Monday", or type "none" for no day filter \n').lower()
      if day not in days:
        print('Selection error! Please enter a valid day or "none" for no day filter. \n')
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender or "No gender data to share" if no data ,Birth Year
        1423854,2017-06-23 15:09:32,2017-06-23 15:14:53,321,Wood St & Hubbard St,Damen Ave & Chicago Ave,Subscriber,Male,1992.0
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'none':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df): 
    """Displays statistics on the most frequent times of travel."""

    print('\nWhat is the breakdown of time stats?...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
   
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day:', common_day_of_week)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nWhat is the breakdown of station stats?...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_and_end_station = df['Start Station'].str.cat(df['End Station'],sep=", ").mode()[0]
    print ('Most Common Start and End Station:', common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nWhat is the breakdown of trip duration stats?...\n')
    start_time = time.time()


    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nWhat is the breakdown of user stats?...\n')
    start_time = time.time()
    

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    

    # Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else: 
        print('There is no gender data to return!')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth = df['Birth Year'].min()
        print('Earliest year of birth:', earliest_year_of_birth)
    else: 
        print('There is no earliest year of birth data to return!')
    

    if 'Birth Year' in df:
        most_recent_year_of_birth = df['Birth Year'].max()
        print('Most recent year of birth:', most_recent_year_of_birth)
    else: 
        print('There is no most recent year of birth data to return!')
    

    if 'Birth Year' in df:
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth:', common_year_of_birth)
    else: 
        print('There is no most common year of birth data to return!')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print('Would you like to see individual trip data?')
        trip_data = input()
        trip_data = trip_data.lower()

        i = 5
        while trip_data == 'yes':
            """ To display five rows of data for user view """
            print(df[:i])
            print('Would you like to see more individual trip data?')
            i *= 2
            trip_data = input()
            trip_data = trip_data.lower()



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()