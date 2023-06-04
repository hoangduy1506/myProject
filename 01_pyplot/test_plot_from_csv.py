import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
df_origin = pd.read_csv("storeData2D.csv")
df = df_origin.copy()

df_dropped = df.drop_duplicates(subset = ["yaw", "pitch", "robot_x", "robot_y", "robot_z"], keep = 'last')
open('storeData2D_final.csv', 'w', encoding='UTF8', newline='')
df_dropped.to_csv('storeData2D_final.csv')
ax.plot(df_dropped['x'], df_dropped['y'])
ax.set_xlim(-400, 400)
ax.set_ylim(-400, 400) 
plt.show()

# def update_chart(i):
#     # Get the latest data
#     new_data = df_origin[0+i:8000+i]   

#     # # Append the new data to the dataframe
#     # df.loc[i] = new_data

#     # Clear the previous plot
#     ax.cla()

#     # Plot the updated data
#     ax.plot(new_data['0'], new_data['0.1'])   

#     # Optionally set axis limits
#     ax.set_xlim(-400, 400)
#     ax.set_ylim(-400, 400)   

#     # Add labels and title
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_title('Real-Time Chart')

# def start_animation():
#     anim = FuncAnimation(fig, update_chart, interval=5)
#     plt.show()

# start_animation()