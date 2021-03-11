'''
Given an unordered list of flights taken by someone, each
represented as (origin, destination) pairs, and a starting
airport, compute the person's itinerary. If no such itinerary
exists, return null. All flights must be used in the itinerary.

For example, given the following list of flights:

HNL ➔ AKL
YUL ➔ ORD
ORD ➔ SFO
SFO ➔ HNL

and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL.

'''

def is_valid():
    '''
    Check if solution is invalid if:
    1) there are no flights leaving from our last destination
    2) there are still flights remaining that can be taken. Since
    all flights must be used, we are at a dead end.
    :return:
    '''
    pass

def get_itinerary(flights):
    '''

    :param flights:             List of [origin, destination]
    :param current_itinerary:   [origin, destination]
    :return:
    '''
    # Base case: If we've used up all the flights, we're done
    if not flights or len(flights) == 0:
        return

    # Load up two dictionaries: one in each direction
    dir_flights = {}
    rev_flights = {}
    for flight in flights:
        dir_flights[flight[0]] = flight[1]
        rev_flights[flight[1]] = flight[0]

    # Find the starting point where a city
    # is a starting point but not destination.
    starting_point = ''
    for origin in dir_flights.keys():
        if origin not in rev_flights.keys():
            starting_point = origin
            break

    # Walk the flights from origin to destination.
    to = dir_flights[starting_point]
    while to is not None:
        print(f"{starting_point} -> {to}")
        if to not in dir_flights:
            break
        starting_point = to
        to = dir_flights[to]



# driver
flights = []
flights.append(['HNL', 'AKL'])
flights.append(['YUL', 'ORD'])
flights.append(['ORD', 'SFO'])
flights.append(['SFO', 'HNL'])

get_itinerary(flights)
