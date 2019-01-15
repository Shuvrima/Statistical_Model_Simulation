Name:Shuvrima Alam
Date: 11/27/2018

TO COMPILE:

python simulateDist.py <number-of-samples> <distribution> <parameters>

Example:
python simulateDist.py 4 poisson 9.0
Lambda is put as float.
---------------------------------------------------------------------------
python simulateDist.py 4 neg-binomial 5 2
All integer inputs.
---------------------------------------------------------------------------

NOTE:
All probability, lambda values are inputted as float and rest of the parameters as integers including alpha in gamma
distribution.

All the functions are implemented in one file and the main function is the entry point of the code.

IMPORTANT NOTE:
The following is  written in Python 2. Sometimes transferring files to
omega from windows machine where the files are used with other text
editor(having different space and tab settings)  can change indentation. Please excuse this problem as when I run there was no deliberate indentation error on
my part.

Following are some example test commands: 
python simulateDist.py 4 geometric 0.3
python simulateDist.py 4 uniform 9 10
python simulateDist.py 4 binomial 4 0.2
python simulateDist.py 4 bernoulli 0.2
python simulateDist.py 4 exponential 4.5
python simulateDist.py 4 arb-discrete 0.3 0.2 0.5
python simulateDist.py 4 neg-binomial 5 0.3
python simulateDist.py 4 gamma 4 2.5
python simulateDist.py 4 poisson 2.5
python simulateDist.py 4 normal 500 2


This program is simulation of different statistical models. The output generates random numbers from each distribution.