using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class TreeNode
    {
        public Durak data;
        public List<Musteri> musteriList; //Burasi derste tartisilmisti. Istenen sanirim tam bu degil ama boyle de kalirsa
        public TreeNode leftChild;        //sikinti olmayacagi soylendi.
        public TreeNode rightChild;
        
        public void displayNode()
        {
            int tandemBisikletSay = 0;
            int normalBisikletSay = 0;
            int toplamBisikletSay = 0;

            Console.WriteLine(data.durakAdi+" Duraginin Musteri Bilgisi\n---------------------------------");
            foreach(Musteri musteriYazdirilacak in musteriList)
            {
                Console.Write("#");
                musteriYazdirilacak.musteriYazdir();
                if (musteriYazdirilacak.kiraladigiBisikletTuru == "Tandem Bisiklet")
                    tandemBisikletSay += 1;
                else if (musteriYazdirilacak.kiraladigiBisikletTuru == "Normal Bisiklet")
                    normalBisikletSay += 1;

            }
            toplamBisikletSay = tandemBisikletSay + normalBisikletSay;
            Console.WriteLine("\n"+data.durakAdi+" Duragindaki Son Durum\n---------------------------");
            Console.WriteLine("Kiralanan Normal Bisiklet:: "+normalBisikletSay+ "\nKiralanan Tandem Bisiklet:: "+tandemBisikletSay);
            Console.Write("Kiralanan Toplam Bisiklet:: " + toplamBisikletSay);
            data.durakYazdir();

        }
         
               
    }
    class BinTree
    {
        private TreeNode root;
        public BinTree() { root = null; }
        public TreeNode getRoot()
        { return root; }

        public void preOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                localRoot.displayNode();
                preOrder(localRoot.leftChild);
                preOrder(localRoot.rightChild);
            }

        }

        public void inOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                inOrder(localRoot.leftChild);
                localRoot.displayNode();
                inOrder(localRoot.rightChild);
            }
        }

        public void postOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                postOrder(localRoot.leftChild);
                postOrder(localRoot.rightChild);
                localRoot.displayNode();
            }
        }
        public int getHeight(TreeNode root)
        {
            // #Agacin derinliginin 1 fazlasini bulur ve dondurur.
            if (root != null)
                return 1 + Math.Max(getHeight(root.leftChild), getHeight(root.rightChild));
            else
                return 0;
        }

        public void insert(Durak durakEklenecek,List<Musteri> musteriListesi)
        {
            TreeNode newNode = new TreeNode();
            newNode.data = durakEklenecek;
            newNode.musteriList = musteriListesi;

            if (root == null)
                root = newNode;
            else
            {
                TreeNode current = root;
                TreeNode parent;

                while (true)
                {
                    parent = current;
                    if (durakEklenecek.durakAdi.CompareTo(current.data.durakAdi) == -1)
                    {
                        current = current.leftChild;
                        if (current == null)
                        {
                            parent.leftChild = newNode;
                            return;
                        }
                    }
                    else
                    {
                        current = current.rightChild;
                        if (current == null)
                        {
                            parent.rightChild = newNode;
                            return;
                        }
                    }
                }
            }
        }



    }
}

    
