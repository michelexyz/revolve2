<a href="https://zenodo.org/badge/latestdoi/17549/ci-group/revolve2"><img src="https://zenodo.org/badge/17549/ci-group/revolve2.svg" alt="DOI"></a>
<img  align="right" width="150" height="150"  src="/docs/source/logo.png">

# Revolve2
Revolve2 is a Python package for optimization, geared towards modular robots and evolutionary computing.
Its primary features are a modular robot framework, wrappers around physics simulators, and evolutionary optimizers.
It consists of multiple smaller python packages and optional supplementary packages that contain varying functionality that is not always required.

## Reason of the fork
The fork was made to explore modifications to the package I used in my research project on Evolutionary Computing at Vrije Universiteit. My focus for the experimentation was on developing a fitness function that penalized robots for exceeding a certain height, like during a jump, to prevent potential damage in real-world scenarios. To achieve this, I needed to adjust how the robot's states were sampled in the simulation. Instead of only considering the initial and final states, I included intermediate states to effectively monitor if the robot exceeded the threshold height.

## Reason for closing the repo
I continued working on the Evolutionary Computing project on another repo: [Origin of Simmetry](https://github.com/satchitchatterji/OriginOfSymmetry).


## Documentation
[ci-group.github.io/revolve2](https://ci-group.github.io/revolve2/)
