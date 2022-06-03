# MtG-Historical-Analysis
 Uses the Magic the Gathering API to build a localized database of card information and perform statistical analysis on the evolution of published cards over the course of the game's history. This project was developed in four parts as part of Simmons University's fall 2021 course, Data Interoperability.

 ###PART 1: Transforming Data
 The dataset is downloaded via basic API query and saved locally as JSON file. Data is extracted from JSON and loaded into a local database to perform the analysis described in Parts 2 & 3.

 ###PART 2: Charting Data
 MatPlotLib is used to create charts of several historical trends of interest over the game's development. Chart 1 is a multi-line graph depicting the numbers of cards of each major type published in each successive core set, to show trends in the relative numbers of e.g. creature cards vs. sorcery cards over time. Charts 2-1 through 2-3 sample three card sets of interest and depict their mana curves for different card types, i.e. the number of cards in the set broken down by card type and mana cost. Chart 3 shows the power and toughness of creatures relative to their mana cost over time on a scatter plot.

 ###PART 3: Analyzing Data
 This analysis will dig into the frequency with which Magic the Gathering has published cards of different type and cost over time, starting with the same data as the charts described in Part 2 and following any interesting trends which emerge in more detail. Additionally, the data set will be analyzed to select a few mechanical keywords and perform an analysis of how frequently those keywords appear in cards of each set, e.g.: the 2021 "Midnight Hunt" set is known for its use of cards with keyword "disturb": in what set and year did this keyword first appear, and how frequently has it been used since? Finally, create an HTML table showing how many counterspells were published in each set and what years those sets occurred in.

 ###PART 4: Presentation and Write-Up
 The methodology and results of the project will be presented in a ten-minute slideshow video with voiceover narration. A 2-3 page writeup of the experience of the project will accompany, and the dataset and code will be made available to classmates via GitHub for review.

## Installation
 This project is written in Python 3.9.4. It requires the additional libraries MatPlotLib, Requests, and SQLite.

## Usage
 Others are welcome to use and modify this project's code as they will. The programs are structured in such a way as to hopefully make it easy to rewrite them to answer new questions about the data set.

## Contributing
 This is a learner's project and contributions are welcome to expand upon or clean up the code.

## History
 Developed by Ray Stevens in November 2021 for Dr. Catherine Dumas's course 487 Data Interoperability at Simmons University, School of Library and Information Science, Boston, MA.

## Credits
 This project uses the Magic the Gathering API published at https://magicthegathering.io/. Thanks also to the folks at MatPlotLib (https://matplotlib.org/) for visualization tools, at Requests (https://docs.python-requests.org/en/master/index.html) for API handling, and at SQLite (https://sqlite.org/index.html) for database management.

## License
 MIT License

 Copyright (c) 2021 Ray A. Stevens

 Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
