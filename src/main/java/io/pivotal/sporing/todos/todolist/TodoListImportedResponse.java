package io.pivotal.sporing.todos.todolist;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Simon Maple
 */
@Data
@NoArgsConstructor
public class TodoListImportedResponse {    
    private List<TodoList> todoLists = new ArrayList<>();

    public TodoListImportedResponse(ArrayList<TodoList> todoLists) {
        this.todoLists = todoLists;
    }

    public static TodoListImportedResponse from(ArrayList<TodoList> todoLists) {
        return new TodoListImportedResponse(todoLists);
    }
}
