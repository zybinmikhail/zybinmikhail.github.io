https://www.biorxiv.org/content/10.1101/724005v1.full.pdf

Авторы предлагают основанный на глубоких нейронных сетях метод, который позволяет по первичной структуре ДНК предсказывать Hi-C данные.

Энхенсер должен прореагировать с промотером, чтобы запустить экспрессию генов. 

Hi-C медленное и дорогое.

Авторы утверждают, что их модель дает предсказания высокого разрешения, позволяющие смотреть на множество разных уровней организации ДНК.

When optimizing the network architecture and data encoding (Figure 1B, Supplementary Figure 1A), we found twofactors crucial for successful learning and generalization: 
- First, we normalize the proximity signal in Hi-C data bypercentile normalizing the interactions stratified over different genomic distances (Supplementary Figure 1B, for detailssee methods). Effectively this skeleton encoding reveals the informative longer range interactions underlying Hi-C data.
- Second, we found a two-step training process to yield much better results (Fig 1A, Supplementary Figure 2). 
	- We firsttrain a convolutional neural network to predict a compendium of chromatin features (eg, open chromatin regions, CTCFbinding site etc.). 
	- We then use the hidden layers of the trained network to seed the first layers of our chromatininteraction network. 
The full network then simultaneously optimizes the initial layers and learns to combine themthrough the dilated convolutional layers to predict chromatin interactions. This can be conceptualized as transferlearning, where the network learns to recognize chromatin features from DNA sequence first and then learns to use thelearned underlying sequence patterns and combine them over large distances for chromatin interaction prediction. Weobserved fast convergence when seeding with a pre-trained chromatin feature network.

Что такое NG Caption-C.