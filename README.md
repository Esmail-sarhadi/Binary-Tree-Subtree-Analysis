
# Binary Tree Subtree Analysis

## Overview
This repository contains a Python implementation for constructing a binary tree from a given input, analyzing the maximum subtree sum, and finding the path to the node with the maximum subtree sum. The implementation uses a divide-and-conquer approach to solve the problem efficiently.

## Features
- **Tree Construction**: Build a binary tree from a list of values, with `'*'` representing the root, `'+'` for internal nodes, and numerical values for leaf nodes.
- **Subtree Analysis**: Calculate the maximum sum of any subtree and identify the node contributing to this maximum sum.
- **Path Finding**: Trace the path from the node with the maximum subtree sum to the root of the tree.

## Code Explanation
- **Node Class**: Represents a node in the binary tree with attributes for value, parent, left child, and right child.
- **create_tree Function**: Constructs the binary tree from a list of values. The tree is built in reverse order to ensure correct placement of nodes.
- **divide_and_conquer Function**: Recursively calculates the maximum sum of subtrees and identifies the node with the maximum subtree sum.
- **find_path_of_max_subtree Function**: Traces the path from the node with the maximum subtree sum to the root, returning the path as a string.
- **print_tree Function**: Prints the structure of the tree for debugging and verification purposes.

## Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/binary-tree-subtree-analysis.git
   cd binary-tree-subtree-analysis
   ```

2. **Prepare Input File:**
   Create an `input.txt` file in the repository directory. The file should contain a space-separated list of values where `'*'` denotes the root, `'+'` denotes internal nodes, and other values denote leaf nodes.

3. **Run the Script:**
   ```bash
   python main.py
   ```

4. **View Results:**
   The script will output the maximum subtree sum and the path to the node with the maximum subtree sum.

## Example
**Input File (`input.txt`):**
```
* + 1 2 + 3 + 4 5
```

**Output:**
```
Max Value =  12
Max Node Path:  01* 
```

## Contribution
Feel free to open issues, submit pull requests, or suggest improvements. Your contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact [sarhadiesmail@gmail.com](mailto:sarhadiesmail@gmail.com).

<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a>
