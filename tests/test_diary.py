from lib.diary import Diary

'''

given no entries (on initialization)
ensure diary entry list is empty

'''

def test_init_list_is_empty():
    diary = Diary()
    assert diary.all() == []

'''

following tests check todo list functionality given 1 task

'''

def test_add_one_task_to_todo_list():
    diary = Diary()
    diary.add_task("Go shopping")
    assert diary.tasks_outstanding() == ["Go shopping"]

'''

check removal of item if 1 on list

'''

def test_remove_only_item_from_todo_list():
    diary = Diary()
    diary.add_task("Go shopping")
    diary.complete_task("Go shopping")
    assert diary.tasks_outstanding() == "All tasks completed!"

'''

check removal of a task that doesnt exist

'''

def test_remove_an_item_from_todo_list_that_isnt_there():
    diary = Diary()
    diary.add_task("Go shopping")
    assert diary.complete_task("Make bank on crypto") == "Task not found, run the tasks_outstanding method to check what tasks remain!"


    
