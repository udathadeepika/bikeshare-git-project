import time
import pandas as pd

CITY_DATA = {'new york city': 'new_york_city.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
        """Ask the user for a city, month and day to analyze."""
    """Ask the user to specify a city, month, and day to analyze.

    Returns:
        (str) city, (str) month, (str) day - all lower case
    """
    print('Hello! Let us explore some US bikeshare data!')
    city = input('Which city? ').lower()
    while city not in CITY_DATA:
        city = input('Please choose a valid city: ').lower()
    month = input('Which month (all, january ... june)? ').lower()
    while month != 'all' and month not in MONTHS:
        month = input('Please choose a valid month: ').lower()
    day = input('Which day (all, monday ... sunday)? ').lower()
    while day != 'all' and day not in DAYS:
        day = input('Please choose a valid day: ').lower()
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """Load data for the city and filter by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['month'] == MONTHS.index(month) + 1]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print('Calculating The Most Frequent Times of Travel...')
    start = time.time()
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most common start hour:', common_hour)
    print('This took %s seconds.' % (time.time() - start))
    print('-' * 40)


def station_stats(df):
    print('Calculating The Most Popular Stations and Trip...')
    start = time.time()
    print('Most common start station:', df['Start Station'].mode()[0])
    print('Most common end station:', df['End Station'].mode()[0])
    trip = df['Start Station'] + ' to ' + df['End Station']
    print('Most common trip:', trip.mode()[0])
    print('This took %s seconds.' % (time.time() - start))
    print('-' * 40)


def trip_duration_stats(df):
    print('Calculating Trip Duration...')
    start = time.time()
    print('Total travel time:', df['Trip Duration'].sum())
    print('Mean travel time:', df['Trip Duration'].mean())
    print('This took %s seconds.' % (time.time() - start))
    print('-' * 40)


def user_stats(df):
    print('Calculating User Stats...')
    start = time.time()
    print(df['User Type'].value_counts())
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    if 'Birth Year' in df.columns:
        print('Earliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year:', int(df['Birth Year'].max()))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))
    print('This took %s seconds.' % (time.time() - start))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
