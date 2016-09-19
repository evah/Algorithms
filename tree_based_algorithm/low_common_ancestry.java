
//CHECK EBOOK, not complete yet, 是递归结法

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

class Finder{
    Node findFromRoot(Node a, Node b, Node root){

        //ENDINg case
        if(root == null || root == a || root ==b ) return root;


        Node left = findFromRoot(a,b, root.left)
        Node right = findFromRoot(a,b, root.right)

        if(left!=null&&right!=null) return root;

        if(left!=null) return left;
        return right;

    }
}


public class Solution {
    public static void main(String() args) throws FileNotFoundException{
        Scanner in = new Scanner(new File("input.txt"));

        int n = in.nextInt();

        while(n! = -1){
            Node[] tree = new Node[n];

            for (int i=0; i<n; ++i) tree[i]=new Node[i];

            for (int i=0; i<n; ++i){

            }




        }
    }}

//Step 1 traversal


//Step 2 find the common parent:  如果一个节点左边找到一个，右边找到一个，就是么？不对。
//忽略了一个重要情况，当一个节点已经是另一个节点的父亲节点，就是本身
