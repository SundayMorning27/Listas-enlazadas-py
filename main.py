class Node:
    def __init__(self, data):
        self.data = data  # Representa el valor que almacenará el nodo
        self.next = None  # Representa el puntero al siguiente nodo


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)  # Se crea un nuevo nodo con el dato proporcionado

        if not self.head:  # Verifica si la lista está vacía
            self.head = new_node  # Si está vacía, entonces el nuevo nodo se convierte en el head
            return

        # Si la lista no está vacía, entonces busca el último nodo y agrega uno nuevo al final
        last = self.head
        while last.next:
            last = last.next  # Nos movemos hasta el último nodo de la lista
        last.next = new_node  # Enlazamos el último nodo con el nuevo nodo en la lista

    # Muestra los nodos en pantalla seguidos de su puntero
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Imprime un nodo y al final agrega el símbolo de ->
            current = current.next
        print("None")  # Cuando no hayan más nodos, imprime None


# Instancia de la clase LinkedList
my_list = LinkedList()

# Agrega elementos a la linked list a través de este bucle
for e in range(5):
    #  Solicita al usuario un nombre<String>
    data_user = input("Ingresa un nombre: ")
    my_list.append(data_user)  # Agrega el dato del usuario a un nodo de la lista enlazada


# Muestra una Leyenda con el nombre de:
print("Linked List:")
my_list.display()  # Imprime en consola los nodos a través de la función display()
