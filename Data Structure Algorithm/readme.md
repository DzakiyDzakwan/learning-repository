# Data Structure Algorithm
DSA stands for Data Structures and Algorithms. They are two separate, but closely related, concepts fundamental to computer science:

1. Data Structure (DS)
specific way of organizing, managing, and storing data in a computer so that it can be accessed and modified efficiently. Think of it as a specific filing cabinet designed for a particular kind of task.
Examples : Arrays, Hash Maps (Dictionary), Stacks, Queques, LinkedList, Trees

2. Algorithms
a step-by-step procedure or a set of rules used to solve a specific problem or perform a computation. Think of it as a recipe for processing the data in your structure.
Examples: Sorting algorithms (Merge Sort, Quick Sort), Searching algorithms (Binary Search), and Graph algorithms (BFS, DFS).


When you write code, you want it to be fast and consume minimal resources (like memory). A slow or inefficient solution might work for a small set of data (e.g., sorting 10 numbers), but it will completely fail when dealing with real-world data (e.g., sorting 10 million customer records).
By learning DSA, you gain the skills to:

- Write Optimal Code: You learn to measure the performance of your code using Big O Notation (Time and Space Complexity) and choose the best data structure and algorithm combination to meet performance requirements.

- Solve Complex Problems: You gain a toolkit of established patterns and solutions for common problems like searching, sorting, pathfinding, and optimization. You won't have to reinvent the wheel every time.

- Think Logically: The process of breaking down a problem and figuring out the optimal way to solve it with DSA sharpens your logical reasoning and problem-solving skills, which are valuable in all aspects of engineering.

## Time Complexity
Time Complexity measures the number of elementary operations an algorithm performs, expressed as a function of the input size ($n$).

We use Big O Notation ($O$) to describe Time Complexity. Big O specifically represents the worst-case scenario or the upper bound of an algorithm's growth rate. This is the most pessimistic (and safest) way to analyze an algorithm's performance.

> $$T(n) = O(f(n))$$

Where :
- $T(n)$ is the time taken by the algorithm for an input size $n$.
- $f(n)$ is the function that defines the growth rate.

To keep the analysis simple and focused on growth, we follow two main rules:
- Drop the Lower-Order Terms: As $n$ gets very large, lower-order terms become insignificant.
> $O(n^2 + n + 1)$ simplifies to $O(n^2)$

- Drop the Constant Coefficients: Constant factors don't affect the overall growth rate.
> $O(2n)$ simplifies to $O(n)$

these common complexity classes and what they mean for the algorithm's performance:

### 📈 Common Time Complexities (Big O Notation)

| Big O Notation | Name | Description | Example (Algorithm/Operation) | Growth Rate / Impact |
| :---: | :--- | :--- | :--- | :--- |
| **$O(1)$** | **Constant** | The runtime is constant and does not change with the input size $n$. | Accessing an element in an Array by index. Hash Map insertion/lookup. | **Excellent** (Instant) |
| **$O(\log n)$** | **Logarithmic** | The runtime grows very slowly. The problem size is halved in each step. | **Binary Search**. Finding a node in a balanced Binary Search Tree (BST). | **Great** (Very Fast) |
| **$O(n)$** | **Linear** | The runtime grows directly proportional to the input size $n$. | Iterating through an entire **Array** or **Linked List**. Linear Search. | **Good** (Scalable) |
| **$O(n \log n)$** | **Linearithmic** | The runtime grows slightly faster than linear. This is typically the best complexity for general-purpose sorting. | Efficient sorting algorithms like **Merge Sort** and **Quick Sort**. | **Fair** (Acceptable for large inputs) |
| **$O(n^2)$** | **Quadratic** | The runtime grows proportional to the square of the input size. Often involves nested loops. | Bubble Sort. Comparing every pair of elements in a single list. | **Poor** (Avoid for large inputs) |
| **$O(2^n)$** | **Exponential** | The runtime doubles with every single addition to the input size $n$. | Brute-force solutions to problems like the Traveling Salesman Problem. | **Terrible** (Only viable for tiny inputs) |

## Array
Array is a collection of items of the same data type stored in contiguous memory locations. Array are divided into two parts

