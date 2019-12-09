1.subplots:
>so if you define a subplot as (2,3,1), that means to break the subplot into a 2 x 3 grid, and place the new subplot in the
 first cell of that grid.The last number indicates which of those cells to use here 1.
>ex. fig = plt.figure(figsize=(8,8)) # splitting our figure in 2 portions(1 row, 2 column)
     ax1 =fig.add_subplot(1, 2, 1)
     plt.show()
     
2.subplot2grid():
>plt.subplot2grid((3, 2), (0, 0), rowspan=2, colspan=1):  split out grid up into 3 rows by 2 columns, and set our starting index to the top
left cell. Finally, we need to tell our subplot to take up two of our three rows and 1 column .
