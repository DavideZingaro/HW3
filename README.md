# Homework 3 - What movie to watch tonight?

<p align="left">
<img src="https://d3c1jucybpy4ua.cloudfront.net/data/63462/big_picture/popcorn.jpg?1567006493" height=430 
</p>
  
The purpose of the project was to build a search engine over a list of movies that have a dedicate page on Wikipedia.

The repository consists of the following files:
* `collector.py`: a python file that contains the line of code needed to collect data from the `html` pages 1,2,3 of Wikipedia. args(movies1, movies2, movies3, path where you want to save .html files)
* `collector_utils.py`: a python file that stores the function we used in `collector.py`.
* `parser.py`: a python file that contains the line of code needed to parse the entire collection of `html` pages and save those in `tsv` files. args(# pages to download, path to .html files, path where you want to save .tsv files, path to save films data frame)
* `parser_utils.py`: a python file that gathers the function we used in `parser.py`.
* `index.py`: a python file that once executed generate the indexes of the Search engines. args(path to the film dataframe)
* `index_utils.py`: a python file that contains the functions we used for creating indexes.
* `utils.py`: a python file that gather functions we need in more than one of the previous files like (`collector`, `parser`, etc.)
* `main.py`: a python file that once executed build up the search engine. args(searche engine[1,2,3], "yout query")
* `exercise_4.py`: python file that contains the implementation of the algorithm that solves problem 4.
* `main.ipynb`: a Jupyter notebook that explains the strategies we adopted solving the homework and the Bonus point (visualization task).
