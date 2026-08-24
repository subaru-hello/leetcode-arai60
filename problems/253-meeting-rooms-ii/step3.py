class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timelines = self.to_timelines(intervals)
        return self.count_max_rooms(timelines)

    def to_timelines(self, intervals: List[List[int]]) -> List[List[int]]:
        timelines = []
        for begin, end in intervals:
            timelines.append((begin, 1))
            timelines.append((end, -1))
        timelines.sort()
        return timelines

    def count_max_rooms(self, timelines: List[List[int]]) -> int:
        current_max_rooms = 0
        max_rooms_so_far = 0
        for time, delta in timelines:
            current_max_rooms += delta
            max_rooms_so_far = max(max_rooms_so_far, current_max_rooms)
        return max_rooms_so_far
