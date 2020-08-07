#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    flight = [None] * length
    
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
        
    destination = cache["NONE"]
    
    for trip in range(length):
        flight[trip] = destination
        destination = cache[destination]
        
    return flight