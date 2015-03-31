import sys

turker_translations = [pair.strip().split('\t') for pair in open("student-data/turker_translations.tsv")]
ref_translations = [pair.strip().split('\t') for pair in open("student-data/first500references.tsv")]

# the first value of each array contains the column names
turk_titles = turker_translations[0]
ref_titles = ref_translations[0]

# strip column names from the data
turker_translations = turker_translations[1:len(turker_translations)]
ref_translations = ref_translations[1:len(ref_translations)]


for i in range(0,len(turker_translations)):
    # an array of the four turker translations
    options = turker_translations[i]

    # students get the first 499 reference translations
    if (i < 499):
        # an array of the four ref translations
        references = ref_translations[i]

    best = ''
    # iterate through each turker translation for the sentence
    for option in options:
        # for the baseline we just choose the first translation
        best = option;
        break;
    
    sys.stdout.write("%s\n" % best)
