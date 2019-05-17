<template>
    <mdc-card>
        <mdc-card-primary-action>
        </mdc-card-primary-action>
        <mdc-card-header
            v-bind:title="project.title"
            v-bind:subtitle="'Total Cost: $' + project.totalCost.toString() + ' | Total Time: ' + project.totalTime.toString() + ' minutes'">
        </mdc-card-header>
        <mdc-card-text>
            <ProjectItem @deleted="getProjectItems" v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
        </mdc-card-text>
        <mdc-card-actions>
            <form @submit.prevent="handleSubmit">
                <label>
                    Title:
                    <input type="text" v-model="newProjectItem.title" required />
                </label>
                <label>
                    Time(minutes):
                    <input type="number" v-model="newProjectItem.time" required />
                </label>
                <label>
                    Cost($):
                    <input type="number" min="0.00" step="0.01" v-model="newProjectItem.cost" placeholder="0.00" required />
                </label>
                <button type="submit">Add Project Item</button>
            </form>
            <button class="material-icons mdc-icon-button mdc-card__action mdc-card__action--icon" title="delete_forever" v-on:click="deleteProject(project.id)">delete_forever</button>
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
</style>
