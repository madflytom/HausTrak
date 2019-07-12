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
            this.$axios.put("http://localhost:5000/update_projectItem/" + this.projectItem.id, {
            //this.$axios.put("https://haustrak.herokuapp.com/post_projectItem", {
                title: this.projectItem.title,
                projectId: this.projectItem.projectId,
                description: "",
                time: this.projectItem.time,
                cost: this.projectItem.cost,
                done: false
            }).then(response => {
                console.log(response);
                this.$emit('updated');
            })
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
