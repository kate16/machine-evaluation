# machine-evaluation

## Project Structure
all-data/ contains the source data used for this project
    
student-data/ contains all the data availible to students as they try to complete the assignment

file-parser.py was used to create the files in student-data/

default-evaluation.py provides skeleton code for students and implements the default score for the assignment

## Running Default Code
The general idea of the default code is to just choose the first turker translation for each line regardless of quality.
    
```
./default-evaluation.py > default.out
```

## Running Baseline Code
Basic Levenshtein distance is used for the baseline
```
./baseline-solution.py > baseline.out
```

##Evaluation

```
./grade < default.out
./grade < baseline.out
```
Outputs:

Default: 0.504553379917

Baseline: 0.559288026529
