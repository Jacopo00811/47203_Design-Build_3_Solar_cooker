import numpy as np
import matplotlib.pyplot as plt

def read_data_lvm_file(file_name, skip_header):
    return np.genfromtxt(fname=file_name, skip_header=skip_header)

def extract_column_from_data_with_index(data, column_index):
    return [row[column_index] for row in data]

def create_sub_plot(ax, x_values, y_values, label='', color='b', title=None, xlabel=None, ylable=None, use_offset=False):
    ax.plot(x_values, y_values, color=color, lw=2, label=label)
    ax.set_xlim([min(x_values), max(x_values)])
    ax.grid(color='b', linestyle='-', linewidth=0.2)
    ax.legend(loc='upper left', fontsize='large')
    if use_offset:
        ax.ticklabel_format(axis='y', useOffset=False)
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize='large')
    if ylable is not None:
        ax.set_ylabel(ylable, fontsize='large')

def plot_temperature_as_a_function_of_time(time, temperature, title, save=False):
    fig, ax = plt.subplots()
    create_sub_plot(ax, x_values=time, y_values=temperature, label='Temp1', color='r', title=title, xlabel='Time', ylable='Temperature ($\degree$K)')
    plt.show()
    if save:
        fig.savefig('plot1.png')

def solve_problem_01(data):
    time = extract_column_from_data_with_index(data=data, column_index=0)
    temperature = extract_column_from_data_with_index(data=data, column_index=1)
    plot_temperature_as_a_function_of_time(time, temperature, title='TestTC_17-12-06_1439')

def solve_problem_02(data):
    time = extract_column_from_data_with_index(data=data, column_index=0)
    temperature_01 = extract_column_from_data_with_index(data=data, column_index=1)
    temperature_02 = extract_column_from_data_with_index(data=data, column_index=2)
    temperature_03 = extract_column_from_data_with_index(data=data, column_index=3)

    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    create_sub_plot(ax1, time, temperature_01, label='Temp01', color='r', title='TestTC_17-12-06_1439')
    create_sub_plot(ax2, time, temperature_02, label='Temp02', color='b', ylable='Temperature ($\degree$K)', use_offset=False)
    create_sub_plot(ax3, time, temperature_03, label='Temp03', color='g', xlabel='Time')
    fig.subplots_adjust(hspace=0, left=0.15)
    plt.show()

def calculate_q_from_temperature_data(temperature_data, t0, specific_heat, mass):
    return [(mass*specific_heat*(temperature-t0))/1000 for temperature in temperature_data]

def solve_problem_03(data):
    time = extract_column_from_data_with_index(data=data, column_index=0)
    temperature = extract_column_from_data_with_index(data=data, column_index=1)
    q = calculate_q_from_temperature_data(temperature, t0=300, specific_heat=4.186, mass=100)

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    create_sub_plot(ax1, time, temperature, color='r', title='TestTC_17-12-06_1439', ylable='Temperature ($\degree$K)')
    create_sub_plot(ax2, time, q, color='b', ylable='Q (KJ)', xlabel='Time')
    plt.subplots_adjust(hspace=0)
    plt.show()

def main():
    data= read_data_lvm_file(file_name='TestTC_17-12-06_1439.lvm', skip_header=23)
    #solve_problem_01(data=data)
    #solve_problem_02(data=data)
    solve_problem_03(data=data)

if __name__ == "__main__":
    main()
