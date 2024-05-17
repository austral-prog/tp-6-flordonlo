def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)>=6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements)>=5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements)>0 and list_to_remove_elements<=4:
        del list_to_remove_elements[0]
        return list_to_remove_elements
sample=['Red', 'Green', 'White', 'Black', 'pink','yellow']
print(remove_elements(sample))


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements
sample=['Red', 'Green', 'White', 'Black']
print(add_elements(sample))
    

def is_empty(list_to_check):
    if len(list_to_check)==0:
        return "La lista esta vacia"
    else:
        return "La lista no esta vacia"
lista=[]
print(is_empty(lista))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return 'True'
        else:
            return 'False'
    elif (len(list_to_compare1)>0 and len(list_to_compare1)<3) or (len(list_to_compare2)>0 and len(list_to_compare2)<3):
        return 'False'
    else:
        return 'False'
sample_list1=['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
sample_list2=['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
print(check_lists(sample_list1,sample_list2))


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify)>2:
        if len(list_of_lists_to_modify[0])>=1:
            p1=list_of_lists_to_modify[0][0:2]
        else:
            p1=[]
        if len(list_of_lists_to_modify[1])>=2:
            p2=list_of_lists_to_modify[1][1:4]
        else:
            p2=[]
        if len(list_of_lists_to_modify[2])>=1:
            p3=list_of_lists_to_modify[2][-2:]
        else:
            p3=[]
    return [p1,p2,p3]
sample=[[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(sample))
