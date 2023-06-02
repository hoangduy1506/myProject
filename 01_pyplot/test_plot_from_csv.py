import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
df_origin = pd.read_csv("storeData.csv")
print(df_origin)
df = df_origin.copy()

def update_chart(i):
    # Get the latest data
    new_data = df_origin[0+i:8000+i]   

    # # Append the new data to the dataframe
    # df.loc[i] = new_data

    # Clear the previous plot
    ax.cla()

    # Plot the updated data
    ax.plot(new_data['0'], new_data['0.1'])   

    # Optionally set axis limits
    ax.set_xlim(-400, 400)
    ax.set_ylim(-400, 400)   

    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Real-Time Chart')

def start_animation():
    anim = FuncAnimation(fig, update_chart, interval=5)
    plt.show()

start_animation()