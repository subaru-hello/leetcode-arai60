class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)
        last_meeting_ended_at = -1
        for begin, end in sorted_intervals:
            if begin < last_meeting_ended_at:
                return False
            last_meeting_ended_at = end
        return True
