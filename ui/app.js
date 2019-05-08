new Vue({
    el: "#app",
    data: {
        title: 'TODOS',
        todos: [
            {text: 'todo 1', done: true, id: Date.now()},
            {text: 'todo 2', done: false, id: Date.now() + 1}
        ],
        projects: [
        ]
    },
    methods: {
        addTodo(event) {
            const text = event.target.value
            this.todos.push({text, done: false, id: Date.now()})
            event.target.value = ''
        },
        removeTodo(id) {
            this.todos = this.todos.filter(todo => todo.id !== id)
        },
        check(todo){
            todo.done = !todo.done
        }
    },
    mounted() {
      axios.get("http://localhost:5000/project")
      .then(response => {
          this.projects = response.data;
        })
    }
})