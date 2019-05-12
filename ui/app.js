// Define a new component called button-counter
Vue.component('button-counter', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
  })

Vue.component('project-item-component', {
    props: ['projectItem'],
    filters: {},
    methods: {
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
                //TODO: Tell app.js to remove the item?
                this.$parent.getProjectItems();
            });
        }
    },
    template: `<div>
        <ul> 
            <li class="flex"> 
                <label>
                    <input type="checkbox" class="nes-checkbox" v-model="projectItem.done" v-on:click="checkProjectItem(projectItem)">
                    <span>&nbsp</span>
                </label> 
                <del v-if="projectItem.done">{{ projectItem.title }}</del>
                <span v-else>{{ projectItem.title }}</span>
                <div class="space"></div>
                <button class="nes-btn is-error padding" v-on:click="deleteProjectItem(projectItem.id)">X</button>
            </li>
        </ul>
    </div>`
})


const app = new Vue({
    el: "#app",
    data: {
        projectItems: [
        ],
        projects: [
        ]
    },
    methods: {
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
        getProjectItems(){
            axios.get("http://localhost:5000/projectItem").then(response => {
                this.projectItems = response.data;
            });
        }
    },
    mounted() {
        axios.get("http://localhost:5000/project").then(response => {
          this.projects = response.data;
        });
        this.getProjectItems();
    },
    template: `
        <div>
            <div>
                <h1>Some other stuff</h1>
                <ul> 
                    <project-item-component v-for="projectItem in projectItems" v-bind:projectItem="projectItem" />
                </ul>
            </div>
            <input type="text" class="nes-input" placeholder="Add project item..." v-on:keyup.enter="addProjectItem">

            <div id="components-demo">
                <button-counter></button-counter>
            </div>
        </div>
    `
})

