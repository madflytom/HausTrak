<template>
    <md-card md-with-hover class="cardWide">
        <md-card-header>
          <div class="md-title">{{ project.title }}</div>
          <div class="md-subhead">Total Cost: {{ project.totalCost }} | Total Time: {{ project.totalTime }} minutes </div>
        </md-card-header>

        <md-card-content>
          <ProjectItem @deleted="getProjectItems" v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
            <form @submit.prevent="handleSubmit">
                <div>
                    <label for="projectTitle">
                        Title:
                        <input id="projectTitle" type="text" v-model="newProjectItem.title" required />
                    </label><br />
                    <label for="projectTime">
                        Time(minutes):
                        <input id="projectTime" type="number" v-model="newProjectItem.time" required />
                    </label> <br />
                    <label for="projectCost">
                        Cost($):
                        <input id="projectCost" type="number" min="0.00" step="0.01" v-model="newProjectItem.cost" placeholder="0.00" required />
                    </label>
                </div>
                <div>
                    <md-button id="submitButton" class="md-raised md-accent" type="submit">Add Project Item</md-button>
                </div>
            </form>
            <hr>
        </md-card-content>

        <md-card-actions>
          <md-button v-on:click="deleteProject(project.id)" >DELETE PROJECT</md-button>
        </md-card-actions>
    </md-card>

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
        projectItems: [],
        newProjectItem: 
        {
            title: '',
            time: '',
            cost: ''
        }
    }
  },
  components:{
      ProjectItem
  },
  methods: {
        getProjectItems(projectId){
            //this.$axios.get("https://haustrak.herokuapp.com/projectItem/" + projectId).then(response => {
            this.$axios.get("http://localhost:5000/projectItem/" + projectId).then(response => {
                this.projectItems = response.data;
            });
            this.$emit('changed')
        },
        handleSubmit() {
            this.$axios.post("http://localhost:5000/post_projectItem", {
            //this.$axios.post("https://haustrak.herokuapp.com/post_projectItem", {
                title: this.newProjectItem.title,
                projectId: this.project.id,
                description: "",
                time: this.newProjectItem.time,
                cost: this.newProjectItem.cost,
                done: false
            }).then(response => {
                this.projectItems.push(response.data);
                this.newProjectItem = 
                {
                    title: '',
                    time: '',
                    cost: ''
                };
                this.$emit('changed')
            });
        },
        deleteProject(projectId){
            this.$axios.delete("http://localhost:5000/delete_project/" + projectId).then(() => {
                //this.$axios.delete("https://haustrak.herokuapp.com/delete_project/" + projectId).then(() => {
                this.$emit('changed')
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
    
    .md-button{
        width: 100%;
        margin-left: 0;
        margin-right: 0;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    input, select {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    form {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 20px;
    }

    .cardWide{
        min-width: 350px;
        margin-bottom: 25px;
    }
</style>
