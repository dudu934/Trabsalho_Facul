import tkinter as tk
from tkinter import messagebox

class ClothingStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clothing Store")

        # List of clothes
        self.clothes = [
            {'name': 'Camisa Branca', 'brand': 'Nike', 'size': 'P', 'price': 200},
            {'name': 'Calça Jeans', 'brand': 'Adidas', 'size': 'M', 'price': 150},
            {'name': 'Jaqueta Preta', 'brand': 'Puma', 'size': 'G', 'price': 300},
            {'name': 'Camiseta Verde', 'brand': 'Reebok', 'size': 'M', 'price': 100}
        ]
        
        # Selected items list
        self.selected_items = []

        # Frame for items
        self.items_frame = tk.Frame(self.root)
        self.items_frame.pack(pady=10)

        # Total label
        self.total_label = tk.Label(self.root, text="Total: 0 R$")
        self.total_label.pack()

        # Add checkboxes for each clothing item
        self.checkbuttons = []
        for item in self.clothes:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.items_frame, text=f"{item['name']}, {item['brand']}, - {item['size']} - {item['price']} R$", variable=var)
            checkbox.item = item
            checkbox.var = var
            checkbox.pack(anchor="w")
            self.checkbuttons.append(checkbox)

        # Add to cart button
        self.add_to_cart_button = tk.Button(self.root, text="Adicionar ao Carrinho", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=5)

        # Finalize purchase button
        self.finalize_button = tk.Button(self.root, text="Finalizar Compra", command=self.finalize_purchase)
        self.finalize_button.pack(pady=5)

        # Remove from cart button
        self.remove_from_cart_button = tk.Button(self.root, text="Remover do Carrinho", command=self.remove_from_cart)
        self.remove_from_cart_button.pack(pady=5)

    def add_to_cart(self):
        self.selected_items.clear()
        for checkbox in self.checkbuttons:
            if checkbox.var.get():
                self.selected_items.append(checkbox.item)
        
        total = sum(item['price'] for item in self.selected_items)
        self.total_label.config(text=f'Total: {total} R$')

    def remove_from_cart(self):
        # Show a list of selected items to remove
        if not self.selected_items:
            messagebox.showinfo("Carrinho Vazio", "Não há itens no carrinho para remover.")
            return
        
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remover Itens")

        tk.Label(remove_window, text="Selecione um item para remover:").pack(pady=10)

        # Add a list of selected items to remove
        for item in self.selected_items:
            remove_button = tk.Button(remove_window, text=f"Remover {item['name']}", command=lambda i=item: self.remove_item(i, remove_window))
            remove_button.pack(pady=5)

    def remove_item(self, item, remove_window):
        self.selected_items.remove(item)
        self.update_total()
        remove_window.destroy()

    def update_total(self):
        total = sum(item['price'] for item in self.selected_items)
        self.total_label.config(text=f'Total: {total} R$')

    def finalize_purchase(self):
        total = sum(item['price'] for item in self.selected_items)
        messagebox.showinfo("Compra Finalizada", f"Total da compra: {total} R$")
        self.selected_items.clear()
        self.total_label.config(text="Total: 0 R$")

# Create the root window
root = tk.Tk()

# Create the app and pass the root window
app = ClothingStoreApp(root)

# Run the app
root.mainloop()

