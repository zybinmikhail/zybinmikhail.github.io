# ISP project report
## Mikhail Zybin
## February 2021

I had the following objectives
- read some papers in order to understand how Hi-C procedure works
- increase the basic knowledge of biology
- generate ideas about what can be done with Hi-C matrix

I decided to listen to the lectures from the edX course "Introduction to Biology - The Secret of Life". Namely, I gained knowledge in the following themes
- Introduction to chemistry and life
- Biochemistry - Enzymes, Proteins and Glycolysis
- Genetics: The work of Mendel and T. H. Morgan

Here is the short summary of what I have studied.

Covalent bond between atoms is a situation whem atoms share electrons. It can be single, double and triple. The main elements that constitute living organisms are hydrogen, carbon, oxygen, nitrogen, phosphorus, and sulfur. Electronegativity of an atom is its ability to attract electrons to itself when bounded to anoother atom. There exist Hydrogen bonds, van der Vaals forces, and ionic bonds (I will not go into much details here). Polar molecules are hydrophilic, nonpolar molecules are hydrophobic. 

Proteins are chains of animoacids. There are 20 aminoacids that are found in organisms. Some of them are nonpolar, soma are polar and uncharged, some are polar and positively charged, and some are polar and negatively charged.

It is a very complicated task to determine the protein's secondary structure given the sequence of aminoacids. However, there are often-occuring structures such as alpha-helices and beta-sheets. Enzymes are proteins that act as catalizers in chemical reaction. 

Gene is a discrete factor of inheritance. Allele is an alternative type of gene. An organism is said to be a homozygote, if it has two same alleles of a gene. An organism is said to be a heterozygote, if it has two different alleles of a gene.

I have read the following papers

- [Organization and function of the 3D genome](https://www.nature.com/articles/nrg.2016.112?spMailingID=52532022&spUserID=MTc2NzQ3MDc1OAS2&spJobID=1022653213&spReportId=MTAyMjY1MzIxMwS2)

- [Iterative correction of Hi-C data reveals hallmarks of chromosome organization](https://www.nature.com/articles/nmeth.2148)
 
- [The Hitchhiker's Guide to Hi-C Analysis: Practical guidelines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4347522/)

Chromosome conformation capture techniques are set of methods used to determine spacial organization of chromatin in a cell.

There is a variety of methods: 
- 3C; able to discover the interaction of one fragment with another one (one-vs-one)
- 4C; able to discover the interaction of one fragment with all others (one-vs-all)
- 5C; many-vs-many
- Hi-C; able to discover the interaction between all fragments (all-vs-all)

All methods start similarly.

> In 3C, cells are cross-linked using formaldehyde, lysed and the chromatin is then digested with a restriction enzyme of choice (typicallyHindIII or EcoRI). The chromatin is then extracted and the restriction fragments are ligated under very dilute conditions to favor intra-molecular ligation over inter-molecular ligation. The crosslinks are then reversed, proteins are degraded and DNA is purified. The newly generated chimeric DNA ligation products represent pairwise interactions (physical 3D contacts) and can then be analyzed by a variety of down-stream methods. This results in a collection of chimeric DNA fragments consisting of a ligation of DNA sequences from two interacting loci.

Then the following steps are performed:

1. Read Mapping
2. Fragment Assignment
3. Fragment Filtering
4. Binning
5. Bin Level Filtering
6. Balancing

Hi-C may be too noisy and biased. Solving this problem is an important challenge.

>*Hi-C data can contain many different biases, some of known origin and others from an unknown origin.*
>
>The Hitchhiker's Guide to Hi-C Analysis: Practical guidelines

In original paper, although, the contrary is stated

>*Hi-C allows unbiased identification of chromatin interactions across an entire genome.*
>
>Comprehensive mapping of long range interactions reveals folding principles of the human genome

There is an iterative algorithm that is guaranteed to converge:
1. Divide each row of the matrix by its sum
2. Divide each column of the matrix by its sum

HiC measures frequency between loci, not distance. Week signal means that a small population of cells had it. Here are the levels of interactions that might be observed in data:

1) Cis/trans interaction ratio
2) Distance-dependent interaction frequency
3) Genomic compartments
4) Topological domains
5) Point interactions

Possilble future directions:
- learn to use `cooler` library to work with genomically-labeled sparse 2D arrays
- investigate how the Hi-C matrix depends on species, age, and cell line
- understand the mechanisms of systematic biases and how to fight them
- smoothen the matrix using Nadaraya-Watson kernel density estimation instead of making a 2D histogram
	- if that does not work, apply DL techniques to increase resolution
- apply various numerical linear algebra tools, such as LU-decomposition, QR-decomposition, SVD, eigendecomposition, two-dimentional Fourier transform, etc
- interpet the matrix as Markov Chain transition matrix
- explore whether a concept of fractal dimentionality fits here, and calculate it
- explore the possibility of inferring 3D structure of the DNA via numerical optimization