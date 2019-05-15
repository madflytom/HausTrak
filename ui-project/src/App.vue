<template>
  <div class="app">
    <mdc-layout-grid>
      <mdc-layout-cell v-for="project in projects" v-bind:key="project.id">
        <Project v-bind:project="project" @changed="getProjectData" />
      </mdc-layout-cell>
      <mdc-layout-cell>
        <input type="text" placeholder="Add new project..." v-on:keyup.enter="addProject" />
      </mdc-layout-cell>
    </mdc-layout-grid>
    
  </div>
</template>

<script>
  import Project from './components/Project.vue'

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
      addProject(event) {
            const title = event.target.value
            this.$axios.post("http://localhost:5000/post_project", {
                title: title,
                userId: 1,
                description: "",
                totalCost: 0,
                totalTime: 0
            }).then(response => {
                this.projects.push(response.data);
                event.target.value = ''
            });
        },
        getProjectData(){
          this.$axios.get("http://localhost:5000/project").then(response => {
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
