<template>
  <div class="app">
    <mdc-layout-grid>
      <mdc-layout-cell v-for="project in projects" v-bind:key="project.id">
        <Project v-bind:project="project" />
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
            description: 'whatever'
          }
        ]
      }
    },
    components: { Project },
    methods: {},
    mounted() {
      this.$axios.get("http://localhost:5000/project").then(response => {
        this.projects = response.data;
      });
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
