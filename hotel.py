# class HOTEL
class Hotel:
    sortparam='name'
    def __init__(self) -> None:
        self.name=''
        self.roomAvl=0
        self.location=''
        self.rating=int
        self.pricePr=0

    def __lt__(self,other):
        getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)

#Function to change sort parameter to name.
    @classmethod
    def sortByName(cls):
        cls.sortParam='name'
    # Function to change sort parameter to  rating.
    @classmethod
    def sortByRate(cls):
        cls.sortParam='rating'
#Function to change sort parameter to room availability.
    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam='roomAvl'

    def __repr__(self) -> str:
        return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tRating:{}\tPricePer Room:{}".format(self.name,self.roomAvl,self.location,self.rating,self.pricePr) 
 #Create class for user data.
class User:
    def __init__(self) -> None:
        self.uname=''
        self.uId=0
        self.cost=0
    def __repr__(self) -> str:
        return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname,self.uId,self.cost) 
       
#print hotels data.
def PrintHotelData(hotels):
    for h in hotels:
        print(h)
#Sort Hotels data by name.
def SortHotelByName(hotels):
    print("SORT BY NAME:")

    Hotel.sortByName()
    hotels.sort()

    PrintHotelData(hotels)
    print()

# Sort Hotels by rating
def SortHotelByRating(hotels):
    print("SORT BY A RATING:")

    Hotel.sortByRate()
    hotels.sort()

    PrintHotelData(hotels) 
    print()

# print Hotels for any city Location.
def printHotelBycity(s,hotels):
    print("HOTELS FOR {} LOCATION ARE:".format(s))
    hotelsByLoc=[h for h in hotels if h.location==s]

    PrintHotelData(hotelsByLoc)
    print()

# Sort hotels by room Available.
def sortByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE:")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()

#Print the user's data
def PrintUserData(userName, userId,bookingcost,hotels):
    users=[]
    #ACCESS user data
    for i in range(3) :
        u=User()
        u.uname= userName[i]
        u.uId= userId[i]
        u.cost= bookingcost[i]
        users.append(u)
    for i in range(len(users)) :
        print(users[i],"\tHote name:",hotels[i].name)
#function to slove #Hotel management problem
def HotelManagement(userName,userId,hotelName,bookingcost,rooms,locations,ratings,prices):
    hotels=[]  
    for i in range(3):
        h = Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)
    print()
    # call the various operations
    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    printHotelBycity("Bangalore",hotels)
    sortByRoomAvailable(hotels)
    PrintUserData(userName,userId,bookingcost,hotels)

# Driver code.
if __name__=='__main__':
    #Initialize variable to stores
    #hotels data and user data.
    userName = ["U1","U2","U3"]
    userId = [2, 3, 4]
    hotelName = ["H1","H2","H3"]
    bookingcost = [1200,1000,1100]  
    rooms = [4, 5, 7]
    locations = ["Bangalore", "Mumbai", "Noida"]
    ratings = [3, 4, 5]
    prices = [100, 200, 300]

    #function to perform operations
    HotelManagement(userName,userId,hotelName,bookingcost,rooms,locations,ratings,prices)
