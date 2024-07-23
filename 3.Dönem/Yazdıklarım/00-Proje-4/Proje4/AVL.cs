using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    public class AVL    //https://simpledevcode.wordpress.com/2014/09/16/avl-tree-in-c/
    {                   
        public class Node
        {
            public int data;
            public Node left;
            public Node right;
            public Node(int data)
            {
                this.data = data;
            }
        }
        public Node root;

        public AVL()
        {
        }
        public void Add(int data)
        {
            Node newItem = new Node(data);
            if (root == null)
            {
                root = newItem;
            }
            else
            {
                root = RecursiveInsert(root, newItem);
            }
        }

            private Node RecursiveInsert(Node current, Node n)
            {
                if (current == null)
                {
                    current = n;
                    return current;
                }
                else if (n.data < current.data)
                {
                    current.left = RecursiveInsert(current.left, n);
                    current = balance(current);
                }
                else if (n.data > current.data)
                {
                    current.right = RecursiveInsert(current.right, n);
                    current = balance(current);
                }
                return current;
            }
        

        private Node balance(Node current)
        {
            int b_factor = balance_factor(current);
            if (b_factor > 1)
            {
                if (balance_factor(current.left) > 0)
                {
                    current = RotateL(current);
                }
                else
                {
                    current = RotateLR(current);
                }
            }
            else if (b_factor < -1)
            {
                if (balance_factor(current.right) < 0)
                {
                    current = RotateR(current);
                }
                else
                {
                    current = RotateRL(current);
                }
            }
            return current;
        }
        private int max(int l, int r)
        {
            return l > r ? l : r;
        }

        private int getHeight(Node current)
        {
            int height = 0;
            if (current != null)
            {
                int l = getHeight(current.left);
                int r = getHeight(current.right);
                int m = max(l, r);
                height = m + 1;
            }
            return height;
        }

            private int balance_factor(Node current)
        {
            int l = getHeight(current.left);
            int r = getHeight(current.right);
            int b_factor = l - r;
            return b_factor;
        }
        private Node RotateR(Node parent)
        {
            Node pivot = parent.right;
            parent.right = pivot.left;
            pivot.left = parent;
            return pivot;
        }
        private Node RotateL(Node parent)
        {
            Node pivot = parent.left;
            parent.left = pivot.right;
            pivot.right = parent;
            return pivot;
        }
        private Node RotateLR(Node parent)
        {
            Node pivot = parent.left;
            parent.left = RotateR(pivot);
            return RotateL(parent);
        }
        private Node RotateRL(Node parent)
        {
            Node pivot = parent.right;
            parent.right = RotateL(pivot);
            return RotateR(parent);
        }

    }
}
