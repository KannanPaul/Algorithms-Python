```
Relationship between Array Indexes and Tree Elements

How to "heapify" a tree
- Starting from a complete binary tree, we can modify it to become a Max-Heap by running a function called heapify on all the non-leaf elements of the heap.
- To maintain the max-heap property for the entire tree, we will have to keep pushing 2 downwards until it reaches its correct position.
- To maintain the max-heap property in a tree where both sub-trees are max-heaps, we need to run heapify on the root element repeatedly until it is larger than its children or it becomes a leaf node.

Build max-heap
- In the case of a complete tree, the first index of a non-leaf node is given by n/2 - 1. All other nodes after that are leaf-nodes and thus don't need to be heapified.

Working of Heap Sort
- Since the tree satisfies Max-Heap property, then the largest item is stored at the root node.
- Swap: Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place.
- Remove: Reduce the size of the heap by 1.
- Heapify: Heapify the root element again so that we have the highest element at root.
- The process is repeated until all the items of the list are sorted

Reference
- https://www.programiz.com/dsa/heap-sort
- https://www.geeksforgeeks.org/heap-sort/?ref=shm
```
