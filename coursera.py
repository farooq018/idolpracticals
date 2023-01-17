# x="1"+"2"
# print(x)

# x=2//2
# print(x)

# Write your code below and press Shift+Enter to execute
# Genres=['rock','R&B','Soundtrack','R&B','soul','pop']
# for i in Genres:
#     print(i)

# i=0
# for i in range(-4,5):
#     print(i)
#


# squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
# new_squares = []
# i = 0
# while (i < len(squares) and squares[i] == 'orange'):
#     new_squares.append(squares[i])
#     i = i + 1
# print(new_squares)

# dates = [1982, 1980, 1973, 2000]
#
# i = 0
# year = dates[i]
#
# while (year != 1973):
#     print(year)
#     i = i + 1
#     year = dates[i]
# print("It took ", i, "repetitions to get out of loop.")

# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i = 0
# Rating = PlayListRatings[i]
# while(i < len(PlayListRatings) and Rating >= 6):
#     print(Rating)
#     i = i + 1 # This prints the value 10 only once
#     Rating = PlayListRatings[i]
#     i = i + 1
#
# def type_of_album(artist, album, year_released):
#     print(artist, album, year_released)
#     if year_released > 1980:
#         return "Modern"
#     else:
#         return "Oldie"
#
#
# x = type_of_album("Michael Jackson", "Thriller", 1980)
# print(x)


#Try and Except exersice
# a = 1
#
# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")
# else:
#     print("success a=",a)
# finally:
#     print("Processing Complete")

# create a dataframe to display the result below

# import pandas as pd
# x={"Student":["David","Samuel","Tery","Evan"],"Age":[27,24,22,32],"Country":["UK","Canada","China","USA"],"Course":["Python","Data Structures","Machine Learning","Web Development"],
#    "Marks":[85,72,89,76]}
# df=pd.DataFrame(x)
# print(df)
# # x=df.loc[0,'Country']
# # print(x)
# df1=df
# df1=df1.set_index("Country")
# x=df1.head()
# print(x)

# import pandas as pd
# x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
#       'Salary':[100000, 80000, 50000, 60000]}
#
# #casting the dictionary to a DataFrame
# df = pd.DataFrame(x)
#
# #display the result df
# print(df)
#
# # z=df.loc['Jane','Department']
# # print(z)
# # z=df.iloc[0:2,0:3]
# # print(z)
# # z=df.loc[0:2,'ID':'Department']
# # print(z)
# z=df.loc[2:3,"Name":"Department"]
# print(z)



# import pandas as pd
# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)
# print(df)
# # xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
#
# df = pd.read_excel(xlsx_path)
# print(df)

# Working with 1D arrays
# import numpy as np
# a=np.array([10,20,30])
# b=np.array([5,10,15])
# c=np.subtract(a,b)
# print(c)


import numpy as np
# a=np.array([10,20,30])
# b=np.array([2,10,5])
# c=np.divide(a,b)
# print(c)

# x=np.array([0,np.pi/2,np.pi])
# y=np.sin(x)
# print(y)

# Working with 2D arrays

import numpy as np
# a=[[11,12,13],[21,22,23],[31,32,33]]
# A=np.array(a)
# print(A)

# X=np.array([[1,0],[0,1]])
# Y=np.array([[2,1],[1,2]])
# Z=np.dot(X,Y)
# print(Z)

#import pandas as pd
# import numpy as np
# df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# print(df)
#
# # Let’s say we want to add 10 to each element in a dataframe:
#
# df = df.transform(func = lambda x : x + 10)
# print(df)
#
# # Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
#
# result = df.transform(func = ['sqrt'])
# print(result)

# import pandas as pd
# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
#
# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())
#
# await download(filename, "diabetes.csv")
# df =pd.read_csv("diabetes.csv")
# print(df)

# A=["1","2","3"]
# for a in A:
#     print(2*a)

# for i in range(1,5):
#     if (i!=2):
#         print(i)

class Rectangle(object):
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color


def drawRectangle(self):
    import matplotlib.pyplot as plt
    plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
    plt.axis('scaled')
    plt.show()

d1=drawRectangle(Rectangle)
d1