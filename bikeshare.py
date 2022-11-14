import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    while True:
        # user input
        city = input("would you like to see data for chicago, new york city, or washington ? \n ").lower()
        # check if user input not as the three cities
        if city not in ('chicago', 'new york city', 'washington'):
            print("invalid input , try again please  \n!")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        # user input
        month = input("which month - january , february , march , april , may ,  june or all ? \n ").lower()
        # check if user input not a month
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("invalid input , try again please  \n!")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        # user input
        day = input(
            " which day - monday , tuesday , wedensday , thursday , friday , saturday , sunday or all ? \n").lower()
        # check user input
        if day not in ('monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("invalid input , try again please \n !")
            continue
        else:
            break

    print('-' * 40)
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
    # read data for the city was selected
    df = pd.read_csv(CITY_DATA[city])
    # convert start time to date time using to_datetime function
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day in the start time and create new column
    df['month'] = df['Start Time'].dt.month
    # using dt. to specific the data will take from the column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter month
    if month != 'all':
        # get index for month
        all_months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = all_months.index(month) + 1
        # filter month to create new data frame
        df = df[df['month'] == month]

        # filter day
    if day != 'all':
        # filter day to create new data frame
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_commn_month = df['month'].mode()[0]
    print(' the most common month is: \n', most_commn_month)

    # TO DO: display the most common day of week
    most_commn_day = df['day_of_week'].mode()[0]
    print(' the most common day of week is: \n', most_commn_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_commn_hour = df['hour'].mode()[0]
    print(' the most common start hour is: \n', most_commn_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station \n', most_start)

    # TO DO: display most commonly used end station
    most_end = df['End Station'].value_counts().idxmax()
    print(' most commonly used end station \n ', most_end)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stat = df.groupby(['Start Station', 'End Station']).count()
    print('the most frequent combination of start station and end station trip: \n ', most_start, " and the end :",
          most_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])
    print(' total travel time \n', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(' mean travel time \n', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    # print count for all user types
    print('count of user types: \n ', user_types)
    # TO DO: Display counts of gender
    Gender = df['Gender'].value_counts()
    # print gender
    print(' count of gender: \n ', Gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # min which is the earlist birth year
    earlist_birth = df['Birth Year'].min()
    print("earliest year of birth : \n ", earlist_birth)
    # max for most recent birth year
    recent_birth = df['Birth Year'].max()
    print("most recent year of birth : \n ", recent_birth)
    # idxmax() to return index of the maximm value for each column
    most_birth = df['Birth Year'].value_counts().idxmax()
    print(" the most common year of birth : \n ", most_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_rows(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no (small letter) \n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you want to continue? ").lower()
        if view_display == 'yes':
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        display_rows(df)
        station_stats(df)
        display_rows(df)
        trip_duration_stats(df)
        display_rows(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
