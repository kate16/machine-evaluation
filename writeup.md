Authors: Michael Browne, Luke Carlson, and Kate Miller

## Problem Definition
The invention and popularization of crowdsourcing platforms like Amazon's Mechanical Turk and CrowdFlower has led to a revolution in the creation of and analysis content for all academic disciplines. In the case of Machine Translation, crowdsourcing is commonly used to generate translations for languages with small samples of parallel corpora and evaluate translation quality. The value in doing this comes from the fact that crowdsourced tasks are completed by humans, not computers. That said, having untrained workers half a world work on translate documents into languages they might be unfamiliar with can lead to a variety of problems. One of these is picking the best translation from a group of crowdsourced translations. Sometimes you get lucky and get experts, other times you get people who don't even know english. In this project you'll write a program to pick the best translation from a group of crowdsourced translations given three reference translations.

## Relevant Papers and Textbook Sections ##
See below for a collection of resources that we used to come up with our ideas for this project.
 - Textbook Sections:
  - Chapter 8.1: Manual Evaluation
  - Chapter 8.2: Automatic Evaluation
  - Chapter 8.4: Task-Oriented Evaluation
 - Lecture Slides:
  - 2/12/15 - Evaluating Translation Quality Part 1
  - 2/17/15 - Evaluating Translation Quality Part 2
 - Papers:
  - Workshop on Creating Speech and Language Data with Amazon’s Mechanical Turk: Proceedings of the Workshop by Chris Callison-Burch and Marke Dredze (link: http://bit.ly/18Vh81X)
  - Crowdsourcing Translation: Professional Quality from Non-Professionals by Omar F. Zaidan and Chris Callison-Burch (link: http://bit.ly/1wTKqJU)
  - Fast, Cheap, and Creative: Evaluating Translation Quality Using Amazon’s Mechanical Turk by Chris Callison Burch (link: http://bit.ly/1BLCB89)

## Objective Function & Default ##
See below for brief descriptions of our scoring function and default implementation.

### Objective Function ###
Compare the pairs of ranked translation

### Default ###
Selects the first translation as the best translation for every sentence.

## Data Evaluation and Analysis

## Possible Extensions
- Learning the experts and beginners
