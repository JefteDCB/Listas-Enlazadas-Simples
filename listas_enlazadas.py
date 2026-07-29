from unittest import case


class Node:
    def __init__(self,valor): #inicializamos valores
        self.valor=valor #Damos el valor al nodo
        self.next = None #Damos el valor de siguiente a nulo

class SinglyLinkedList: 
    def __init__(self):
        self.head = None

    def esVacia(self):
        return self.head is None

    def insert(self, valor): 
        new_node = Node(valor)
        if(self.head is None):
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def insertInicio(self, valor):
        new_node = Node(valor)
        new_node.next=self.head
        self.head=new_node

    def insert_posicion(self, valor, posicion):
        new_node = Node(valor)
        if (self.head is None):
            self.head = new_node
            return
        current = self.head
        cantidad = 0
        while(current and cantidad != posicion -1 ):
            current = current.next
            cantidad += 1
        if cantidad == posicion -1:
            new_node.next = current.next
            current.next = new_node

    def insertMedio(self, valor):
        new_node = Node(valor)

        if self.head is None:
            self.head = new_node
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node.next = slow.next
        slow.next = new_node 
            
    def display(self):
        current = self.head
        while(current):
            print(current.valor, end=" -> ")
            current = current.next
        print("None")

    def eliminarEnPosicion(self, posicion):
    # Lista vacía
        if self.head is None:
            print("La lista está vacía.")
            return
    # Eliminar el primer nodo
        if posicion == 0:
            self.head = self.head.next
            return
        current = self.head
        contador = 0
    # Buscar el nodo anterior a la posición
        while current.next is not None and contador < posicion - 1:
            current = current.next
            contador += 1
    # Verificar si la posición existe
        if current.next is None:
            print("Posición fuera de rango.")
            return
    # Saltar el nodo que se desea eliminar
        current.next = current.next.next



    def eliminarInicio(self):
        if self.head is None:
            print("La lista está vacía")
            return
        self.head = self.head.next


    def eliminarFinal(self): 
        if(self.head is None): #Comprobamos que la lista no esté vacía
            print("La lista está vacía")
            return
        if(self.head.next is None): #Comprobamos si la lista tiene solo un nodo
            self.head = None
            return

        current = self.head #Asigna la variable a el valor inicial de la lista

        while(current.next.next is not None): #Comprobamos que el siguiente nodo no seá nulo
            current = current.next #actualizamo al siguiente nodo

        current.next = None #el siguiente le damos el valor de nada

    def buscarValor(self, valor):
        current = self.head

        while(current):
            if current.valor == valor:
                return True
            current = current.next
        return False

        

lista1=SinglyLinkedList()
lista1.insert(10)
lista1.insert(20)
lista1.insert(30)



#print("Inicio Fin de Lista:")

#lista1.display()    

#print("Inicio de la lista")

#lista1.insertInicio(5)

#lista1.display()

#print("Insertar al medio de la lista")

#lista1.insertMedio(25)

#lista1.display()

#print("Insertar Especifica")

#lista1.insert_posicion(15, 2)

#lista1.display()

#print("Eliminar Inicio")

#lista1.eliminarInicio()

#lista1.display()

#print("Eliminar Final")

#lista1.eliminarFinal()

#lista1.display()

#print("Eliminar en Posición")

#lista1.eliminarEnPosicion(2)
#lista1.display()


def Menu(): 
    menu = """
    1. Insertar al inicio
    2. Insertar al final
    3. Insertar en posición específica
    4. Insertar al medio
    5. Eliminar al inicio
    6. Eliminar al final
    7. Eliminar en posición específica
    8. Buscar valor
    9. Mostrar lista
    10. Verificar si la lista está vacía
    11. Salir
    """

    
    seguir = True
    while seguir:
        print(menu)
        opcion = int(input("Ingrese la opción deseada: "))
        match opcion:
                case 1:
                    opcion = int(input("Ingrese el valor a insertar al inicio: "))
                    lista1.insertInicio(opcion)
                case 2: 
                    opcion = int(input("Ingrese el valor a insertar al final:"))
                    lista1.insert(opcion)
                case 3: 
                        opcion = int(input("Ingrese el valor a insertar en la posición específica: "))
                        posicion = int(input("Ingrese la posición donde insertar: "))
                        lista1.insert_posicion(opcion, posicion)
                case 4:
                    opcion = int(input("Ingrese el valor a insertar al medio: "))
                    lista1.insertMedio(opcion)
                case 5:
                    lista1.eliminarInicio()    
                    print("Se ha eliminado el primer nodo de la lista.")
                case 6:
                    lista1.eliminarFinal()
                    print("Se ha eliminado el último nodo de la lista.")
                case 7:
                    posicion = int(input("Ingrese la posición del nodo a eliminar: "))
                    lista1.eliminarEnPosicion(posicion)
                case 8:
                    opcion = int(input("Ingrese el valor a buscar: "))
                    if lista1.buscarValor(opcion):
                        print("El valor se encuentra en la lista.")
                    else:
                        print("El valor no se encuentra en la lista.")
                case 9:    
                        lista1.display()

                case 10:
                    if(lista1.esVacia()):
                        print("La lista está vacía.")
                    else:
                        print("La lista no está vacía.")
                case 11:
                        print("Saliendo del programa.")
                        seguir = False
                case _:
                        print("Opción inválida. Por favor, ingrese un número del 1 al 11.")



Menu()
