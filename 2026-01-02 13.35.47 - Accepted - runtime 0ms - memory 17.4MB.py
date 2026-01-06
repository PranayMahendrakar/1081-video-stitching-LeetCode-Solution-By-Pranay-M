class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Sort by start time, then by end time (descending)
        clips.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        current_end = 0
        i = 0
        n = len(clips)
        
        while current_end < time:
            # Find the clip that starts at or before current_end 
            # and extends the furthest
            max_end = current_end
            while i < n and clips[i][0] <= current_end:
                max_end = max(max_end, clips[i][1])
                i += 1
            
            if max_end == current_end:
                return -1  # Can't extend further
            
            count += 1
            current_end = max_end
        
        return count