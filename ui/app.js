
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
                this.$parent.getProjectItems(this.projectItem.projectId);
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

Vue.component('project-component', {
    props: ['project'],
    filters: {},
    data() {
        return {
            projectItems: [] 
        }
    },
    methods: {
        addProjectItem(event) {
            const title = event.target.value
            axios.post("http://localhost:5000/post_projectItem", {
                title: title,
                projectId: this.project.id,
                description: "",
                time: 0,
                cost: 0.00,
                done: false
            }).then(response => {
                this.projectItems.push(response.data);
                event.target.value = ''
            });
        },
        getProjectItems(projectId){
            axios.get("http://localhost:5000/projectItem/" + projectId).then(response => {
                this.projectItems = response.data;
            });
        }
    },
    mounted() {
        this.getProjectItems(this.project.id);
    },
    template: `<div id="projectCard">
        <div>
            <h1>{{ project.title }}</h1>
            <ul> 
                <project-item-component v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
            </ul>
        </div>
        <input type="text" class="nes-input" placeholder="Add project item..." v-on:keyup.enter="addProjectItem" />
    </div>`
})


const app = new Vue({
    el: "#app",
    data: {
        projects: []
    },
    methods: {},
    mounted() {
        axios.get("http://localhost:5000/project").then(response => {
          this.projects = response.data;
        });
    },
    template: `<div>
        <project-component v-for="project in projects" v-bind:project="project" v-bind:key="project.id"/>
    </div>`
})

