<template>
    <div>
        <form @submit.prevent="handleSubmit">
                <div>
                    <label for="projectTitle">
                        Title:
                        <input id="projectTitle" type="text" v-model="projectItem.title" required />
                    </label><br />
                    <label for="projectTime">
                        Time(minutes):
                        <input id="projectTime" type="number" v-model="projectItem.time" required />
                    </label> <br />
                    <label for="projectCost">
                        Cost($):
                        <input id="projectCost" type="number" min="0.00" step="0.01" v-model="projectItem.cost" placeholder="0.00" required />
                    </label>
                </div>
                <div>
                    <md-button id="submitButton" class="md-raised md-accent" type="submit">Update Project Item</md-button>
                </div>
            </form>
    </div>
</template>

<script>
export default {
  name: 'ProjectItem',
  props: {
    projectItem: {}
  },
  methods: {
      handleSubmit() {
          console.log(this.projectItem.title);
            /* TODO: This will need to be an update endpoint. 
            
            this.$axios.post("http://localhost:5000/post_projectItem", {
            //this.$axios.post("https://haustrak.herokuapp.com/post_projectItem", {
                title: this.projectItem.title,
                projectId: this.project.id,
                description: "",
                time: this.projectItem.time,
                cost: this.projectItem.cost,
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
            });*/
        },
        deleteProjectItem(id){
            this.$axios.delete("http://localhost:5000/delete_projectItem/" + id).then(() => 
            //this.$axios.delete("https://haustrak.herokuapp.com/delete_projectItem/" + id).then(() => 
            {
                //this.$parent.getProjectItems(this.projectItem.projectId);
                this.$emit('deleted', this.projectItem.projectId)
            });
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
