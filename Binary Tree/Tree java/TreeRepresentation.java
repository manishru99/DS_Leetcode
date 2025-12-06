// Tree representation in java

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class TreeNode {
    int data;
    List<TreeNode> children;

    TreeNode(int data) {
        this.data = data;
        this.children = new ArrayList<>();
    }

    void addChild(TreeNode child) {
        this.children.add(child);
    }

    void removeChild(TreeNode child) {
        this.children.remove(child);
    }

    void printTree() {
        System.out.println(this.data + " -> " + children.stream().map(c -> String.valueOf(c.data)).reduce((a, b) -> a + " " + b).orElse(""));
        for (TreeNode child : children) {
            child.printTree();
        }
    }

    static TreeNode findNode(TreeNode root, int data) {
        if (root == null) return null;
        if (root.data == data) return root;
        for (TreeNode child : root.children) {
            TreeNode result = findNode(child, data);
            if (result != null) return result;
        }
        return null;
    }
}

public class TreeRepresentation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the root node value: ");
        int rootValue = scanner.nextInt();
        TreeNode root = new TreeNode(rootValue);

        System.out.print("Enter the number of nodes (excluding root): ");
        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter the child node value: ");
            int childData = scanner.nextInt();
            System.out.print("Enter the parent of node " + childData + ": ");
            int parentData = scanner.nextInt();
            
            TreeNode parent = TreeNode.findNode(root, parentData);
            if (parent != null) {
                TreeNode child = new TreeNode(childData);
                parent.addChild(child);
            } else {
                System.out.println("Parent not found!");
            }
        }

        System.out.println("Tree Structure:");
        root.printTree();
        scanner.close();
    }
}