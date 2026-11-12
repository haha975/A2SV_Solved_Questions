class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ans=[0]*n
        for i in range(len(bookings)):
            ans[bookings[i][0] - 1] += bookings[i][2]
            if bookings[i][1]<n:
                ans[bookings[i][1]]-=bookings[i][2]
         
        for j in range(1,len(ans)):
            ans[j]+=ans[j-1]
        return ans

        

        