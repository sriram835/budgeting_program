class Sort():
    def __init__(self,dictionary):
        self.dictionary=dictionary

    def Ascend_Sorting(self,column):
        l=list(self.dictionary.keys())
        l.remove(column)
        for i in range(len(self.dictionary[column])-1):
            for j in range(0,len(self.dictionary[column])-i-1):
                if self.dictionary[column][j]>self.dictionary[column][j+1]:
                    self.dictionary[column][j],self.dictionary[column][j+1]=self.dictionary[column][j+1],self.dictionary[column][j]
                    for keys in l:
                        self.dictionary[keys][j],self.dictionary[keys][j+1]=self.dictionary[keys][j+1],self.dictionary[keys][j]

    def Descend_Sorting(self,column):
        l=list(self.dictionary.keys())
        l.remove(column)
        for i in range(len(self.dictionary[column])-1,0,-1):
            max_index=i
            for j in range(max_index,-1,-1):
                if self.dictionary[column][max_index]>self.dictionary[column][j]:
                    max_index=j
            self.dictionary[column][i], self.dictionary[column][max_index] = self.dictionary[column][max_index], self.dictionary[column][i]
            for keys in l:
                self.dictionary[keys][i],self.dictionary[keys][max_index]=self.dictionary[keys][max_index],self.dictionary[keys][i]

#HOW TO MAKE IT WORK
#import sorting_dict
#<variable>=sorting_dict.Sort(<dictionary you want to sort>)
#<variable>.<function>(<column_name_to_be_sorted>)