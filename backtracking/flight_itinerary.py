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

def get_itinerary(flights, current_itinerary):
    '''

    :param flights:             List of [origin, destination]
    :param current_itinerary:   [origin, destination]
    :return:
    '''
    # Base case: If we've used up all the flights, we're done
    if not flights:
        return current_itinerary

    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        # Make a copy of flights without the
        # current one to mark it as used.
        flights_minus_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(destination)
        # Make sure the flight is a valid connection.
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()
    return None

# driver
flights = []
flights.append(['SFO', 'HNL'])
flights.append(['HNL', 'AKL'])
flights.append(['YUL', 'ORD'])
flights.append(['ORD', 'SFO'])


print(get_itinerary(flights, flights[0]))
