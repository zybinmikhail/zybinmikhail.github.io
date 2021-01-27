Бывает формальная верификация - когда ищется вопрос "Правльно ли мы сделали то, что сделали?"
Бывает формальная валидация - когда ищется вопрос "Правльно ли мы собираемся делать то что хотим?"

2 типа
- model checking
	- temporal logics
- deductive verification
	- proof assistants
		-  HOL, ACL2, Isabelle, Coq or PVS
	- automatic theorem provers
		- satisfiability modulo theories
- abstract interpretation
- type systems
- ...

KeYMaera X - deductive verification tool для дифференциальной динамической логики и дифференциальной логики игр 

JSC - justified speculative control, первый способ создания доказуемо безопасных RL-агентов
- off-line verification
- runtime monitoring
- RL

Как передавать доказательства безопасности RL-алгоритмам?

A plant in control theory is the combination of process and actuator. A plant is often referred to with a transfer function (commonly in the s-domain) which indicates the relation between an input signal and the output signal of a system without feedback, commonly determined by physical properties of the system. An example would be an actuator with its transfer of the input of the actuator to its physical displacement. In a system with feedback, the plant still has the same transfer function, but a control unit and a feedback loop (with their respective transfer functions) are added to the system. 
[link](https://en.wikipedia.org/wiki/Plant_(control_theory))

$s \models P$ означает, что P истинно в состоянии s
$[\alpha]\phi$ означае, что $\phi$ верна во всех состояниях, достижимых при запусках $\alpha$

$\langle \alpha \rangle \phi$ означае, что $\phi$ верна в некоторых состояниях, достижимых при запусках $\alpha$

$\alpha^*$ означает повторить программу альфа ппроизвольное недетерминированое число раз

### ModelPlex
KeYMaera дает механизм перевода формул вида $P \to [\alpha^*]Q$ в арифметические формулы.

Имеется две сущности - 
Controller Monitor $A \times S \to \{0, 1\}$
Model Monitor. $S \times A \times S \to \{0, 1\}$

Когда ММ истинен, то СМ используется для урезания возможных действий до безопасных.

RL-model
Рассматриваем модель с конечным числом состояний и детерминированной функцией перехода, то есть каждой паре "состояние-действие" однозначно ставится в соответствие следующее состояние и награда.

Формула $\models init|\{ctrl; plant\}|safe$ означает, что если начать в стстоянии $init$ и проделать $\{ctrl; plant\}$ сколько угодно раз, то придем в безопасное состояние.

Что такое plant?

Инпут для алгоритма JSC
1. модель RL (S, A, R, E)
2. стратегия choose для выбора действий
3. функция update, записывающая переходы между состояниями
4. предикат done для определения. какие состояния являются терминальными
5. controller monitor
6. model monitor

Логика $\text{\textsf{d{\kern-0.05em}L}}$
Что же такое дифференциальная динамическая логика?
[[Синтаксис дифференциальной динамической логики]]

Применяем, чтобы поезда ездили, самолеты летали, роботы-хирурги все делали правильно.

- дифференциальные инварианты
- дифференциальные варианты


[[интервью с Плацером]]






