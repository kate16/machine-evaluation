import sys
#
# This file is used to extract information for students
# from the translations.tsv file
#

all_data = [pair.strip().split('\t') for pair in open("test-data/translations.tsv")]
# keep column names
titles = all_data[0]
# strip column names from the data
#all_data = all_data[1:len(all_data)]

for line in all_data:
    # The three reference translations
    ref_translations = line[2:5]
    # The four worker translations
    turk_translations = line[6:10]
    # Print out the important section
    sys.stdout.write("%s\n" % ref_translations[0])
