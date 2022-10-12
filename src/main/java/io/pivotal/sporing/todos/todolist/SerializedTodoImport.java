package io.pivotal.sporing.todos.todolist;

    import org.springframework.stereotype.Component;

    import java.util.ArrayList;
    import java.util.function.Function;
    import com.thoughtworks.xstream.XStream;

@Component("StoreTodos")
    public class SerializedTodoImport implements Function<ArrayList<TodoItem>, StoreTodosXMLResponse> {

        @Override
        public StoreTodosXMLResponse apply(ArrayList<TodoItem> todos) {
            XStream xStream=new XStream();
            String xml= xStream.toXML(todos);

            return new StoreTodosXMLResponse(xml);
        }
    }

    class ImportTodo {

    private Object obj;
        ImportTodo() {
    }

    public ImportTodo(Object obj) {

        this.obj = obj;
    }

    public Object getObj() {
        return obj;
    }

    public void setObj(Object ob) {
        this.obj = obj;
    }

}
