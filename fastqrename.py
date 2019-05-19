#fastqrename will rename DKFZ fastq files to fit bcl2fastq format
#Anthony Hill
#05/2019
fastq_dir = "/Users/tony/fastqrename/fastqs/"
analysis_dir = "/Users/tony/fastqrename/analysis/"
target_directory = "/Users/tony/fastqrename/renamedfastqs/"
import os
from subprocess import call
import csv


# Read sample table, make sample dictionary of identifier/sample number pairs
with open('/Users/tony/fastqrename/15051-resultData.csv', mode='r') as csv_file:
    sampleNo_dict = {}
    sampleName_dict = {}
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        sampleNo_dict[row['\ufeffIdentifier'][:9]] = row['Protocol']
        sampleName_dict[row['Protocol']] = row['Sample Name']

# Read filenames
file_list = os.listdir(fastq_dir)

#extract sample and run data, copy renamed file
lane_dict = {'LR-43602':'L001', 'LR-43603':'L002'}
file_count = 0
for file in file_list:
    sObject = slice(-1,-9,-1)
    file_end = file[sObject]
    if file_end == 'zg.qtsaf':
        print (file)
        sample_ID = file[:10]
        sample_number = sampleNo_dict[sample_ID[:9]]
        sample_name = sampleName_dict[sample_number]
        lane = file[10:18]
        lane_number = lane_dict[lane]
        format_file = sample_ID+sample_name+"_"+sample_number+"_"+lane_number+"_"+file[-11:]
        command = "cp "+fastq_dir+file+" "+target_directory+format_file
        print("executing:"+command)
        os.system(command)
        print(format_file+" successfully saved")
        file_count += 1
print(str(file_count)+" files saved")

