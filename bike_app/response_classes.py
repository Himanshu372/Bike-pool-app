
class FindRideResponse(object):
    def __init__(self, user_id, distance, depart_time, fare):
        self.user_id = user_id
        self.distance = distance
        self.depart_time = depart_time
        self.fare = fare