1. Static Array
In many lower-level programming languages (like C, C++, or Java's native arrays), arrays are defined by their strict space management rules:
- Contiguous Block: When you declare an array of size 1$N$, the operating system or runtime environment allocates a single, continuous block of memory large enough to hold 2$N$ elements of that specific data type.
- Fixed Size: Once allocated, the array's size is fixed.4 If you need to store $N+1$ elements, you cannot simply expand the existing array. You must:
    1. Allocate a new, larger block of contiguous memory.
    2. Copy all existing $N$ elements from the old location to the new location.
    3. Deallocate the old memory block.
- Space Overhead: This fixed-size approach is space-efficient because there is no wasted space (the array is exactly the size it needs to be, once defined). However, the process of resizing is very time-inefficient (5$O(n)$) and can be viewed as a space management challenge, forcing the application to manage memory churn

2. Dynamic Array
Dynamic Array manages space to optimize for the common operation of appending elements:
- Oversizing: When you append an item to a Python list and it runs out of space, the list doesn't just allocate space for one more element. It typically allocates a larger block (e.g., $1.5 \times$ or $2 \times$ the current size).
- Amortized Efficiency: The goal of this strategy is to make most append operations 7$O(1)$, only incurring the slow 8$O(n)$ copy operation occasionally when the pre-allocated space runs out.9 When we average the cost of the fast $O(1)$ operations with the infrequent slow $O(n)$ operations, the cost per operation is said to be amortized $O(1)$.
- Space Waste: The trade-off is that Python lists often have unused "buffer" space at the end. This is a form of intentional space overhead used to achieve time efficiency. The space is managed dynamically, growing and sometimes shrinking behind the scenes.

The contiguous nature of arrays is key to their 11$O(1)$ access time, which relies on simple arithmetic for space management. The memory address of any element at index $i$ is calculated using this formula:
> $$\text{Address}(i) = \text{Base Address} + (i \times \text{Size of Element})$$

Where : 
- Base Address: The memory location of the first element (index 0).
- Size of Element: The fixed number of bytes required to store one element (e.g., 4 bytes for an integer).

Arrays are commonly used as a building block for:
- Storing Simple Lists of Data: Any ordered collection of homogeneous items (e.g., a list of student scores, a sequence of characters in a string, or pixel data in an image).
- Implementing Other Data Structures: Arrays are often the underlying structure used to implement:
    - Stacks and Queues
    - Hash Tables (for storing the actual data)
    - Heaps
- Lookup Tables: Because of their fast access time, they are perfect for use cases where you need to quickly retrieve data based on a position or index.

Arrays are not just theoretical; they underpin many core features in modern software:
- Image Processing: Images are often represented as 2D Arrays (or matrices) where each element holds the color value of a pixel. Manipulating these arrays allows for image filters, cropping, and resizing.
- Game Development: Game maps, especially for grid-based games (like Chess or Tetris), are typically managed using 2D Arrays to track the position and state of objects on the board.
- Database Management (Internally): While databases use complex structures, the raw data columns in memory or on disk are often managed using contiguous memory blocks, similar to arrays, for fast sequential access.
- Financial Data: Storing a time series of stock prices or daily sales figures is done efficiently using an array because the data is ordered, and you often need to access the $k$-th element quickly.

## Linked List
Linked List is a linear data structure, like an Array, but it does not store elements at contiguous memory locations. Instead, it is composed of a sequence of interconnected objects called Nodes.

While the Singly Linked List (only pointing forward) is the most basic, there is 3 type of linked list:
1. Single Linked List : Node only has pointer to next node. This list can only travel foward
2. Double Linked List : Each node has a pointer to both the next and the previous node. This allows for traversal in both directions.
3. Circular Linked List : First of node has previous pointer for the last node. And the last node has next pointer to first node

Linked Lists shine in scenarios where the size of the data structure changes frequently and performance in the middle of the list is crucial.
- Dynamic Data Management: They are highly efficient when the number of elements is unknown or constantly fluctuating.
- Implementing Advanced Structures: They are the backbone for implementing:
    - Stacks and Queues: They offer easy $O(1)$ time complexity for adding/removing from one or both ends.
    - Adjacency List in Graphs: Each vertex in a graph often uses a Linked List to store its neighbors.
- Memory Management: Operating systems sometimes use linked lists to manage free and allocated memory blocks.

Linked Lists power features that require fluid, ordered storage:
- Music/Video Playlists: A playlist is naturally a linked list. Songs are nodes, and the "next song" button simply follows the link to the next node. Insertion or deletion of a song takes $O(1)$ time (if you know the song before it).
- Browser History/Navigation: The "Back" and "Forward" buttons can be modeled by a Doubly Linked List. Going back means following the previous pointer, and going forward means following the next pointer.
- Undo Functionality: Editors and graphic design software can use a linked list to store the sequence of user actions. Undoing means moving back one node in the list.

## Hashmap
Hashmap is a data structure that implements an associative array abstract data type. It is used to store collections of key-value pairs. The core idea behind a HashMap is to use a special function, called a hash function, to compute an index, or hash, into an array of buckets or slots, from which the desired value can be retrieved.

How it Works:
- Key-Value Pair: Every item stored in a HashMap consists of a unique key and its associated value.
- Hash Function: When you want to insert a key-value pair, the key is passed through the hash function.
- Hash Code/Index: The hash function returns an integer, which is used as the index (or memory address) where the value is stored in the underlying array (the "buckets").
- Retrieval: To retrieve a value, the key is passed through the same hash function to immediately calculate the storage index, allowing for very fast lookups.

he core concept of a HashMap is implemented in various forms and programming languages. The key features it implements are that of an efficient associative data structure.
- Database Indexing
- Spell Checkers and Dictionaries
- Caching System
- Router and DNS resolution
- Symbol Table in Compiler