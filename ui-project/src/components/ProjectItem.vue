<template>
    <div>
        <ul> 
            <li class="flex"> 
                <div v-if="!isEditing">
                    <label>
                        <input type="checkbox" class="nes-checkbox" v-model="projectItem.done" v-on:click="checkProjectItem(projectItem)">
                        <span>&nbsp;</span>
                    </label> 
                
                    <del v-if="projectItem.done"><b>{{ projectItem.title }}</b> <br /> <i>${{projectItem.cost}} - {{ projectItem.time }} min</i></del>
                    <span v-else><b>{{ projectItem.title }}</b> <br /> <i>${{projectItem.cost}} - {{ projectItem.time }} min</i></span>
                </div>
                <EditProjectItem @updated="updated" v-if="isEditing" v-bind:projectItem="projectItem"></EditProjectItem>
                <div class="space"></div>
                <md-button v-on:click="toggleEdit" class="md-icon-button">
                    <md-icon v-if="!isEditing" alt="edit project item">edit</md-icon>
                    <md-icon v-if="isEditing" alt="undo/cancel">undo</md-icon>
                </md-button>
                <md-button v-on:click="deleteProjectItem(projectItem.id)" class="md-icon-button">
                    <md-icon>clear</md-icon>
                </md-button>
            </li>
        </ul>
    </div>
    
</template>

<script>

import EditProjectItem from './EditProjectItem'

export default {
  name: 'ProjectItem',
  props: {
    projectItem: {}
  },
  components:{
      EditProjectItem
  },
  data: function() {
      return {
          isEditing : false
      }
  },
  methods: {
      checkProjectItem(projectItem){
            const done = !projectItem.done
            this.$axios.post("http://localhost:5000/check_projectItem/" + projectItem.id, {
            //this.$axios.post("https://haustrak.herokuapp.com/check_projectItem/" + projectItem.id, {
                done: done
            }).then(() => {
                projectItem.done = done
            });
        },
        deleteProjectItem(id){
            this.$axios.delete("http://localhost:5000/delete_projectItem/" + id).then(() => 
            //this.$axios.delete("https://haustrak.herokuapp.com/delete_projectItem/" + id).then(() => 
            {
                //this.$parent.getProjectItems(this.projectItem.projectId);
                this.$emit('deleted', this.projectItem.projectId)
            });
        },
        toggleEdit(){
            if(!this.isEditing){
                this.isEditing = true;
            } else {
                this.isEditing = false;
            }
            
        },
        updated(){
            console.log("update success");
            this.isEditing = false;
            this.$emit("updated");
        }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    li {
        margin: 8px 0;
    }

    del {
        color: rgba(0, 0, 0, 0.3);
    }

    .padding {
        padding: 1px 7px 2px;
    }

    .flex {
        display: flex;
    }

    .space {
        flex-grow: 1;
    }

    mdc-button {
        cursor: pointer;
    }
    input[type="checkbox"]{
        cursor: pointer;
    }
</style>
