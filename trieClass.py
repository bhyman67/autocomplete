# modified trieClass.py code provided from the CU CS Moodle (CSCI 3104)!!!
# LastName: Hyman                   ===========
# FirstName: Brent                  === BCH ===
# Email: brent.hyman@colorado.edu   ===========
# Comments (by BCH): Trie Class that stores words, searches for words, and auto completes
#                    strings in a trie data structure 

from __future__ import print_function
import sys

class MyTrieNode:

    def __init__(self, isRootNode):                                                    #
        # Trie attributes (provided by the trieClass.py code)                          # provided by
        self.isRoot = isRootNode	                                               # the CU CS moodle 
        self.isWordEnd = False # is this node a word ending node                       # (CSCI 3104)
        self.count = 0 # frequency count                                               #
        self.next = {} # Dictionary mappng each character from a-z to the child node   #
        # -> I deleted the self.isRoot = False line (BCH)
		
    # ====== addWord() funct written/modified by BCH ======
    # -> just takes the word as an input and adds it to the trie
    def addWord(self,w):
        assert(len(w) > 0) # only line in addWord() funct from original triClass.py code!!!
        n = len(w)
        # for each character in word		
        for i in range(0,n):
            # if current character is in branch of current node
            if(w[i] in self.next):
                # travel across the character branch to corresponding node
                self = self.next[w[i]]
                # if current character is the last, denote end of word and  
                # add to the word count								
                if(i == n-1):
                    self.isWordEnd = True
                    self.count = self.count + 1
            # otherwise add a branch to the current node to represent current character
            else:
                # added branch mapping character to node
                self.next[w[i]] = MyTrieNode(False)
                # if current character is last in word
                if(i == n-1):
                    # the node that it maps to needs to indicate end of word
                    self.next[w[i]].isWordEnd = True
                    # it also needs to add to the word count
                    self.next[w[i]].count = self.next[w[i]].count + 1
                # not last character, so go to newly created corresponding node
                else:
                    self = self.next[w[i]]

    # ====== wordLookUp() and lookupWord functs written by BCH ======
    # -> wordLookUp() takes in a string. If the string is not in the trie (in other words
    #    isn't a word or a prefix in the trie) then it returns and empty node (None). 
    #    Otherwise, it will return the node after the last character of the string.
    # -> lookupWord() returns the frequency count of the given word in the tri
    def wordLookUp(self,w):
        # indicates the truth value of a character match
        noChar = False
        # create an empty node
        node = None
        n = len(w)
        i = 0        
        # until either end of given word or no match of current character with any branch 
        while(  (i != n) and (not noChar)  ):
            # if current character matches with a branch in current node
            if( w[i] in self.next):
                # travel accross the character branch to the corresponding node
                self = self.next[w[i]]
                i = i+1
                # if at end of word set the empty node equal to current node
                if(i == n):
                    node = self
            # word not there when current char doesn't match with a branch in the node
            else:
                noChar = True
        return node

    def lookupWord(self,w):
        trieNode = self.wordLookUp(w)
        if(trieNode and trieNode.isWordEnd):
            wordFreq = trieNode.count
        else:
            wordFreq = 0
        return wordFreq

    # ====== autoComplete() funct written by BCH. DFS_Visit is modified by BCH from CLRS textbook ======
    # -> The autoComlete funct Returns the set of autocompletions paired with the freq count for the given word/prefix. 
    #    In other words, it returns the set {(s,j)} s.t. word s, which occurs with frequency j, is an 
    #    autocompletion of the given string
    # -> the autoComplete funct relys on DFS_Visit to traverse the trie and find all completions of the 
    #    given prefix
    def DFS_Visit(self,node,tempW,set,w):
        for key in node.next:
            if(node.next[key].isWordEnd):
                set.append((tempW+key,node.next[key].count))
            set = self.DFS_Visit(node.next[key],tempW+key,set,w)
        return set
		
    def autoComplete(self,w):
        node = self.wordLookUp(w)
        if(node):		
            if(node.isWordEnd):
                set = [(w,node.count)]
            else:
                set = []
            AtoCmpltns = self.DFS_Visit(node,w,set,w)
        else:
            AtoCmpltns = []
        return AtoCmpltns    

# remaining code for testing the trie class was provided in original trieClass.py file provided
# by CU CS moodle (CSCI 3104)
if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']
    for w in lst1:
        t.addWord(w)
    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2	
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
