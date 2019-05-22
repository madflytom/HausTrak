<template>
    <mdc-layout-grid>
        <mdc-layout-cell v-for="project in projects" v-bind:key="project.id">
        <Project v-bind:project="project" @changed="getProjectData" />
        </mdc-layout-cell>
        <mdc-layout-cell>
        <input type="text" placeholder="Add new project..." v-on:keyup.enter="addProject" />
        </mdc-layout-cell>
    </mdc-layout-grid>   
</template>

<script>
  import Project from './Project.vue'
  import { isLoggedIn, getSubjectId, getIdToken } from '../utils/auth';

  export default {
    data () {
      return {
        projects: [
          {
            id: 1,
            title: 'some such title',
            description: 'whatever',
            totalCost: 0,
            totalTime: 0
          }
        ]
      }
    },
    components: { Project },
    methods: {
        isLoggedIn() {
            return isLoggedIn();
        },
      addProject(event) {
            const title = event.target.value
            this.$axios.post("http://localhost:5000/post_project", {
                title: title,
                userId: 1,
                description: "",
                totalCost: 0,
                totalTime: 0,
                auth0subject: getSubjectId(getIdToken())
            }).then(response => {
                this.projects.push(response.data);
                event.target.value = ''
            });
        },
        getProjectData(){
            const user = getSubjectId(getIdToken());
            this.$axios.get("http://localhost:5000/project/" + user).then(response => {
                this.projects = response.data;
            });
        }
    },
    mounted() {
      this.getProjectData();
    }
  }
</script>

<style lang="scss">
  // First, set the value for variable
  $mdc-typography-font-family: "Roboto Mono", monospace;

  // Then, import required files
  @import "@material/typography/mixins";

  html {
    width: 100%;
    height: 100%;
  }

  body {
    @include mdc-typography(body2);

    width: 100%;
    min-height: 100%;
    margin: 0;
  }
</style>
