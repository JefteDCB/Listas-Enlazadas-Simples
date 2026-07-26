class Node:
    def __init__(self, valor): #el init es para crear la clase nodo
        self.valor = valor #lo que hacemos que es que el valor actual
        self.next = None #Y el siguiente valor es igual a Nulo, xke no hay nada


    #Hacer la clae lista:


class SinglyLinkedList:
    def __init__(self):
        self.head = None #la cabeza está viendo a Nulo

    def insert(self, valor): #El caso de insertar cuando no hay nada en la lista
        new_node = Node(valor)
    
        new_node.next = self.head #nos permite recorrer la lista
        self.head = new_node

    def insert_posicion(self, valor, posicion):
        new_node = Node(valor)
        if (self.head is None):
            self.head = new_node
            return 
        current = self.head
        cantidad = 0
        while(current and cantidad != posicion - 1):
            current = current.next
            cantidad += 1
        if cantidad == posicion:
            new_node.next = current.next
            current.next = new_node


    def display(self): #se asemeja al recorrido de un toString
        current = self.head
        while(current):
            print(current.valor, end=" -> ")
            current = current.next #Lo que permite es navegar entre los nodos de la lista
        print("None")

lista1=SinglyLinkedList() # Se crea un objeto de la clase SinglyLinkerList
lista1.insert(10)
lista1.insert(20)
lista1.insert(30)
lista1.insert(40)
lista1.insert(50)
lista1.insert(60)
lista1.insert(5)
lista1.insert_posicion(100, 3)

lista1.display()
