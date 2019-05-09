new Vue({
    el: "#app",
    data: {
        title: 'TODOS',
        todos: [
            {text: 'todo 1', done: true, id: Date.now()},
            {text: 'todo 2', done: false, id: Date.now() + 1}
        ],
        projectItems: [
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
        },
        addProjectItem(event) {
            const title = event.target.value
            axios.post("http://localhost:5000/post_projectItem", {
                title: title,
                projectId: "3",
                description: "",
                time: 0,
                cost: 0.00,
                done: false
            }).then(response => {
                this.projectItems.push(response.data);
                event.target.value = ''
            });
        },
        checkProjectItem(projectItem){
            done = !projectItem.done
            axios.post("http://localhost:5000/check_projectItem/" + projectItem.id, {
                done: done
            }).then(response => {
                projectItem.done = done
            });
        },
        deleteProjectItem(id){
            axios.delete("http://localhost:5000/delete_projectItem/" + id).then(response => 
            {
                //TODO: maybe return the updated list of project items?
                axios.get("http://localhost:5000/projectItem").then(response => {
                    this.projectItems = response.data;
                });
            });
        }
    },
    mounted() {
        axios.get("http://localhost:5000/project").then(response => {
          this.projects = response.data;
        });
        axios.get("http://localhost:5000/projectItem").then(response => {
            this.projectItems = response.data;
        });
    }
})