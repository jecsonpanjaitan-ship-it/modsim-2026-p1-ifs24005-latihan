from typing import List
from entities.Todo import Todo

class TodoRepository():
    def __init__(self):
        self.data: List[Todo] = []  # type: ignore

    def get_all_todos(self) -> List[Todo]: # type: ignore
        return self.data

    def add_todo(self, new_todo: Todo):
        self.data.append(new_todo)

    def remove_todo(self, id: int) -> bool:
        # cari todo berdasarkan id
        target_todo = next((todo for todo in self.data if todo.id == id), None)
        if target_todo is None:
            return False
        self.data.remove(target_todo)
        return True

    def search_todos(self, keyword: str):
            keyword = keyword.lower()
            return [
                todo for todo in self.data
                if keyword in todo.title.lower()
            ]

    def sort_todo(self, key: str):
        if key == "title":
            self.data.sort(key=lambda todo: todo.title.lower())
        elif key == "status":
            self.data.sort(key=lambda todo: todo.is_finished)
        elif key == "alphabet":
                self.data.sort(key=lambda todo: todo.title.lower())

    def update_todo(self, id: int, new_title=None, new_status=None) -> bool:
            for todo in self.data:
                if todo.id == id:
                    if new_title is not None:
                        todo.title = new_title
                    if new_status is not None:
                        todo.is_finished = new_status
                    return True
            return False

    def search_todos(self, keyword: str):
            keyword = keyword.lower()
            return [
                todo for todo in self.data
                if keyword in todo.title.lower()
            ]

    def mark_all_unfinished_as_finished(self) -> int:
            count = 0
            for todo in self.data:
                if not todo.is_finished:
                    todo.is_finished = True
                    count += 1
            return count

