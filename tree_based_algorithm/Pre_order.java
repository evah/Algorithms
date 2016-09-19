//先根遍历
//中根 in-order
//后根  post-order


import java.io.*;
import java.util.*;

class Node {
    int id;
    Node left;
    Node right;
    Node (int id) {
        this.id = id;
        left = null;
        right = null;
    }
}


//用递归非常方便
//if (root=null) return;


//比较难一点的结法，循环
//嵌套的循环，stack
//DFS--stack, BFS--queue
