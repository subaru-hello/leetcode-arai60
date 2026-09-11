class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timelines = self.to_timeline(intervals)
        return self.count_max_rooms(timelines)

    def to_timeline(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for begin, end in intervals:
            events.append((begin, 1))
            events.append((end, -1))
        events.sort()
        return events

    def count_max_rooms(self, events: List[List[int]]) -> int:
        max_meeting_rooms_count = 0
        current_meeting_rooms_count = 0
        for _, delta in events:
            current_meeting_rooms_count += delta
            max_meeting_rooms_count = max(max_meeting_rooms_count, current_meeting_rooms_count)
        return max_meeting_rooms_count
