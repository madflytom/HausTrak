<template>
    <mdc-card>
        <mdc-card-primary-action>
        </mdc-card-primary-action>
        <mdc-card-header
            v-bind:title="project.title"
            v-bind:subtitle="'Total Cost: $' + project.totalCost + ' | Total Time: ' + project.totalTime + ' minutes'">
        </mdc-card-header>
        <mdc-card-text>
            <ProjectItem @deleted="getProjectItems" v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
            <form @submit.prevent="handleSubmit">
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
                </label><br />
                <mdc-button id="submitButton" raised dense type="submit">Add Project Item</mdc-button>
            </form>
            <hr>
        </mdc-card-text>
        <mdc-card-actions>
            <mdc-card-action-buttons>
                <mdc-card-action-button v-on:click="deleteProject(project.id)" >DELETE PROJECT</mdc-card-action-button>
            </mdc-card-action-buttons>
        </mdc-card-actions>
    </mdc-card>
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
            this.$axios.get("http://localhost:5000/projectItem/" + projectId).then(response => {
                this.projectItems = response.data;
            });
            this.$emit('changed')
        },
        handleSubmit() {
            this.$axios.post("http://localhost:5000/post_projectItem", {
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
    #projectCard {
        background: #fff;
        border-radius: 4px;
        padding: 20px;
        transition: all 0.2s;
    }
    #submitButton{
        width: 100%
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
</style>
