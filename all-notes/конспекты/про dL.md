Статья про относительно полный доказательный анализ (proof calculus) для формул из dL. Он основан на равномерной подстановке. Эта подстановка позволяет использовать аксиомы вместо схем акмиом, что упрощает имплементацию. Также в статье представлены дифференциальные формы.

Пробовали секвентный анализ и гильбертоподобную аксиоматизацию, остновились на первой. Это очень негибко и сложновато.

Аксиомы реализованы на объектном языке, а не на мета-языке.	

Дифференциальная динамическая логика с дифференциальными формами.

Смысл равномерной подстановки - упростить реализацию.


- The KeYmaera X theorem prover for hybrid systems implements the dL calculus [45].
- There is an extension called quantified differential dynamic logic (QdL) [19], with which distributed hybrid systems can be verified. This is the first formal verification approach for (dynamic/reconfigurable) distributed hybrid systems, in which participants may appear and disappear during the system evolution. QdL is implemented in KeYmaera.
- The extension differential game logic (dGL) provides specification and verification for hybrid games [43,46].
- There is an extension called stochastic differential dynamic logic (SdL) [22], with which stochastic hybrid systems can be verified.
Publications related to dL
- There is an extension called differential-algebraic dynamic logic (DAL) for more general differential-algebraic programs [8]
- ODE verification technology for differential dynamic logic is based on differential invariants [8,10,13,50,53], which are formulas that remain true along the dynamics of the hybrid system and its differential equations.
- There is a temporal extension called differential temporal dynamic logic (dTL) [4]. Also see further details and extensions in a book [18].

Differential dynamic logic itself has been originally introduced in 