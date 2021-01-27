We are going to be talking about safety issues in RL. Nominally it does not have a specific machinery for ensuring safety.

In a nutshell - agent (controller) interact with environment. Agent commonly consisd of actor and critic.

Envirronment can be deterministic of stochastic, with finite or infinite number of states, discrete or continous.

Agent can have finite or infinite number of actions. Agent tries to maximize te running cost. We want to find a policy such that it provides the biggest number of RC in every state.

RL does not have built-in safety and trustworthiness.

What is safety?Keeping the environment in some "safe" zone of state space.

*Model predictive control*

RL vs MPC?

infinite vs finite-horizon objective
the objective gets unwrapped vs objective can be identified ditectly
everything is encoded in the value function
model-free, data driven vs thorough convergence ans safety analysis
lack of prediction and imperfection of NN compromise safety vs reduced optimality

Overseer-based RL
- introduction of a human superviser
- needs tedioud human work
- no formal guarantees

Let us replace a human with automated "shield", which wouldbe logically based. For example, temporal logic.
18:50
"Shield" filtering out unsafe actions, 2017
Formalizing is difficult.

Safe RL by fution with MPC.
*Fusion of RL with robust MPC*

Learning-based MPC.

Backpropagation will fail here. It is possible to propagate probability through time.

We need a well-calibtated statistical models.

RL dreamer.

Lyapunov-based safe RL. If there is an energy in the setting that is going away, then the agents should make an allianz.

Barrier functions for safe RL. The approach in untractable, and the approximate approach converges slowly.

And another 5 different examples

Time discretization on Q-Learning

Safety is beng recognized

rcognita











