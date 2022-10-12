package io.pivotal.sporing.todos.todolist;

import java.io.File;

import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Simon Maple
 */
@Data
@NoArgsConstructor
public class TodoListImportRequest {

    private File zippedTodoLists;

    public TodoListImportRequest(File zippedTodoLists) {
        this.zippedTodoLists = zippedTodoLists;
    }
}
