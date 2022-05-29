# -*- coding:utf-8 -*-

import copy     # 注意对象的深拷贝和浅拷贝的使用！！！
from ast import literal_eval

class GameNode:
    '''博弈树结点数据结构
    成员变量：
    name - string 结点名字
    val - int  结点值
    children - list[GameNode] 子结点列表
    '''
    def __init__(self, name='', val=0):
        self.name = name        # char
        self.val = val          # int
        self.children = []      # list of nodes

class GameTree:
    '''博弈树结点数据结构
    成员变量：
    root - GameNode 博弈树根结点
    成员函数：
    buildTree - 创建博弈树
    '''
    def __init__(self):
        self.root = None                # GameNode 博弈树根结点

    def buildTree(self, data_list, root):
        '''递归法创建博弈树
        参数：
        data_list - list[] like this ['A', ['B', ('E', 3), ('F', 12)], ['C', ('H', 2)], ['D', ('K', 14)]]
        root - GameNode
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        for i in range(1,len(data_list)):
            if type(data_list[i]) == list:
                root.children.append(GameNode(data_list[i][0]))
                self.buildTree(data_list[i],root.children[i-1])
            else:
                root.children.append(GameNode(data_list[i][0],data_list[i][1]))
        #********** End **********#


class AlphaBeta:
    '''博弈树结点数据结构
    成员变量：
    game_tree - GameTree 博弈树
    成员函数：
    minmax_with_alphabeta - 带AlphaBeta剪枝的极大极小值算法，计算最优行动
    max_value - 计算最大值
    min_value - 计算最小值
    get_value - 返回结点的值
    isTerminal - 判断某结点是否为最终结点
    '''
    def __init__(self, game_tree):
        self.game_tree = game_tree      # GameTree 博弈树

    def minmax_with_alphabeta(self, node):
        '''带AlphaBeta剪枝的极大极小值算法，计算最优行动
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - GameNode 最优行动的结点
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        clf = self.max_value(node,-10000,10000)
        for child in node.children:
            if child.val == clf:
                return child;
        #********** End **********#


    def max_value(self, node, alpha, beta):
        '''计算最大值
        参数：
        node - GameNode 博弈树结点
        alpha - int 剪枝区间下限值
        beta - int 剪枝区间上限值
        返回值：
        clf - int 子结点中的最大的评估值
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        if self.isTerminal(node):
            return self.get_value(node)
        clf = -10000
        for child in node.children:
            clf = max(clf,self.min_value(child,alpha,beta))
            if clf >= beta:
                return clf
            alpha = max(alpha,clf)
        node.val = clf;
        return clf
        
        #********** End **********#


    def min_value(self, node, alpha, beta):
        '''计算最小值
        参数：
        node - GameNode 博弈树结点
        alpha - int 剪枝区间下限值
        beta - int 剪枝区间上限值
        返回值：
        clf - int 子结点中的最小的评估值
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        if self.isTerminal(node):
            return self.get_value(node)
        clf = 10000
        for child in node.children:
            clf = min(clf,self.max_value(child,alpha,beta))
            if clf <= alpha:
                return clf
            beta = min(clf,beta)
        node.val = clf;
        return clf;
        #********** End **********#


    def get_value(self, node):
        '''返回结点的值
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - int 结点的值，即 node.val
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        return node.val;
        #********** End **********#


    def isTerminal(self, node):
        '''判断某结点是否为最终结点（无子结点）
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - bool 是最终状态，返回True，否则返回False
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        if node.val == 0:
            return False
        else:
            return True
        #********** End **********#
        