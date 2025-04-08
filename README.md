# DFA Simulator

A concise and efficient Python implementation of a Deterministic Finite Automaton (DFA) simulator. This tool allows users to define a DFA through command-line inputs and evaluate whether a given input string is accepted by the automaton.

## Features

- Customizable number of states and transitions
- User-defined start and final states
- Step-by-step simulation of input string traversal
- Validates input strings based on user-defined transition rules
- Lightweight and easily extensible

## How to Use

1. Run the script.
2. Input the number of states.
3. Define transitions for each symbol in the alphabet.
4. Provide the input sequence.
5. The program will determine whether the input is accepted by the DFA.

### Example

```bash
Enter number of states: 3
Enter state no: 0 is initial and last is final
Enter state for alphabet a from state 0: 1
Enter state for alphabet b from state 0: 2
...
Enter sequence: 0 1 0
The input sequence is accepted by the DFA.
