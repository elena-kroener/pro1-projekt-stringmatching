# String Matching

String Matching is a simple program that finds the starting position of a string in another string, .txt-file or folder.

It uses the Knuth-Morris-Pratt-Algorithm (KMP).

## Requirements
To run the program, you need to install `argparse`.

## Usage
You can use the program with your command line.
1. Run the file `matcher.py`.
2. Required arguments are `suche`, the string you want to search and the string, file or folder you want to search in.
3. Optional arguments are `-i`, to set the search to case-insensitive, and `-n`, to use a naive search algorithm instead of KMP.

## Examples
`python matcher.py suche "great" "That's really great"`

Output: 14

`python matcher.py suche -i -n "Great" "That's really great"`

Output: 14

`python matcher.py suche -i "Great" "example\news.txt"`

Output: 389, 1116, 1280, 1848, 3636, 4225, 4475

## Author
Elena Kröner

Matrikelnummer: 780552

ekroener@uni-potsdam.de


Wintersemester 2020/21

Programmierung I

Universität Potsdam
