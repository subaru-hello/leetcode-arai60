class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for begin, end in intervals:
            events.append((begin, 1))
            events.append((end, -1))

        sorted_events = sorted(events)
        current_meeting_rooms = 0
        max_meeting_rooms = 0
        for time, delta in sorted_events:
            current_meeting_rooms += delta
            max_meeting_rooms = max(max_meeting_rooms, current_meeting_rooms)

        return max_meeting_rooms
