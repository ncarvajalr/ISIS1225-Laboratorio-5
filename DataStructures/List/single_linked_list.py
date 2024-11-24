from DataStructures.List import list_node
def new_list():
    newlist = { 'first': None,
                'last': None,
                'size': 0 }
    return newlist

def add_first(lst,element):
    node=list_node.new_single_node(element)
    node['next']=lst['first']
    lst['first']=node
    if lst['size'] == 0:
        lst['last']=lst['first']
    lst['size']+=1
    return lst

def add_last(my_list,element):
    node=list_node.new_single_node(element)
    if my_list["size"]==0:
        my_list["first"]=node
        my_list['last']=node
        my_list['size']+=1
    else:
        my_list["last"]["next"]=node
        my_list["last"]=node
        my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"]!=0:
        return my_list["first"]["info"]
    else:
        return None

def last_element(my_list):
    if my_list["size"]!=0:
        return my_list["last"]["info"]
    else:
        return None
    
def is_empty(my_list):
    return my_list["size"]==0

def get_element(my_list,pos):
    counter = 1
    first=my_list["first"]
    if pos ==0:
        return first["info"]
    else:
        nodo=first["next"]
        while counter != pos:
            nodo = nodo["next"]
            counter +=1
    return nodo["info"]
    
def delete_element(my_list,pos):
    counter = 1
    first=my_list["first"]
    if pos ==1:
        my_list["first"]=first["next"]
        my_list["size"]-=1
    else:
        anterior=first["next"]
        nodo = anterior["next"]
        while counter != pos:
            nodo = nodo["next"]
            counter +=1
        if nodo==None:
            my_list["last"]=anterior
            my_list["size"]-=1
            anterior["next"]=None
        else:
            anterior["next"]=nodo["next"]
            my_list["size"]-=1
            
def remove_first(my_list):
    primero=my_list["first"]
    my_list["first"]=primero["next"]
    my_list["size"]-=1
    return primero

def remove_last(my_list):
    counter=1
    while counter != my_list["size"]-1:
        nodo= my_list["first"]["next"]
        counter+=1
    my_list["last"]=nodo
    my_list["size"]-=1
    return nodo
    
def insert_element(my_list,element,pos):
    nodo=list_node.new_single_node(element)
    if (my_list['size'] == 0):
        my_list['first'] = nodo
        my_list['last'] = nodo
    elif ((my_list['size'] > 0) and (pos == 1)):
            nodo['next'] = my_list['first']
            my_list['first'] = nodo

    else:
        cont = 1
        prev = my_list['first']
        current = my_list['first']
        while cont < pos:
            prev = current
            current = current['next']
            cont += 1
            nodo['next'] = current
            prev['next'] = nodo

    my_list['size'] += 1
    return my_list
        
def is_present(my_list, element, cmp_function):
    if my_list['size']>0:
        cent=False
        nodo=my_list["first"]
        for pos in range (1, my_list['size']+1):
            while cent== False and nodo is not None:
                if cmp_function(nodo["info"],element)==0:
                    cent=True
                    resul=nodo["info"]
                else:
                    nodo=nodo["next"]
        return pos
    else:
        return 0