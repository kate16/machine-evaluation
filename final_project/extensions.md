##Final Project Extensions

####Extension 1: Luke Carlson
For my extension I implemented a stemming method to complement the Levenshtein distance method. Without stemming, small differences between translations can seem much more drastic. For example the Levenshtein distance between "I began to run quickly" and "I began running quick" is 8. If we stem both sentences to "I began to run quick" and "I began run quick" the distance drops to 3. Stemming then helps us distinguish between different word choices and just different tenses.

To run/grade this extension:
```
./extension-luke > luke.out   # create output
./grade < luke.out            # score (grade-dev)
```

####Extension 2: Kate Miller
For my extension, I used sentence-level BLEU scores to rank the hypothesis Turker translations, comparing them against the first reference translation. We selected BLEU as one of the baseline extensions because we wanted a system that would correspond closely with human fluency, which BLEU is effective for. This metric was meant to replace the Levenshtein Distance metric used in the baseline, but was found to be about as effective. The Levenshtein baseline achieved a score of 0.559288026529, while the sentence-level BLEU achieved a score of 0.557458581711.

To run/grade this extension:
```
./extension-kate > kate.out   # create output
./grade < kate.out            # score (grade-dev) = 0.557458581711
```

####Extension 3: Mike Browne
Instead of counting the number of common n-grams between each translation and its reference, I counted the number of common n-grams between each translation and the entire reference corpus. I experimented with several different lengths for my n-grams and found that a range of n-grams of lengths 1 word to 9 words produced the highest-scoring output. With this combination I recieved a score of 0.571586198729 beating the baseline's score of 0.559288026529.

To run/grade this extension:
```
./extension-mike > mike.out   # create output
./grade < mike.out            # score (grade-dev) = 0.571586198729
```
