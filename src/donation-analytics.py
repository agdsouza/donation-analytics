from data_initializer import DataInitializer
from data_calculator import DataCalculator
from data_outputer import DataOutputer
import os

# creating file paths for the inputs and outputs
file_dir = os.path.dirname(os.path.realpath('__file__'))

input_path = os.path.join(file_dir, '../input/itcont.txt')
input_path = os.path.abspath(os.path.realpath(input_path))
percent_path = os.path.join(file_dir, '../input/percentile.txt')
percent_path = os.path.abspath(os.path.realpath(percent_path))
output_path = os.path.join(file_dir, '../output/repeat_donors.txt')
output_path = os.path.abspath(os.path.realpath(output_path))

# initialize data to get ready for calculations
raw_data = DataInitializer(input_path)
raw_gen = raw_data.get_data()
filtered_data = raw_data.filter_data(raw_gen)
repeat_gen = raw_data.get_data()
repeat_filter = raw_data.filter_data(repeat_gen)
raw_data.set_nonrepeat_donors(repeat_filter)
clean_gen = raw_data.get_repeat_donors(filtered_data)

# execute calculations for all the returned elements
data_calc = DataCalculator(clean_gen, percent_path)
proc_data = data_calc.process_data()

# format the results and output them into a text file
output = DataOutputer(proc_data, output_path)
output.write_to_txt()

