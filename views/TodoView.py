from services.TodoService import TodoService
from utils.InputUtil import InputUtil

class TodoView:
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def show_todos(self):
        while True:
            self.todo_service.show_todos()

            print("\nMenu:")
            print("1. Tambah")
            print("2. Ubah")
            print("3. Cari")
            print("4. Urutkan")
            print("5. Hapus")
            print("x. Keluar")

            choice = InputUtil.input("Pilih")
            stop = False

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.update_todo()
            elif choice == "3":
                self.search_todo()
            elif choice == "4":
                self.sort_todo()
            elif choice == "5":
                self.remove_todo()
            elif choice.lower() == "x":
                stop = True
            else:
                print("[!] Pilihan tidak dimengerti.")

            if stop:
                break

            print()

    def add_todo(self):
        print("[Menambah Todo]")
        title = InputUtil.input("Judul (x Jika Batal)")
        if title.lower() != "x":
            self.todo_service.add_todo(title)

    def remove_todo(self):
        print("[Menghapus Todo]")
        str_id = InputUtil.input("[ID Todo] yang dihapus (x Jika Batal)")
        if str_id.lower() != "x":
            try:
                todo_id = int(str_id)
                self.todo_service.remove_todo(todo_id)
            except ValueError:
                print("[!] ID harus berupa angka.")

    def update_todo(self):
        print("[Mengubah Todo]")
        # TODO: implement update functionality
        pass

    def search_todo(self):
        print("[Mencari Todo]")
        # TODO: implement search functionality
        pass

    def sort_todo(self):
        print("[Mengurutkan Todo]")
        # TODO: implement sort functionality
        pass

    def search_todo(self):
            print("[Mencari Todo]")
            keyword = InputUtil.input("Kata kunci (x jika batal)")

            if keyword.lower() == "x":
                return

            self.todo_service.search_todo(keyword)

    def sort_todo(self):
            print("[Mengurutkan Todo]")
            print("1. Berdasarkan Judul")
            print("2. Berdasarkan Status")
            print("3. Berdasarkan Abjad (A-Z)")

            choice = InputUtil.input("Pilih")

            if choice == "1":
                self.todo_service.sort_todo("title")
            elif choice == "2":
                self.todo_service.sort_todo("status")
            elif choice == "3":
                self.todo_service.sort_todo("alphabet")
            else:
                print("Pilihan tidak valid.")

    def update_todo(self):
            while True:
                print("[Ubah Todo]")
                print("1. Ubah satu Todo")
                print("2. Ubah semua Todo menjadi Selesai")
                print("x. Batal")

                choice = InputUtil.input("Pilih")

                if choice == "1":
                    self.update_single_todo()
                elif choice == "2":
                    self.complete_all_todos()
                elif choice.lower() == "x":
                    return
                else:
                    print("Pilihan tidak valid.")

    def complete_all_todos(self):
        confirm = InputUtil.input("Yakin ubah semua todo menjadi selesai? (y/n)")
        if confirm.lower() != "y":
            print("Dibatalkan.")
            return

        self.todo_service.complete_all_todos()

    def update_single_todo(self):
        print("[Ubah Satu Todo]")

        str_id = InputUtil.input("ID Todo (x jika batal)")
        if str_id.lower() == "x":
            return

        try:
            todo_id = int(str_id)
        except ValueError:
            print("ID harus berupa angka.")
            return

        new_title = InputUtil.input("Judul baru (kosong = tidak diubah)")
        if new_title.strip() == "":
            new_title = None

        status = InputUtil.input("Status (1=Selesai, 0=Belum, kosong=skip)")
        if status == "":
            new_status = None
        elif status == "1":
            new_status = True
        elif status == "0":
            new_status = False
        else:
            print("Status tidak valid.")
            return

        self.todo_service.update_todo(todo_id, new_title, new_status)

