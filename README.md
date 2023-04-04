<!------------------------------------------ TITLE BLOCK --------------------------------------------------------------->
<h1 align="center"> Kingdom Hearts: Re:Chain of Memories Card Dataset </h1>

<p align="center">
  Scripts to retrieve, filter, and combine battle cards from the game Kingdom Hearts: Re:Chain of Memories
</p>


<!------------------------------------------ TABLE OF CONTENTS ---------------------------------------------------------->
<details open="open">
  <summary><h2 style="display: inline-block"> Table of Contents </h2></summary>
  <ol>
    <li>
      <a href="#about-the-project"> About The Project </a>
      <ul>
        <li><a href="#battle-card-mechanics"> Battle Card Mechanics </a></li>
        <li><a href="#job-to-be-done"> Job To Be Done </a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started"> Getting Started </a>
      <ul>
        <li><a href="#prerequisites"> Prerequisites </a></li>
        <li><a href="#how-to-run"> How to Run </a></li>
      </ul>
    </li>
    <li><a href="#file-architecture"> File Architecture </a></li>
  </ol>
</details>


<!------------------------------------------ About The Project ---------------------------------------------------------->
## About The Project

After finishing Kingdom Hearts: Re:Chain of Memories and a data science project-based course, I was motivated to contribute a
dataset of my own of all battle cards featured in Kingdom Hearts: Re:Chain of Memories (specifcally for Sora's story mode). All card
stats and descriptions will be scraped from https://www.khguides.com/.

The dataset will contain battle cards, specifically attack, magic, item, friend, and enemy cards. A unique combat mechanic 
were sleights, where stocking three cards can trigger combos depending on their prerequisites. I plan to implement scripts to 
detect/suggest all sleights from a given deck.

### Battle Card Mechanics

### Job To Be Done
1.
2.
3.


<!------------------------------------------ Getting Started ---------------------------------------------------------->
## Getting Started
To get a local copy up and running follow these steps.

### Prerequisites
Clone the repository:
```
git clone https://github.com/kendrick010/KH-CoM-Card-Dataset.git
```

Install the following dependencies:
* requests
* beautifulsoup4

or alternatively run,
```
pip install -r requirements.txt
```

### How to Run

<!------------------------------------------ File Architecture  ---------------------------------------------------------->
## File Architecture
