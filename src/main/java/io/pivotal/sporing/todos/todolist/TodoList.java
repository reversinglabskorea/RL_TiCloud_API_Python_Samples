package io.pivotal.sporing.todos.todolist;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

import io.pivotal.sporing.todos.user.User;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Matt Stine
 */
@Entity
@Data
@NoArgsConstructor
@Table(name="todo_list")
public class TodoList {

    @Id
    @GeneratedValue
    private Long id;
    private String name;

    @OneToMany(mappedBy = "list",
            cascade = CascadeType.ALL,
            fetch = FetchType.LAZY)
    private List<TodoItem> items = new ArrayList<>();

    @OneToOne
    @JoinColumn(name = "OWNER_USER_ID")
    @JsonIgnore
    private User owner;

    public TodoList(String name, User owner) {
        this.name = name;
        this.owner = owner;
    }

    public static TodoList from(TodoListRequest todoListRequest, User user) {
        return new TodoList(todoListRequest.getName(), user);
    }
    
    public static TodoList from(File file, User user) {
        return new TodoList(parseFile(file), user);
    }
    
    private static String parseFile(File file) {
		// TODO set name and add todo items
		return null;
	}

	public void merge(TodoListRequest request) {
        setName(request.getName());
    }
}
