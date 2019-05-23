<template>
  <div class="page-container">
    <md-app>
      <md-app-toolbar class="md-primary" md-elevation="1">
        <h3 class="md-title" style="flex: 1">HausTrak</h3>
        <md-button v-show="isLoggedIn()" @click="handleLogout()">Log out</md-button>
        <md-button v-show="!isLoggedIn()" @click="handleLogin()">Log in</md-button>
      </md-app-toolbar>

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


  .accessButtons{
    margin-right: 20px;
  }

  .welcomeDiv{
    margin: 20px;
  }

  html {
    width: 100%;
    height: 100%;
  }

  body {

    width: 100%;
    min-height: 100%;
    margin: 0;
  }
</style>
