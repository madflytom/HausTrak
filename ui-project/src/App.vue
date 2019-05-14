<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Project v-for="project in projects" v-bind:project="project" v-bind:key="project.id" />
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Project from './components/Project.vue'

export default {
  name: 'app',
  components: {
    Project
  },
  data() {
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
  methods: {},
  mounted() {
      this.$axios.get("http://localhost:5000/project").then(response => {
        this.projects = response.data;
      });
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
