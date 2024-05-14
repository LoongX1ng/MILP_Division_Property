### Algorithm 1

This folder implementes the algorithm to select a set of linear inequalities from the H-Representation of a set of points, which corresponds to the Algorithm 1 presented in the paper.

此文件夹实现从一个点集的H表示中选择一组线性不等式的算法，对应文章中的算法1。
* [cipher_Inequalities.txt] ---This txt file contains the H-Representation of a given set of points, which is actually a set of linear inequalities returned by Sage software. Sage returns a linear inequality with the form $(a_1, a_2, ..., a_n)\cdot x^{T} + b >= 0$, this linear inequalty will be stored within a single line in cipher_Inequalities.txt with the form $(a_1, a_2, \cdots, a_n, b)$. The cipher_Inequalities.txt presented here contains all the linear inequalities among the H-Representation of the division trails of PRESENT Sbox with each line representing a single inequality.
* 此txt文件包含一个给定点集的H表示，实际上是一组由Sage软件返回的线性不等式。Sage以$(a_1, a_2, ..., a_n)\cdot x^{T} + b >= 0$的形式返回线性不等式，以$(a_1, a_2, \cdots, a_n, b)$的格式存在cipher_Inequalities.txt中，每个不等式一行。The cipher_Inequalities.txt包含PRESENT的S盒的可分轨迹的H表示的全部不等式，一行代表一个不等式。
* [cipher_Reduced_Inequalities.txt] ---This file contains the inequalities chosen by Algorithm 1. There are 10 inequalities for PRESENT Sbox as listed in this file.
* 此文件包含算法1选择的线性不等式。文件列出了PRESENT的S盒的10个线性不等式。
#### NOTE
PRESENT_Reduced_Inequality.txt contains 10 linear inequalities which are the linear description of division property propagations of PRESENT sbox. However, in our paper *Applying MILP Method to Searching Integral Distinguishers based on Division Property for 6 Lightweight Block Ciphers*, we presented 11 linear inequalites to describe the division property propagation for PRESENT Sbox. And the difference comes from the different implementations of Algorithm 1.

PRESENT_Reduced_Inequality.txt包含10个线性不等式，它们是PRESENT的S盒的可分性传播规则的线性描述。然而，在我们的论文《基于可分性使用MILP方法搜索6个轻量级分组密码的积分区分器》中，我们提出了11个线性不等式以描述PRESENT的S盒的可分性传播规则。此差异来自于对算法1的不同实现。

We implemented Algorithm 1 in C++ in an earlier version, and we destroyed the original order of the linear inequalities returned by Sage software. In this version we implemented Algorithm 1 in Python and we keep the original order, thus, the number of linear inequalites returned is a little less. However, this does not influence the results of the paper.

在早期版本中我们用C++实现算法1，我们破坏了Sage返回的线性不等式的原始顺序。在此版本中，我们用Python实现算法1，并保持了原始顺序，因此，返回的线性不等式数目略小。然而，这不影响本文的结果。
