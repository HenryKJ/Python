class TextFrequency():
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = []
        self.getText()
    def getText(self):
        file = open(self.file_name, 'r')
        self.text = file.read()
        file.close()
    def letterFreq(self):
        t = self.text.replace('\n', ' ')
        freq = {}
        for i in t:
            freq[i] = freq.get(i,0)+1
        return freq
    def wordFreq(self):
        t = self.text.replace('\n', ' ')
        t = t.split(' ')
        freq = {}
        for i in t:
            freq[i] = freq.get(i,0)+1
        return freq
    def toLower(self):
        self.text = self.text.lower()
    
class HistogramPrinter(TextFrequency):
    def __init__(self,file_name):
        TextFrequency.__init__(self, file_name)
    def printLetterHist(self):
        freq = TextFrequency.letterFreq(self)
        for letter in freq:
            print(letter,freq[letter] * '*')
    def printWordHist(self):
        freq = TextFrequency.wordFreq(self)
        for word in freq:
            print(word,freq[word] * '*')
        
        
        
myHistogram = HistogramPrinter('lyrics.txt')
myHistogram.toLower()
myHistogram.printLetterHist()



#myTextFrequency = TextFrequency('lyrics.txt')
#letterFreq = myTextFrequency.letterFreq()
#for letter in letterFreq:
#    print(letter,letterFreq[letter])
    
#wordFreq = myTextFrequency.wordFreq()
#for word in wordFreq:
#    print(word, wordFreq[word])