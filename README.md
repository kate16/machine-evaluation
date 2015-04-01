# machine-evaluation

## Project Structure
all-data/ contains the source data used for this project
    
student-data/ contains all the data availible to students as they try to complete the assignment

file-parser.py was used to create the files in student-data/

default-evaluation.py provides skeleton code for students and implements the default score for the assignment

## Running Default Code
The general idea of the default code is to just choose the first turker translation for each line regardless of quality.
    
```
python default-evaluation.py > default.out
```

##Evaluating BLEU Score
BLEU is used to evaluate the success of the system. 

```
python compute-bleu < default.out
```
