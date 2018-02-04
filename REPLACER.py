import csv
import shutil #
import os #

print('############# LINE REPLACER ################')
print('######### CC - Jason Whittle, 2017 #########')
print('''
───▄▄▄───▄██▄──█▀───█─▄    \\
─▄██▀█▌─██▄▄──▐█▀▄─▐█▀______\\_
▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌      //
▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄    //
''')

print('Do not put .csv at the end of the filename')
filename = input('file name: ')
print('')
print('NOTES')
print('#######################################')
print('* The original file has "_old" at the end')
print('* The file with "_step" does not need to be kept. It is used to generate the new file')
print('* The fixed file has the exact name of the orignial file')
print('')

filename = filename + '.csv'
filename_old = filename[0:-4] + '_old' + '.csv'
filename_step = filename[0:-4] + '_step' + '.csv'

# This will rename your file to filename_old.csv
os.rename(filename, filename_old)

# Read as a csv object
obj_file_in = open(filename_old, 'r', newline='')
obj_csv_in = csv.reader(obj_file_in, delimiter=',')

# this will use the second row to store the string to check as test_string
row_number = int(1)
for row in obj_csv_in:
    if row_number == 2:
        test_string = row[0]
    elif row_number > 3:
        break
    row_number +=1

print('DETERMINED VARIABLES')
print('#######################################')
print('Row 2 Column A (string to test each row): ', test_string)

# create a new step file with the original filename and write good rows only to it
bad_rows_numbers = []
bad_rows_strings = []
row_number = int(1)
with open(filename_step, 'w', newline='') as obj_file_out:
    obj_csv_out = csv.writer(obj_file_out, delimiter=',')
    with open(filename_old, 'r', newline='') as obj_file_in:
        obj_csv_in = csv.reader(obj_file_in, delimiter=',')
        for row in obj_csv_in:
            if row_number == 1:
                obj_csv_out.writerow(row)
            elif row[0] != test_string:
                bad_rows_numbers.append(row_number)
                bad_rows_strings.append(row)
            else:
                obj_csv_out.writerow(row)
            row_number += 1

# This chunk will figure out the rows that need to have the bad rows appended to them (fixing rows)
bad_row_num_new = []
v = 1
for e in bad_rows_numbers:
    new_bad_row_number = e-v
    bad_row_num_new.append(new_bad_row_number)
    v += 1

# make the final file, write good rows that dont need appending, append 'fixing rows'
row_number = int(1)
fix_count = int(0)
with open(filename, 'w', newline='') as obj_file_out:
    obj_csv_out = csv.writer(obj_file_out, delimiter=',')
    with open(filename_step, 'r', newline='') as obj_file_in:
        obj_csv_in = csv.reader(obj_file_in, delimiter=',')
        for row in obj_csv_in:
            if row_number in bad_row_num_new:
                temp_row = row + bad_rows_strings[fix_count]
                fix_count += 1
                obj_csv_out.writerow(temp_row)
            else:
                obj_csv_out.writerow(row)
            row_number += 1

print('')
print('bad_rows in old file', bad_rows_numbers)
print('')
print('bad_rows in step file', bad_row_num_new)
print('')
print('BAD ROWS FOUND')
print('#######################################')
row_counter = int(0)
for string in bad_rows_strings:
    print('')
    print('row number: ', bad_rows_numbers[row_counter])
    row_counter += 1
    print(string[0:2])
print('')
print('#######################################')
print('       DONE, HIT ENDTER TO EXIT        ')
print('#######################################')
input()
