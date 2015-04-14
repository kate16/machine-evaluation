##Luke's Extension over baseline

For my extension I implemented a stemming method to complement the Levenshtein distance method. Without stemming, small differences between translations can seem much more drastic. For example the Levenshtein distance between "I began to run quickly" and "I began running quick" is 8. If we stem both sentences to "I began to run quick" and "I began run quick" the distance drops to 3. Stemming then helps us distinguish between different word choices and just different tenses
