Chapter 1
Cyber-Physical Systems: Overview

Кибер-фзические системы - это системы, в которых происходит взаимодействие кибер- и физических возможностей.

Приложения - автопилоты на самолетах и поездах, медицинские устройства, роботы-хирурги

Мультидинамическая система - система, сочетающая в себе разные виды динамики.

Гибридная система - математическая модель динамической системы, в которой присутствет как дискретная, так и непрерывная динамика.

- Гибридная игра - мультдинамическая система, сочетающая дискретные, непрерывные и адверсариальные динамики.
- Стохастическая гибридная система - мультдинамическая система, сочетающая дискретные, непрерывные и стохастические динамики.
- Распределенная гибридная система - мультдинамическая система, сочетающая дискретные, непрерывные и распределенные  динамики.

Before you read on, see if you can find the answer for yourself.

Note 5 (Descriptive power of differential equations) As a very general phe-
nomenon, observe that solutions of differential equations can be much more
involved than the differential equations themselves, which is part of the repre-
sentational and descriptive power of differential equations. Pretty simple dif-
ferential equations can describe quite complicated physical processes.

Note 7 (Continuous programs) Layer 1 of hybrid programs (HPs) comprises
continuous programs. If x is a variable, e any term possibly containing x, and
Q a formula of first-order logic of real arithmetic, then continuous programs
are of the form
$\alpha = x'=e&Q$


# Part I
# Elementary Cyber-Physical Systems

## Chapter 2
## Differential Equations & Domains
Каждый дифур определяет некоторое векторное поле в фазовом пространстве.

$x' = f(x)&Q$ - уравнение состемы, которая подчиняется $x' = f(x)$ и не выходит за пределы домена $Q$. 

HP - hybrid program

Общий вид непрерывной программы $x'=e&Q$
пример: $x'=v, v'=a&(v \geq 0 \land v \leq 10)$

Q - формула из логики первого порядка действительных чисел

Терм определяется рекурсивно. Переменные  и рациональные числа - термы, сумма и произведение термов - термы.

Все переменные и рациональные числ - атомарные термы. Все многочлены с рац коэффициентами - термы.

Формулы логики первого порядка действительной арифметики

P, Q ::= e ≥ ẽ | e = ẽ | ¬P | P ∧ Q | P ∨ Q | P → Q | P ↔ Q | ∀x P | ∃x P

Синтаксис дает нам правила для построения корретктных формул. Семантика дает им значение.

Значение терма в состоянии определяется рекурсивно.

$ω[[x]] = ω(x)$
$ω[[c]] = c$
$ω[[e + ẽ]] = ω[[e]] + ω[[ ẽ]]$
$ω[[e · ẽ]] = ω[[e]] · ω[[ ẽ]]$

$[[\cdot]] : Trm \to (\mathcal{S} \to \mathbb{R})$

Аналогично пожно поступить со значением формулы в состоянии.










