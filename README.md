# MtG-Historical-Analysis
 Uses the Magic the Gathering API to perform statistical analysis on the evolution of published cards over the course of the game's history.

 PART 1: Transforming Data
 The dataset will be downloaded either via basic API query or taken from the Python SDK and saved locally as a series of JSON files. Data will be extracted from these files and loaded into database files/tables as needed to perform the analysis described in Parts 2 & 3.

 PART 2: Charting Data
 MatPlotLib will be used to create charts of several historical trends of interest over the game's development. One will be a multi-line graph depicting the numbers of cards of each major type published in each successive card set, to show trends in the relative numbers of e.g. creature cards vs. sorcery cards over time. Another series of charts will sample several card sets of interest and depict their mana curves for different card types, i.e. the number of cards in the set broken down by card type and mana cost. A third will show  the power and toughness of creatures relative to their mana cost over time.

 PART 3: Analyzing Data
 This analysis will dig into the frequency with which Magic the Gathering has published cards of different type and cost over time, starting with the same data as the charts described in Part 2 and following any interesting trends which emerge in more detail. Additionally, the data set will be analyzed to select a few mechanical keywords and perform an analysis of how frequently those keywords appear in cards of each set, e.g.: the 2021 "Midnight Hunt" set is known for its use of cards with keyword "disturb": in what set and year did this keyword first appear, and how frequently has it been used since? Finally, create an HTML table showing how many counterspells were published in each set and what years those sets occurred in.

 PART 4: Presentation and Write-Up
 The methodology and results of the project will be presented in a ten-minute slideshows video with voiceover narration. A 2-3 page writeup of the experience of the project will accompany, and the dataset and code will be made available to classmates via GitHub for review.

## Installation
 This project is written in Python 3.9.4. It requires the additional libraries MatPlotLib, Sqlite, and Mtgsdk, all of which are available via Pip.

## Usage
 TODO: Write usage instructions

## Contributing
 TODO: Write contributor suggestions

## History
 Developed by Ray Stevens in November 2021 for Dr. Catherine Dumas's course 487 Data Interoperability at Simmons University, School of Library and Information Science, Boston, MA.

## Credits
 This project uses the Magic the Gathering API published at https://magicthegathering.io/ and its associated Python SDK at https://github.com/MagicTheGathering/mtg-sdk-python/. Thanks also to the folks at MatPlotLib (https://matplotlib.org/) for visualization tools.

## License
 TODO: Decide on licensing
