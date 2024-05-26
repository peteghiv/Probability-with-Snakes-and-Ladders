# Probability in Snakes And Ladders
This is based on a Mathematics project I did in IP4 (Grade 10) and submitted for the Singapore Mathematics Project Festival (SMPF) where I won a Bronze award.

The paper presents a generalised approach to find the probability of going from square $i$ to square $j$ in $x$ moves, where we use an $n$-sided dice and a board with $k$ squares.

The proposed approach is as follows:
- Create a Markov Chain, where we represent each square as an event.
- Use the Markov Chain to construct a Transition Matrix, say $P$.
- The required answer is given by $P^x_{ij}$.

## Format of Input File
The first line contains the variables $k$, $s$, and $n$ space separated, where $s$ represents the number of "special" squares (i.e. a snake, or a ladder).

$s$ lines follow. In each of these $s$ lines there are variables $a$ and $b$ space separated, which indicates that square $a$ is connected to square $b$. For example, $12$ $20$ indicates that a ladder connects square $12$ to square $20$ (where a ladder is implied since $20>12$.) 

## Non-Code Files
- sample_board.jpg: https://www.ymimports.com/pages/how-to-play-snakes-and-ladders
- input.txt: An input text file based on sample_board.jpg
- smpf_board.jpg: A simplified board used during the SMPF paper to outline the method.
- smpf_input.txt: An input text file based on smpf_board.jpg