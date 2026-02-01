from entities.Todo import Todo
from repositories.TodoRepository import TodoRepository

class TodoService():
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def show_todos(self):
        todos = self.todo_repository.get_all_todos()
        print("Daftar Todo:")
        if not todos:
            print("- Data todo belum tersedia!")
            return

        for counter, todo in enumerate(todos, start=1):
            print(todo)

    def add_todo(self, title: str):
        new_todo = Todo(title=title)
        self.todo_repository.add_todo(new_todo)

    def remove_todo(self, id: int):
        success = self.todo_repository.remove_todo(id)
        if not success:
            print(f"[!] Gagal menghapus todo dengan ID: {id}.")

    def search_todo(self, keyword: str):
            if not keyword.strip():
                print("Kata kunci tidak boleh kosong.")
                return

            results = self.todo_repository.search_todos(keyword)

            if not results:
                print("Todo tidak ditemukan.")
                return

            print("Hasil pencarian:")
            for todo in results:
                print(todo)

    def sort_todo(self, criteria: str):
            if criteria not in ["title", "status","alphabet"]:
                print("Kriteria pengurutan tidak valid.")
                return

            self.todo_repository.sort_todo(criteria)

    def update_todo(self, id: int, new_title=None, new_status=None) -> bool:
        if new_title is not None and not new_title.strip():
            print("Judul tidak boleh kosong.")
            return False

        success = self.todo_repository.update_todo(id, new_title, new_status)
        if not success:
            print(f"Todo dengan ID {id} tidak ditemukan.")
            return False

        return True

    def complete_all_todos(self) -> bool:
            updated_count = self.todo_repository.mark_all_unfinished_as_finished()
            if updated_count == 0:
                print("Tidak ada todo yang perlu diperbarui.")
                return False
            return True