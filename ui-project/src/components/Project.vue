<template>
    <mdc-card>
        <mdc-card-primary-action>
        </mdc-card-primary-action>
        <mdc-card-header
            v-bind:title="project.title"
            subtitle="subtitle here" >
        </mdc-card-header>
        <mdc-card-text>
            <ProjectItem @deleted="getProjectItems" v-for="projectItem in projectItems" v-bind:projectItem="projectItem" v-bind:key="projectItem.id" />
        </mdc-card-text>
        <mdc-card-actions>
            <input type="text" placeholder="Add project item..." v-on:keyup.enter="addProjectItem" />
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
