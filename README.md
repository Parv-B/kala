## kala

i've been learning music for over a decade. i want to enable a machine to teach itself.

raags form the foundation for Indian classical music. it provides a framework for the notes used (which to emphasize and which to avoid), encoding a variety of moods and emotions.

Indian classical music is a tradition that is taught not from written media but rather by listening, reproducing and experimentation. 
kala aims to replicate this by "training" a markov chain to learn raag yaman from training data and improvise on its own.

markov chains represent transition probabilites between different states in a sequence. an inhomogeneous Markov chain is a markov chain where the transition probabilities between states vary with more-than-one previous states in the sequence.

to tune the temperature of the output, a modified softmax normalization is used to tune the "improvisation".

a simple pure data patch is used to "audialaize" the output, communicated with over UDP.

areas for growth:
- increasing training data to more pieces of raag yaman, others raags
- exploring the use of GPTs for generation
- building a physical prosthetic for kala that allows it to interact with the physical world
    learning by listening
    producing using a speaker or physical instrument
