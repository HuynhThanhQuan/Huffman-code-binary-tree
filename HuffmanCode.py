# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 03:06:38 2018

@author: ASUS
"""

if __name__ == '__main__':
    PATH = input('Please insert your path file: ')
    with open(PATH, 'r') as file:
        lines = []
        fre = dict()
        for line in file:
            line = line.rstrip()
            for letter in line:
                fre[letter] = fre.get(letter, 0) + 1
        bst = HuffmanCodeBST()
        queue = PriorityQueue()
        for k, v in fre.items():
            queue.enqueue(k, v)
        print('Frequence of words')
        queue.printAll()
        for i in range(queue.size()):
            k, v = queue.dequeue()
            bst.add(v, k)
        bin_dic = dict()
        len_dic = dict()
        print('Huffman encoded')
        bst.traverseTree(bst.root,'', bin_dic)
        for k, v in bin_dic.items():
            len_dic[k] = len(v)
        ABR = 0
        total_len = 0
        for k, v in fre.items():
            ABR += v*len_dic[k]
            total_len += v
        ABR = total_len*8/ABR
        print('The compression ratio is:', ABR)
        print('Binary tree structure in BFT view')
        for i in range(1, bst.findHeightOfTree(bst.root, 0)+1):
            print('Level',i-1)
            bst.printBFT(bst.root,i)
