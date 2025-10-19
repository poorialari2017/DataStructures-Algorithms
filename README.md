# ساختمان داده‌ها و الگوریتم‌ها (Data Structures & Algorithms)

این ریپوزیتوری جهت ارائه‌ی فایل‌ها و تمرینات کلاس **ساختمان داده‌ها و الگوریتم‌ها** به‌صورت عملی ایجاد شده است.  
هدف از این پروژه، یادگیری عمیق مفاهیم ساختار داده‌ها، تحلیل الگوریتم‌ها و پیاده‌سازی عملی آن‌ها در قالب پروژه‌های کاربردی است.

---

## سرفصل‌ها و مباحث پوشش داده شده

در این ریپوزیتوری، مباحث زیر به‌صورت تئوری و عملی بررسی شده‌اند:

### مفاهیم پایه
- **تحلیل پیچیدگی زمانی** - تحلیل الگوریتم‌ها و بررسی کارایی بر اساس زمان و حافظه مصرفی
- **نمادهای مجانبی** - Big O، Ω و Θ
- **مرور مفاهیم برنامه‌نویسی شیءگرا**

### ساختارهای داده پایه
- **آرایه‌ها و لیست‌ها** - پیاده‌سازی و کاربردها
- **لیست‌های پیوندی** - یک‌طرفه، دوطرفه و دایره‌ای
- **پشته و صف** - ساختارهای LIFO و FIFO و کاربردهای آن‌ها

### درخت‌ها
- **درخت‌های دودویی و درخت‌های جستجوی دودویی (BST)**
- **پیمایش درخت** - پیش‌ترتیب، میان‌ترتیب، پس‌ترتیب و سطح‌به‌سطح
- **درخت‌های متوازن** - AVL و درخت‌های قرمز-سیاه

### هیپ و درهم‌سازی
- **هیپ** - Min-Heap، Max-Heap و الگوریتم Heap Sort
- **توابع درهم‌سازی** - روش‌های حل برخورد و جدول درهم‌سازی

### گراف‌ها
- **مفاهیم پایه گراف** - روش‌های نمایش ماتریس مجاورت و لیست مجاورت
- **الگوریتم‌های پیمایش** - BFS و DFS
- **الگوریتم‌های مهم گراف** - دایجسترا، بلمن-فورد، کروسکال، پریم و مرتب‌سازی توپولوژیکی

### الگوریتم‌های مرتب‌سازی
- **مرتب‌سازی پایه** - حبابی، انتخابی، درجی
- **مرتب‌سازی پیشرفته** - ادغامی، سریع، پایه‌ای

### پارادایم‌های طراحی الگوریتم
- **تقسیم و حل** - تحلیل روابط بازگشتی
- **برنامه‌نویسی پویا** - زیرمسئله‌های همپوشان و ساختار بهینه
- **الگوریتم‌های حریصانه** - انتخاب حریصانه و مالکیت انتخاب بهینه

### الگوریتم‌های پیشرفته
- **الگوریتم‌های رشته‌ای** - تطبیق الگو با روش‌های Naive، KMP و رابین-کارپ
- **مسائل NP-Complete** - کلاس‌های پیچیدگی و مسائل کلاسیک
- **مباحث پیشرفته** - پوشش محدب، الگوریتم‌های تصادفی و چندنخی

### الگوریتم‌های هوش مصنوعی
- **الگوریتم‌های جستجو** - جستجوی آگاهانه و ناآگاهانه
- **بازی‌ها** - الگوریتم Minimax و هرس آلفا-بتا
- **یادگیری ماشین** - درخت تصمیم، KNN، بیز ساده و خوشه‌بندی k-Means
- **الگوریتم‌های احتمالی** - استنتاج بیزی و حذف متغیر

### سیستم‌های خبره
- **الگوریتم‌های استنتاج** - الگوریتم Rete
- **مدیریت عدم قطعیت** - شبکه‌های بیزی، نظریه دمپستر-شفر و منطق فازی
- **استدلال مبتنی بر مورد** - الگوریتم‌های بازیابی و انطباق مورد
- **الگوریتم‌های بهینه‌سازی** - الگوریتم ژنتیک و بهینه‌سازی ازدحام ذرات

---

## زبان‌های برنامه‌نویسی

تمامی تمرین‌ها و مثال‌ها با **Python** و **C++** پیاده‌سازی شده‌اند تا درک عمیق‌تری از ساختار داده‌ها و الگوریتم‌ها فراهم شود.

---

