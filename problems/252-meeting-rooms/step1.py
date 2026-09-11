class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)
        last_meeting_end = -1
        for start, end in sorted_intervals:
            if start < last_meeting_end:
                return False
            last_meeting_end = end
        return True
