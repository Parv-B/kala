i've been learning music for over a decade. i want to teach a harmonium to play itself.

to-dos:

1. clean up file structure - ongoing

2. sequence-generation
markov chains represent transition probabilites between different states. an inhomogenous markov chain could be "taught" vadi-samvadi and varjit rules from playback.
how much should i train?
- overfitting would probably cause the model to get stuck in small loops with little "exploration"
- without enough training, the music produced would sound unguided and random

code/inmarkov.ipynb does a mediocre job of generating new sequences
need to explore paramteric "temperature" to generation to increase variance

networkx provides an interesting insight for homogenous (order = 1) chains, anything more is incomprehensible
- animation?

3. sound generation
- "prosthetic" for harmonium that records & plays the sequence
- servos or solenoid?
    solenoid clicking on the harmonium keys could also provide "percussion"? (like guitar)
