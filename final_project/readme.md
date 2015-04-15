## File Structure
`data-test/` contains the source data used for this project

`data-dev/` contains all the data availible to students as they try to complete the assignment

`file-parser.py` was used to create the files in data-dev/

`default` provides skeleton code for students and implements the default score for the assignment

`baseline` provides a skeleton for the baseline for this assignment

`baseline-solution` provides a solution to the baseline skeleton for the project

## Running Default Code
The default system ranks the translations in order
```
./default-evaluation.py > default.out   # create default output
```

## Running Baseline Code
The baseline system uses Levenshtein Distance to rank the translations
```
./baseline-solution.py > baseline.out   # create baseline output
```

##Evaluation
Grading the output files by comparing their ordering to that of an output file based on BLEU-ranked translations with access to the entire reference corpus
```
./grade < default.out   # score (grade-dev) = 0.504553379917
./grade < baseline.out  # score (grade-dev) = 0.559288026529
```

## Markdown Files

`readme.md` file describing the basics of

`report.md` final version of our writeup

`extensions.md` file describing the extensions implemented and their performance
