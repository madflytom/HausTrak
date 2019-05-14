<template>
<div id="projectCard">
        <div>
            <h1>{{ project.title }}</h1>
            <ul> 
                <ProjectItem v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
            </ul>
        </div>
        <input type="text" class="nes-input" placeholder="Add project item..." v-on:keyup.enter="addProjectItem" />
    </div>
</template>

<script>

import ProjectItem from './ProjectItem.vue'

export default {
  name: 'Project',
  props: {
    project: {}
  },
  data() {
    return {
        projectItems: [] 
    }
  },
  components:{
      ProjectItem
  },
  methods: {
      addProjectItem(event) {
            const title = event.target.value
            this.$axios.post("http://localhost:5000/post_projectItem", {
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
            this.$axios.get("http://localhost:5000/projectItem/" + projectId).then(response => {
                this.projectItems = response.data;
                console.log(this.projectItems);
            });
        }
  },
  mounted() {
        this.getProjectItems(this.project.id);
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #projectCard {
    background: #fff;
    border-radius: 4px;
    padding: 20px;
    transition: all 0.2s;
    }

    li {
    margin: 8px 0;
    }

    del {
    color: rgba(0, 0, 0, 0.3);
    }

    .padding {
    padding: 1px 7px 2px;
    }

    .flex {
    display: flex;
    }

    .space {
    flex-grow: 1;
    }
</style>
