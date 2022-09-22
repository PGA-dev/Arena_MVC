# Arena_MVC
### MVC Battlegame for python
## PGA

### Concept
This project began as a merging of two simple ideas: 
1. How can I make a version of our NuCamp intro to Python game, that doesn't suck
2. How can I incorporate MVC design patterns into the game


### Technology Used
* Python
* Basic MVC design pattern developed from G. Debidda's MVC patterns article series (originally a simple 3 field--table--usage, but fairly useful as a character creation approach if re-designed...so a nod to GD for the great insight on how to use this useful design pattern in a simple, practical way to understand at the intermediate level): https://www.giacomodebidda.com/posts/mvc-pattern-in-python-dataset/  4-15-2017
* SQLite3 (PostGreSQL eventually)

#### Files included/ Separation of Concerns:
1. Original Battlegame.py from NuCamp's week1 python classes
2. This README
3. The Arena game's driver code
4. dunder init file (my favorite)
5. basic helper methods file: arena_method.py
6. Backend CRUD
7. Exceptions file
8. Controller
9. Model
10. View