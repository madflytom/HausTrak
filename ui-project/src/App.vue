<template>
  <div class="page-container">
    <md-app>
      <md-toolbar class="md-primary" md-elevation="1">
        <h3 class="md-title" style="flex: 1">HausTrak</h3>
        <md-button v-show="isLoggedIn()" @click="handleLogout()">Log out</md-button>
        <md-button v-show="!isLoggedIn()" @click="handleLogin()">Log in</md-button>
      </md-toolbar>

      <md-app-content>
        <div class="welcomeDiv" v-show="!isLoggedIn()">
        <h1>Welcome to HausTrak!</h1>
        <p>Please log in to view your projects!</p>
      </div>
      <div id="app">
        <router-view/>
      </div>
      </md-app-content>
    </md-app>
  </div>

</template>

<script>
  import { isLoggedIn, login, logout } from './utils/auth';
  export default {
    name: 'app-nav',
    methods: {
      handleLogin() {
        login();
      },
      handleLogout() {
        logout();
      },
      isLoggedIn() {
        return isLoggedIn();
      },
    },
  };
</script>

<style lang="scss">
  // First, set the value for variable
  $mdc-typography-font-family: "Roboto Mono", monospace;

  .accessButtons{
    margin-right: 20px;
  }

  .welcomeDiv{
    margin: 20px;
  }

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