## ساختار پوشه‌ها
```
DATASTRUCTURES-ALGORITHMS/
├── 00 Basic concepts/
│   ├── 00 Time Complexity/
│   ├── 01 Asymptotic Analysis/
│   ├── 02 Asymptotic symbols O (Big O), Ω (Omega), Θ (Theta)/
│   └── 03 A brief overview of OOP/
|
├── 01 Basic Data Structures/
│   ├── 00 Array/
│   ├── 01 Linked List/
│   ├── 02 Stack/
│   ├── 03 Queue/
│   └── 04 Lists/
|
├── 02 Trees/
│   ├── 00 Basic tree concepts/
│   ├── 01 Binary Tree/
│   ├── 02 Binary Search Tree - BST/
│   ├── 03 Tree Traversal/
│   │   ├── 00 Pre-order/
│   │   ├── 01 In-order/
│   │   ├── 02 Post-order/
│   │   └── 03 Level-order/
│   └── 04 Self-Balancing Trees/
│       ├── 00 AVL/
│       ├── 01 Red-Black Tree/
│       └── 02 N-ary Trees/
|
├── 03 Heap/
│   ├── 00 Min-Heap/
│   ├── 01 Max-Heap/
│   └── 02 Heap Sort/
|
├── 04 Hashing/
│   ├── 00 Hash Function/
│   └── 01 Collision Resolution/
│       ├── 00 Open Addressing/
│       ├── 01 Separate Chaining/
│       └── 02 Hash Table/
|
├── 05 Graphs/
│   ├── 00 Basic graph concepts/
│   ├── 01 Graph display methods/
│   │   ├── 00 Adjacency Matrix/
│   │   └── 01 Adjacency List/
│   ├── 02 Graph Traversal Algorithms/
│   │   ├── 00 Breadth-First Search - BFS/
│   │   └── 01 Depth-First Search - DFS/
│   └── 03 Important problems and algorithms on graphs/
│       ├── 00 Bellman-Ford/
│       ├── 01 Dijkstra/
│       ├── 02 Kruskal/
│       ├── 03 Minimum Spanning Tree - MST/
│       ├── 04 Prim/
│       └── 05 Topological Sort/
|
├── 06 Sorting Algorithms/
│   ├── 00 Bubble Sort/
│   ├── 01 Insertion Sort/
│   ├── 02 Selection Sort/
│   ├── 03 Merge Sort/
│   ├── 04 Quick Sort/
│   └── 05 Radix Sort/
|
├── 07 Divide and Conquer/
│   └── 00 Assen/
|
├── 08 Dynamic Programming/
│   ├── 00 Optimal Substructure/
│   ├── 01 Overlapping Subproblems/
│   ├── 02 Difference between division and solution/
│   ├── 03 Implementation methods/
│   │   ├── 00 Bottom-up/
│   │   └── 01 Top-down/
│   └── 04 Classic examples/
│       ├── 00 Fibonacci series/
│       ├── 01 Knapsack problem/
│       ├── 02 Matrix Chain Multiplication/
│       ├── 03 Longest Common Subsequence - LCS/
│       └── 04 Floyd-Warshall Algorithm/
|
├── 09 Greedy Algorithms/
│   ├── 00 The concept of greedy choice and ownership of optimal choice/
│   ├── 01 Difference from dynamic programming/
│   └── 02 Classic examples/
│       └── Huffman Coding/
|
├── 10 String Algorithms/
│   └── 00 Pattern Matching/
│       ├── 00 Naive/
│       ├── 01 Knuth Morris Pratt - KMP/
│       └── 02 Rabin-Karp/
|
├── 11 NP-Complete/
│   ├── 00 Concept of optimization and decision problems/
│   ├── 01 Complexity classes P, NP, NP-Hard, NP-Complete/
│   ├── 02 Reduction between issues/
│   ├── 03 Classic issues/
│   │   ├── 00 Travelling salesman problem - TSP/
│   │   ├── 01 Vertex Cover/
│   │   └── 02 Subset Sum/
│   └── 04 Ways to deal with difficult problems/
│       ├── 00 Approximation Algorithms/
│       └── 01 Heuristics/
|
├── 12 Other Advanced Topics/
│   ├── 00 Convex Hull/
│   ├── 01 Randomized Algorithms/
│   ├── 02 Multithreaded Algorithms/
│   └── 03 Streaming Algorithms/
|
├── 13 AI Algorithms/
│   ├── 00 Search Algorithms/
│   │   ├── 00 Uninformed Search/
│   │   │   ├── 00 Breadth-First Search - BFS/
│   │   │   ├── 01 Depth-First Search - DFS/
│   │   │   ├── 02 Depth-Limited Search - DLS/
│   │   │   ├── 03 Iterative Deepening Search - IDS/
│   │   │   └── 04 Uniform-Cost Search - UCS/
│   │   ├── 01 Informed Search/
│   │   │   ├── 00 Greedy Best-First Search - Greedy BFS/
│   │   │   ├── 01 A-STAR/
│   │   │   └── 02 Iterative Deepening A-STAR - IDA-STAR/
│   │   └── 02 Local Search/
│   │       ├── 00 Hill Climbing/
│   │       ├── 01 Simulated Annealing/
│   │       ├── 03 Genetic Algorithm/
│   │       └── 04 Beam Search/
|   |
│   ├── 01 Game Playing/
│   │   ├── 00 Minimax Algorithm/
│   │   └── 01 Alpha-Beta Pruning/
|   |
│   ├── 02 Reasoning Algorithms/
│   │   ├── 00 Forward Chaining/
│   │   ├── 01 Backward Chaining/
│   │   └── 02 Resolution Algorithm/
|   |
│   ├── 03 Machine Learning/
│   │   ├── 00 Decision Tree Learning/
│   │   ├── 01 K-Nearest Neighbors - KNN/
│   │   ├── 02 Naive Bayes Classifier/
│   │   └── 03 k-Means Clustering/
|   |
│   └── 04 Probabilistic Algorithms/
│       ├── 00 Bayesian Inference/
│       ├── 01 Variable Elimination/    
│       └── 02 Sampling Methods/
|
└── 14 Expert System Algorithms/
    ├── 00 Inference Algorithms/
    │   └── 00 Rete Algorithm/
    |
    ├── 01 Uncertainty Management/
    │   ├── 00 Certainty Factors/
    │   ├── 01 Bayesian Belief Networks/
    │   ├── 02 Dempster-Shafer Theory/
    │   └── 03 Fuzzy Logic Algorithms/
    |
    ├── 02 Case-Based Reasoning/
    │   ├── Case Adaptation Algorithms/
    │   ├── Case Retrieval Algorithms/
    │   └── CBR for KNN/
    |
    └── 03 Optimization algorithms/
        ├── 00 Genetic Algorithms/
        └── 01 Particle Swarm Optimization/
```

