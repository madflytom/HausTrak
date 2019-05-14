<template>
    <div>
        <ul> 
            <li class="flex"> 
                <label>
                    <input type="checkbox" class="nes-checkbox" v-model="projectItem.done" v-on:click="checkProjectItem(projectItem)">
                    <span>&nbsp;</span>
                </label> 
                <del v-if="projectItem.done">{{ projectItem.title }}</del>
                <span v-else>{{ projectItem.title }}</span>
                <div class="space"></div>
                <button class="nes-btn is-error padding" v-on:click="deleteProjectItem(projectItem.id)">X</button>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
  name: 'ProjectItem',
  props: {
    projectItem: {}
  },
  methods: {
      checkProjectItem(projectItem){
            const done = !projectItem.done
            this.$axios.post("http://localhost:5000/check_projectItem/" + projectItem.id, {
                done: done
            }).then(() => {
                projectItem.done = done
            });
        },
        deleteProjectItem(id){
            this.$axios.delete("http://localhost:5000/delete_projectItem/" + id).then(() => 
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
</style>
