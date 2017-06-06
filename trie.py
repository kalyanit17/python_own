import sys

class TrieNode(object):
 
 def __init__(self):
  self.children = {}
  isLeaf = 0

 def add_string(self,input_string):
  temp = self
  for ch in input_string:
   if ch not in temp.children:
    node = TrieNode()
    temp.children[ch] = node
   temp = temp.children[ch]
  temp.isLeaf = 1

 def print_strings(self,prefix=''):
  global allstrings

  if not self.children:
   allstrings.append(prefix)

  for ch in self.children:
   self.children[ch].print_strings(prefix+ch)

 def search_prefix(self,prefix_string):
  temp = self
  for ch in prefix_string:
   if ch in temp.children:
    temp = temp.children[ch]
   else:
    sys.exit("prefix string \"{0}\" is not found in trie".format(prefix_string))
  temp.print_strings(prefix_string)

 def allpaths(self,start_str=''):

  if not self.children:
   print "{0}\n".format(start_str)
   return

  for ch in self.children:
   self.children[ch].allpaths(start_str+ch)

 def search_string(self,search_string):
  temp = self
  for ch in search_string:
   if ch not in temp.children:
    print ("search string \"{0}\" not found in trie".format(search_string))
    return 0
   temp = temp.children[ch]
  print "Search string \"{0}\" found in trie".format(search_string)
  return 1  

if __name__ == "__main__":   
 allstrings = []
 head = TrieNode()
 head.add_string("kalyan")
 head.add_string("kiran")
 head.add_string("kishore")
 head.add_string("welcome")
 head.search_prefix("kal")
 head.allpaths()
 print "all strings are :: {0}".format(allstrings)
 head.search_string("kirani")
