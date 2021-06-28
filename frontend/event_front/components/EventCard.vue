<template>
  <div class="savedCondition">
    <div>
      <p class="keyword">{{ items.keyword }}</p>
      <!-- <p class="not_contain">not : {{ items.notKeyword }}</p> -->
      <p class="address">開催地 : {{ items.address }}</p>
      <!-- <a href="" class="card__link"></a> -->
    </div>
    <div>
      <!-- <span class="date">開催日 : {{ items.start_from }}から</span> -->
      <!-- <span class="date">{{ items.start_to }}</span> -->
      <p class="target">表示数:{{ items.limit }}</p>
      <p class="target">{{ items.target }}</p>
    </div>
    <button class="btn btn-dark button-Btn" @click="setCondition">
      set
    </button>
    <button class="btn btn-secondary button-Btn" @click="deleteCondition">
      delete
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent, PropType } from '@nuxtjs/composition-api'
import { DisplayForm } from '@/types/interfaces'
// class SendForm<SendForms>
export default defineComponent({
  props: {
    items: {
      type: Object as PropType<DisplayForm>,
      default: () => undefined
    }
  },
  setup(_, { emit }) {
    const setCondition = () => {
      emit('set')
    }
    const deleteCondition = () => {
      emit('delete')
    }
    return {
      setCondition,
      deleteCondition
    }
  }
})
</script>
<style scoped>
.savedCondition {
  margin: 30px auto;
  width: 300px;
  background: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px #aaa;
  /* padding: 1em; */
  border: none;
  text-align: center;
}
.savedCondition p {
  margin: 1px;
}
.savedCondition:hover {
  background-color: rgb(107, 103, 101);
  color: #fff;
}
.keyword {
  font-size: 2em;
}
p span {
  font-size: initial;
}
.address {
}
.date {
  font-size: 1em;
}
.card__link::after {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  pointer-events: auto;
  content: '';
  background-color: transparent;
}
.button-Btn {
  margin-top: auto;
  margin-bottom: 10px;
  padding: 1px 6px;
}
</style>
