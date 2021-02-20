doi: 10.1093/nar/gkz167

3С-методы фокусируются на локальных локусах
ChIA-PET получает только взаимодейвтсия, относящиеся к заданным протеинам
Hi-C требуется чрезвычайно глубокое секвенирование

Предсказание хроматиновых контактов на уровне индивидуальных регуляторных элементов используя последовательность ДНК и информацию от открытости хроматина.

**Какая задача**
Предсказывать генные взаимодействия (промотор-промотор, промотор-энхенсер)
**Как решали**
С помощью глубокого обучения
The model is a deep neural net-work consisting of three modules: 
(i) a sequence module forextracting sequence features with two convolutional neu-ral networks (CNNs), 
(ii) an openness module for learn-ing epigenomic features from chromatin 7accessibility scoreswith another two CNNs and 
(iii) an integration module formerging features of these two modules and gaining higherlevel context features with an attention-based recurrent neu-ral network.

**Что подается на вход, что получается на выходе**
input for our predictive model is the sequences oftwo regulatory elements represented with a one-hot encod-ing strategy (Figure1A), and their chromatin accessibilitys cores derived from DNase-seq experiments of a given celltype (можно было бы еще использовать ATAC-seq вместо DNase-seq)

Based on this input, our model will com-pute the predictive score of whether the two regulatory el-ements have 3D contact
 
**Бутстреппинг**
Еще для избегания нестабильности сети, вызванной начальными случайными инициализации, авторы применяют бутстреппинг. А именно, из изначальных данных с помощью выбора с возвращениями строится 20 датасетов, каждый из которых некоторым образом аугментируется, и на каждом из которых затем обучается отдельная модель. Затем, для вынесения окончательного решения берется среднее арифметическое результатов каждой модели.

**гитхаб**
https://github.com/liwenran/DeepTACT

**Что осталось непонято**
- что такое promotor-promotor and promotor-enhancer interations
- что такое глубина секвенирования
- что такое DNase-seq, ATAC-seq, ChIA-PET